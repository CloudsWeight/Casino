# blackjack/simulation.py
import random
from dataclasses import dataclass, field
from card       import Card, Suit, Rank
from deck       import Shoe
from hand       import Hand
from strategy   import basic_strategy, i18_deviation
from game_stats import HandRecord, GameStats

# ─────────────────────────────────────────────
# PLAYER TYPES — just two now
# ─────────────────────────────────────────────
TYPE_AGGRESSIVE = 'aggressive'
TYPE_BASIC      = 'basic'
TYPE_RANDOM     = 'random'     # other table players only

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
@dataclass
class SimConfig:
    num_games:         int   = 100
    num_decks:         int   = 6
    starting_bankroll: float = 500.0
    base_bet:          float = 15.0
    min_bet:           float = 15.0
    max_bet:           float = 1000.0
    penetration:       float = 0.75
    num_other_players: int   = 3    # random players at table

# ─────────────────────────────────────────────
# SIM PLAYER STATE
# ─────────────────────────────────────────────
@dataclass
class SimPlayer:
    name:             str
    player_type:      str
    bankroll:         float
    hand:             Hand  = field(default_factory=Hand)
    bet:              float = 0.0
    last_result:      str   = 'none'
    last_bet:         float = 15.0
    consecutive_wins: int   = 0
    peak_bankroll:    float = 0.0

    def __post_init__(self):
        self.peak_bankroll = self.bankroll

    def reset_hand(self):
        self.hand = Hand()
        self.bet  = 0.0

    def update_streak(self, outcome: str):
        if outcome in ('win', 'blackjack'):
            self.consecutive_wins += 1
        else:
            self.consecutive_wins  = 0
        self.last_result       = outcome
        self.last_bet          = self.bet
        self.peak_bankroll     = max(self.peak_bankroll, self.bankroll)

# ─────────────────────────────────────────────
# BET SIZING
# ─────────────────────────────────────────────
def aggressive_bet(player:          SimPlayer,
                   true_count:      float,
                   running_count:   int,
                   aces_remaining:  int,
                   decks_remaining: float,
                   cfg:             SimConfig) -> float:
    expected_aces = decks_remaining * 4
    ace_rich      = aces_remaining > expected_aces * 1.15

    # anchor bet — emotional cover at negative count
    if true_count <= -3 and random.random() < 0.08:
        return min(95.0, player.bankroll)

    # push behavior — won big at high count, let it ride
    if (player.last_result in ('win', 'blackjack') and
        true_count >= 3 and
        player.consecutive_wins <= 4 and
        player.last_bet >= 100):
        return min(player.last_bet, player.bankroll)

    # flat base while count is low
    if true_count < 1:
        return cfg.base_bet

    # TC +1 — double base
    if true_count < 2:
        return min(cfg.base_bet * 2, player.bankroll)

    # TC +2 — quadruple, more if ace rich
    if true_count < 3:
        bet = cfg.base_bet * 4
        if ace_rich:
            bet = max(bet, player.bankroll * 0.15)
        return min(bet, player.bankroll)

    # TC +3+ — aggressive, near all-in if ace rich
    if ace_rich:
        return min(player.bankroll, cfg.max_bet)
    return min(player.bankroll * 0.80, cfg.max_bet)


def basic_bet(cfg: SimConfig) -> float:
    return cfg.base_bet


def random_bet(bankroll: float, cfg: SimConfig) -> float:
    multiplier = random.choice([1, 1, 1, 2, 3])
    return min(cfg.base_bet * multiplier, bankroll)

# ─────────────────────────────────────────────
# SETTLE HAND — returns outcome string
# ─────────────────────────────────────────────
def settle_hand(player:      SimPlayer,
                dealer_hand: Hand,
                is_doubled:  bool) -> tuple[str, float]:

    p = player.hand.score
    d = dealer_hand.score

    if player.hand.is_bust:
        outcome = 'bust'
        payout  = 0.0

    elif player.hand.is_blackjack and not dealer_hand.is_blackjack:
        outcome = 'blackjack'
        payout  = player.bet * 2.5

    elif dealer_hand.is_blackjack and not player.hand.is_blackjack:
        outcome = 'lose'
        payout  = 0.0

    elif dealer_hand.is_bust:
        outcome = 'win'
        payout  = player.bet * 2

    elif p > d:
        outcome = 'win'
        payout  = player.bet * 2

    elif p < d:
        outcome = 'lose'
        payout  = 0.0

    else:
        outcome = 'push'
        payout  = player.bet

    player.bankroll += payout
    player.update_streak(outcome)
    return outcome, payout

