# blackjack/deck.py
import random
from card import Card, Suit, Rank

class Shoe:
    NUM_DECKS = 6

    def __init__(self, num_decks: int = 6):
        self.NUM_DECKS = num_decks
        self.cards: list[Card] = []
        self.build()
        self.shuffle()

    def build(self):
        self.cards = [
            Card(rank, suit)
            for _ in range(self.NUM_DECKS)
            for suit in Suit
            for rank in Rank
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self) -> Card:
        if len(self.cards) < 52:
            self.build()
            self.shuffle()
        return self.cards.pop()

    @property
    def remaining(self) -> int:
        return len(self.cards)

    @property
    def decks_remaining(self) -> float:
        return round(self.remaining / 52, 2)