# blackjack/game_stats.py
from dataclasses import dataclass, field

# ─────────────────────────────────────────────
# HAND RECORD — every hand played in a game
# ─────────────────────────────────────────────
@dataclass
class HandRecord:
    game_number:    int
    hand_number:    int
    player_name:    str
    player_type:    str

    # hand composition
    player_total:   int
    dealer_upcard:  int
    is_soft:        bool
    is_pair:        bool
    is_blackjack:   bool
    num_cards:      int

    # count info
    true_count:     float
    running_count:  int
    aces_remaining: int
    decks_remaining: float

    # decision
    action_taken:   str
    correct_action: str
    was_correct:    bool
    was_i18:        bool        # used a count-based deviation

    # bet and outcome
    bet:            float
    outcome:        str         # win / lose / push / bust / blackjack
    payout:         float
    net:            float       # payout - bet

    # bankroll snapshot
    bankroll_before: float
    bankroll_after:  float

    def to_dict(self) -> dict:
        return {
            'game':            self.game_number,
            'hand':            self.hand_number,
            'player':          self.player_name,
            'type':            self.player_type,
            'playerTotal':     self.player_total,
            'dealerUpcard':    self.dealer_upcard,
            'isSoft':          self.is_soft,
            'isPair':          self.is_pair,
            'isBlackjack':     self.is_blackjack,
            'numCards':        self.num_cards,
            'trueCount':       round(self.true_count, 2),
            'runningCount':    self.running_count,
            'acesRemaining':   self.aces_remaining,
            'decksRemaining':  round(self.decks_remaining, 2),
            'action':          self.action_taken,
            'correctAction':   self.correct_action,
            'wasCorrect':      self.was_correct,
            'wasI18':          self.was_i18,
            'bet':             self.bet,
            'outcome':         self.outcome,
            'payout':          self.payout,
            'net':             round(self.net, 2),
            'bankrollBefore':  self.bankroll_before,
            'bankrollAfter':   self.bankroll_after,
        }

# ─────────────────────────────────────────────
# GAME STATS — aggregated per game (shoe)
# ─────────────────────────────────────────────
@dataclass
class GameStats:
    game_number:     int
    player_name:     str
    player_type:     str

    # bankroll
    start_bankroll:  float
    end_bankroll:    float
    peak_bankroll:   float
    net_profit:      float = 0.0

    # hand counts
    total_hands:     int   = 0
    wins:            int   = 0
    losses:          int   = 0
    pushes:          int   = 0
    busts:           int   = 0
    blackjacks:      int   = 0

    # hand type counts
    soft_hands:      int   = 0
    hard_hands:      int   = 0
    pairs_dealt:     int   = 0
    doubles_taken:   int   = 0
    i18_deviations:  int   = 0

    # strategy accuracy
    correct_plays:   int   = 0
    incorrect_plays: int   = 0

    # bet tracking
    total_wagered:   float = 0.0
    max_bet:         float = 0.0
    min_bet:         float = 999999.0

    # count situations
    hands_at_plus1:  int   = 0
    hands_at_plus2:  int   = 0
    hands_at_plus3:  int   = 0
    hands_negative:  int   = 0

    # hand records for this game
    hand_records:    list  = field(default_factory=list)

    def add_hand(self, record: 'HandRecord'):
        self.hand_records.append(record)
        self.total_hands    += 1
        self.total_wagered  += record.bet
        self.max_bet         = max(self.max_bet, record.bet)
        self.min_bet         = min(self.min_bet, record.bet)
        self.net_profit      = self.end_bankroll - self.start_bankroll

        if record.is_soft:    self.soft_hands      += 1
        else:                 self.hard_hands      += 1
        if record.is_pair:    self.pairs_dealt     += 1
        if record.action_taken == 'D': self.doubles_taken += 1
        if record.was_i18:    self.i18_deviations  += 1
        if record.was_correct: self.correct_plays  += 1
        else:                  self.incorrect_plays += 1

        if record.outcome == 'win':       self.wins       += 1
        elif record.outcome == 'lose':    self.losses     += 1
        elif record.outcome == 'push':    self.pushes     += 1
        elif record.outcome == 'bust':    self.busts      += 1
        elif record.outcome == 'blackjack': self.blackjacks += 1

        tc = record.true_count
        if tc >= 3:   self.hands_at_plus3 += 1
        elif tc >= 2: self.hands_at_plus2 += 1
        elif tc >= 1: self.hands_at_plus1 += 1
        else:         self.hands_negative += 1

    @property
    def win_rate(self) -> float:
        total = self.wins + self.losses + self.pushes + self.busts
        return self.wins / total if total > 0 else 0.0

    @property
    def accuracy(self) -> float:
        total = self.correct_plays + self.incorrect_plays
        return self.correct_plays / total if total > 0 else 0.0

    @property
    def went_broke(self) -> bool:
        return self.end_bankroll <= 0

    @property
    def roi(self) -> float:
        return self.net_profit / self.start_bankroll if self.start_bankroll else 0.0

    def to_dict(self) -> dict:
        return {
            'game':            self.game_number,
            'player':          self.player_name,
            'type':            self.player_type,
            'startBankroll':   self.start_bankroll,
            'endBankroll':     self.end_bankroll,
            'peakBankroll':    self.peak_bankroll,
            'netProfit':       round(self.net_profit, 2),
            'roi':             round(self.roi, 4),
            'totalHands':      self.total_hands,
            'wins':            self.wins,
            'losses':          self.losses,
            'pushes':          self.pushes,
            'busts':           self.busts,
            'blackjacks':      self.blackjacks,
            'softHands':       self.soft_hands,
            'hardHands':       self.hard_hands,
            'pairsDealt':      self.pairs_dealt,
            'doublesTaken':    self.doubles_taken,
            'i18Deviations':   self.i18_deviations,
            'correctPlays':    self.correct_plays,
            'incorrectPlays':  self.incorrect_plays,
            'accuracy':        round(self.accuracy, 4),
            'winRate':         round(self.win_rate, 4),
            'totalWagered':    round(self.total_wagered, 2),
            'maxBet':          self.max_bet,
            'minBet':          self.min_bet if self.min_bet < 999999 else 0,
            'handsAtPlus1':    self.hands_at_plus1,
            'handsAtPlus2':    self.hands_at_plus2,
            'handsAtPlus3':    self.hands_at_plus3,
            'handsNegative':   self.hands_negative,
            'wentBroke':       self.went_broke,
        }