# blackjack/aggressive_strategy.py

from dataclasses import dataclass

@dataclass 
class AggressiveCounterConfig:
    """
    - $15 flat while count is low/negative
    - Anchor bet (emotional cover) at negative TC
    - Aggressive scaling at TC +2/+3 with aces
    - All-in capability when count justifies
    - Push winning bets at high TC
    """
    starting_bankroll:  float = 500.0
    base_bet:           float = 15.0
    anchor_bet:         float = 25.0    # the "emotional" cover bet
    anchor_tc:          float = -3.0    # when to throw anchor
    anchor_frequency:   float = 0.03    # ~3% chance when TC negative
    
    # escalation thresholds
    tc_double:          float = 1.0     # 2× base at TC +1
    tc_quadruple:       float = 2.0     # 4× base at TC +2
    tc_aggressive:      float = 3.0     # all-in mode at TC +3
    
    # ace richness multiplier
    ace_rich_multiplier: float = 1.5    # 50% more when ace rich
    
    # push behavior after wins
    push_wins_at_tc:    float = 1.0     # push bet after win at TC +3
    max_pushes:         int   = 3       # max consecutive pushes
    
    # all-in threshold
    all_in_tc:          float = 3.0     # go all-in at TC +3
    all_in_bankroll_pct: float = .85    # % of bankroll


def aggressive_bet_size(
    bankroll:        float,
    true_count:      float,
    running_count:   int,
    aces_remaining:  int,
    decks_remaining: float,
    base_bet:        float,
    last_result:     str,
    last_bet:        float,
    consecutive_wins: int,
    cfg:             AggressiveCounterConfig
) -> float:
    """
    Models the aggressive counter strategy exactly as described.
    Includes:
    - Anchor bets as emotional cover
    - Quadruple+ scaling at high TC
    - Push behavior after wins
    - All-in at TC +3+ with aces
    """
    import random

    # ace richness calculation
    expected_aces = decks_remaining * 4
    ace_rich      = aces_remaining > (expected_aces * 1.15)
    ace_factor    = cfg.ace_rich_multiplier if ace_rich else 1.0

    # ── ANCHOR BET LOGIC ──
    # throw an "emotional" bet at negative count as cover
    if (true_count <= cfg.anchor_tc and
        random.random() < cfg.anchor_frequency):
        return min(cfg.anchor_bet, bankroll)

    # ── PUSH BEHAVIOR ──
    # after winning at high TC, push the bet
    if (last_result == 'win' and
        true_count >= cfg.push_wins_at_tc and
        consecutive_wins <= cfg.max_pushes and
        last_bet >= 100):
        return min(last_bet, bankroll)  # keep same bet

    # ── NEGATIVE / NEUTRAL COUNT ──
    if true_count < 1:
        return min(base_bet, bankroll)

    # ── RC +3 → double ──
    if running_count >= 1 and running_count < 3:
        bet = base_bet * 4 * ace_factor
        return min(bet, bankroll)

    # ── RC +7 → quadruple ──
    if running_count >= 4 and running_count < 7:
        bet = base_bet * 8 * ace_factor
        if ace_rich:
            bet = max(bet, bankroll * 0.15)  # at least 15% of stack
        return min(bet, bankroll)

    # ── TC +3 → AGGRESSIVE ──
    if running_count >= 8:
        if ace_rich:
            # go all-in or near all-in
            bet = bankroll * cfg.all_in_bankroll_pct
        else:
            # 80% of bankroll
            bet = bankroll * 0.55
        return min(bet, bankroll)

    return min(base_bet, bankroll)