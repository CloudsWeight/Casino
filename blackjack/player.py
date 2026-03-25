# blackjack/player.py
from hand import Hand

class Player:
    def __init__(self, name: str, bankroll: float = 500.0):
        self.name      = name
        self.bankroll  = bankroll
        self.hand      = Hand()
        self.bet       = 0.0
        self.is_active = True      # still in the round
        self.standing  = False

    def place_bet(self, amount: float) -> bool:
        if amount > self.bankroll:
            print(f"  ❌  {self.name} can't bet ${amount:.0f} "
                  f"— only ${self.bankroll:.0f} available")
            return False
        self.bet       = amount
        self.bankroll -= amount
        return True

    def receive_card(self, card):
        self.hand.add_card(card)

    def reset(self):
        self.hand      = Hand()
        self.bet       = 0.0
        self.is_active = True
        self.standing  = False

    def __repr__(self) -> str:
        return f'{self.name} (${self.bankroll:.0f})'


class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = Hand()

    def receive_card(self, card):
        self.hand.add_card(card)

    def reset(self):
        self.hand = Hand()

    def should_hit(self) -> bool:
        # dealer hits on soft 17 — standard Vegas rules
        return (self.hand.score < 17 or
               (self.hand.score == 17 and self.hand.is_soft))

    def __repr__(self) -> str:
        return 'Dealer'