# blackjack/card.py
from dataclasses import dataclass
from enum import Enum

class Suit(Enum):
    HEARTS   = '♥'
    DIAMONDS = '♦'
    CLUBS    = '♣'
    SPADES   = '♠'

class Rank(Enum):
    TWO   = '2';  THREE = '3'; FOUR  = '4'
    FIVE  = '5';  SIX   = '6'; SEVEN = '7'
    EIGHT = '8';  NINE  = '9'; TEN   = '10'
    JACK  = 'J';  QUEEN = 'Q'; KING  = 'K'
    ACE   = 'A'

RANK_VALUES = {
    '2': 2,  '3': 3,  '4': 4,  '5': 5,  '6': 6,
    '7': 7,  '8': 8,  '9': 9,  '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

@dataclass
class Card:
    rank: Rank
    suit: Suit
    face_up: bool = True

    @property
    def value(self) -> int:
        return RANK_VALUES[self.rank.value]

    def __str__(self) -> str:
        if not self.face_up:
            return '[??]'
        return f'[{self.rank.value}{self.suit.value}]'

    def __repr__(self) -> str:
        return self.__str__()