# ─────────────────────────────────────────────
# RUN ONE GAME (SHOE)
# ─────────────────────────────────────────────
def run_game(game_number: int,
             cfg:         SimConfig) -> tuple[GameStats, GameStats]:
    """
    Runs one shoe with:
      - 1 aggressive counter
      - 1 basic strategy player
      - N random players (table fillers)

    Returns GameStats for aggressive and basic players only
    """
    shoe = Shoe(cfg.num_decks)

    aggressive = SimPlayer('Counter', TYPE_AGGRESSIVE, cfg.starting_bankroll)
    basic_p    = SimPlayer('Basic',   TYPE_BASIC,      cfg.starting_bankroll)
    randoms    = [
        SimPlayer(f'Rand{i+1}', TYPE_RANDOM, cfg.starting_bankroll)
        for i in range(cfg.num_other_players)
    ]
    all_players = [aggressive, basic_p] + randoms

    agg_stats   = GameStats(
        game_number    = game_number,
        player_name    = 'Counter',
        player_type    = TYPE_AGGRESSIVE,
        start_bankroll = cfg.starting_bankroll,
        end_bankroll   = cfg.starting_bankroll,
        peak_bankroll  = cfg.starting_bankroll,
    )
    basic_stats = GameStats(
        game_number    = game_number,
        player_name    = 'Basic',
        player_type    = TYPE_BASIC,
        start_bankroll = cfg.starting_bankroll,
        end_bankroll   = cfg.starting_bankroll,
        peak_bankroll  = cfg.starting_bankroll,
    )

    running_count = 0
    aces_seen     = 0
    cut_card      = int(shoe.remaining * cfg.penetration)
    hand_number   = 0

    def hi_lo(card: Card):
        nonlocal running_count, aces_seen
        if not card.face_up:
            return
        if card.value <= 6:
            running_count += 1
        elif card.value >= 10:
            running_count -= 1
        if card.rank.value == 'A':
            aces_seen += 1

    def deal_card(recipient: SimPlayer, face_up: bool = True) -> Card:
        card         = shoe.deal()
        card.face_up = face_up
        recipient.hand.add_card(card)
        hi_lo(card)
        return card

    while shoe.remaining > cut_card:
        # skip players who are broke
        active = [p for p in all_players if p.bankroll >= cfg.min_bet]
        if not active:
            break

        hand_number    += 1
        decks_remaining = max(shoe.remaining / 52, 0.5)
        true_count      = running_count / decks_remaining
        aces_remaining  = max((cfg.num_decks * 4) - aces_seen, 0)

        # reset hands
        for p in all_players:
            p.reset_hand()

        # dealer state
        class Dealer:
            hand = Hand()
            def reset(self): self.hand = Hand()
        dealer = Dealer()

        # ── BETS ──
        for p in all_players:
            if p.bankroll < cfg.min_bet:
                continue
            if p.player_type == TYPE_AGGRESSIVE:
                raw = aggressive_bet(
                    p, true_count, running_count,
                    aces_remaining, decks_remaining, cfg
                )
            elif p.player_type == TYPE_BASIC:
                raw = basic_bet(cfg)
            else:
                raw = random_bet(p.bankroll, cfg)

            p.bet       = max(cfg.min_bet,
                              min(raw, p.bankroll, cfg.max_bet))
            p.bankroll -= p.bet

        # ── INITIAL DEAL ──
        for _ in range(2):
            for p in all_players:
                if p.bet > 0:
                    deal_card(p)
            face_up = len(dealer.hand.cards) == 0
            c          = shoe.deal()
            c.face_up  = face_up
            dealer.hand.add_card(c)
            hi_lo(c)

        dealer_upcard     = dealer.hand.cards[0]
        dealer_upcard_val = min(dealer_upcard.value, 10)

        # ── PLAYER TURNS ──
        # track per-hand info for stats recording
        hand_info = {}  # player_name → {action, correct, i18, doubled}

        for p in all_players:
            if p.bet == 0 or p.hand.is_blackjack:
                hand_info[p.name] = {
                    'action':  'BJ' if p.hand.is_blackjack else 'N',
                    'correct': 'BJ',
                    'i18':     False,
                    'doubled': False,
                }
                continue

            initial_score   = p.hand.score
            initial_is_soft = p.hand.is_soft
            initial_is_pair = p.hand.is_pair
            doubled         = False
            action_taken    = 'S'
            correct_action  = 'S'
            used_i18        = False

            done = False
            while not done:
                score      = p.hand.score
                is_soft    = p.hand.is_soft
                can_double = p.hand.can_double and p.bankroll >= p.bet

                correct = basic_strategy(
                    score, dealer_upcard_val, is_soft, can_double
                )

                if p.player_type in (TYPE_AGGRESSIVE, TYPE_BASIC):
                    dev = i18_deviation(
                        score, dealer_upcard_val,
                        is_soft, true_count, can_double
                    ) if p.player_type == TYPE_AGGRESSIVE else None

                    if dev:
                        action   = dev
                        used_i18 = True
                    else:
                        action = correct

                else:  # random
                    if random.random() < 0.35:
                        choices = ['H', 'S']
                        if can_double: choices.append('D')
                        if correct in choices and len(choices) > 1:
                            choices.remove(correct)
                        action = random.choice(choices)
                    else:
                        action = correct

                # record first decision
                if not hand_info.get(p.name):
                    action_taken   = action
                    correct_action = correct

                if action == 'D' and can_double:
                    p.bankroll -= p.bet
                    p.bet      *= 2
                    deal_card(p)
                    doubled = True
                    done    = True

                elif action == 'S':
                    done = True

                elif action == 'H':
                    deal_card(p)
                    if p.hand.is_bust or p.hand.score >= 21:
                        done = True

                else:
                    done = True

            hand_info[p.name] = {
                'action':          action_taken,
                'correct':         correct_action,
                'i18':             used_i18,
                'doubled':         doubled,
                'initial_score':   initial_score,
                'initial_is_soft': initial_is_soft,
                'initial_is_pair': initial_is_pair,
            }

        # ── DEALER TURN ──
        for card in dealer.hand.cards:
            card.face_up = True
            hi_lo(card)

        while True:
            ds = dealer.hand.score
            if ds < 17 or (ds == 17 and dealer.hand.is_soft):
                c          = shoe.deal()
                c.face_up  = True
                dealer.hand.add_card(c)
                hi_lo(c)
            else:
                break

        # ── SETTLE AND RECORD ──
        for p in all_players:
            if p.bet == 0:
                continue

            bankroll_before = p.bankroll
            outcome, payout = settle_hand(p, dealer.hand,
                                          hand_info.get(p.name, {}).get('doubled', False))
            bankroll_after  = p.bankroll

            info = hand_info.get(p.name, {})

            # only record stats for aggressive and basic players
            if p.player_type in (TYPE_AGGRESSIVE, TYPE_BASIC):
                record = HandRecord(
                    game_number      = game_number,
                    hand_number      = hand_number,
                    player_name      = p.name,
                    player_type      = p.player_type,
                    player_total     = info.get('initial_score', p.hand.score),
                    dealer_upcard    = dealer_upcard_val,
                    is_soft          = info.get('initial_is_soft', False),
                    is_pair          = info.get('initial_is_pair', False),
                    is_blackjack     = p.hand.is_blackjack,
                    num_cards        = len(p.hand.cards),
                    true_count       = true_count,
                    running_count    = running_count,
                    aces_remaining   = aces_remaining,
                    decks_remaining  = decks_remaining,
                    action_taken     = info.get('action', 'S'),
                    correct_action   = info.get('correct', 'S'),
                    was_correct      = info.get('action') == info.get('correct'),
                    was_i18          = info.get('i18', False),
                    bet              = p.bet,
                    outcome          = outcome,
                    payout           = payout,
                    net              = payout - p.bet,
                    bankroll_before  = bankroll_before,
                    bankroll_after   = bankroll_after,
                )

                stats = agg_stats if p.player_type == TYPE_AGGRESSIVE \
                        else basic_stats
                stats.end_bankroll  = p.bankroll
                stats.peak_bankroll = p.peak_bankroll
                stats.add_hand(record)

    # final bankroll sync
    agg_stats.end_bankroll   = aggressive.bankroll
    agg_stats.peak_bankroll  = aggressive.peak_bankroll
    agg_stats.net_profit     = aggressive.bankroll - cfg.starting_bankroll

    basic_stats.end_bankroll  = basic_p.bankroll
    basic_stats.peak_bankroll = basic_p.peak_bankroll
    basic_stats.net_profit    = basic_p.bankroll - cfg.starting_bankroll

    return agg_stats, basic_stats

# ─────────────────────────────────────────────
# RUN ALL GAMES
# ─────────────────────────────────────────────
def run_simulation(cfg: SimConfig) -> dict:
    print(f'  Running {cfg.num_games} games...\n')

    all_agg_stats   = []
    all_basic_stats = []

    for g in range(1, cfg.num_games + 1):
        if g % 100 == 0:
            print(f'  Game {g}/{cfg.num_games}...')

        agg, basic = run_game(g, cfg)
        all_agg_stats.append(agg)
        all_basic_stats.append(basic)

    return {
        'aggressive': all_agg_stats,
        'basic':      all_basic_stats,
        'config':     cfg,
    }