# blackjack/hand.py
from card import Card

class Hand:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    @property
    def score(self) -> int:
        total = sum(c.value for c in self.cards if c.face_up)
        aces  = sum(1 for c in self.cards
                    if c.rank.value == 'A' and c.face_up)
        while total > 21 and aces:
            total -= 10
            aces  -= 1
        return total

    @property
    def is_bust(self) -> bool:
        return self.score > 21

    @property
    def is_blackjack(self) -> bool:
        return len(self.cards) == 2 and self.score == 21

    @property
    def is_soft(self) -> bool:
        total = sum(c.value for c in self.cards if c.face_up)
        aces  = sum(1 for c in self.cards
                    if c.rank.value == 'A' and c.face_up)
        return aces > 0 and total <= 21

    @property
    def is_pair(self) -> bool:
        return (len(self.cards) == 2 and
                self.cards[0].rank == self.cards[1].rank)

    @property
    def can_double(self) -> bool:
        return len(self.cards) == 2

    def __repr__(self) -> str:
        return f'{self.cards} = {self.score}'