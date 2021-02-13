# Copyright 2018-2021 Yegor Bitensky

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# -*- coding: utf-8 -*-

import random

from agstuff.exceptions.cards import (
    CardWeightSymbolError, CardSuitSymbolError,
    DeckCountTypeError, DeckCountNumberError,
    CardsStringTypeError, CardsCardTypeError
)
from agstuff.validators.cards import CardSymbolValidator


class Card:
    """
    Some card from standard 52 cards deck.

    Takes one positional argument consisting of two symbols
    1st symbol is card weight one of
        '1' (Ace), '2' (Two), '3' (Three), '4' (Four), '5' (Five), '6' (Six), '7' (Seven),
        '8' (Eight), '9' (Nine), 'T' (Ten), 'J' (Jack), 'Q' (Queen), 'K' (King), 'A' (Ace).
    2nd symbol is card suit one of
        'c' (clubs), 'd' (diamonds), 'h' (hearts), 's' (spades).
    Five of spades looks like Card('5s').

    Also possible create an abstract card (with one symbol).
    Abstract Five looks like Card('5').
    Abstract spades looks like Card('s').

    Keyword arguments are ignored.
    Positional arguments are ignored since 2nd one.
    Symbols in 1st positional argument are ignored since 3rd one.
    """


    class Weight:
        """
        Card weight.
        From Two to Ace (Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace).
        Ace actually may worth smaller than Two at some point.

        Attributes:
            symbol -- one of
                '1' (Ace), '2' (Two), '3' (Three), '4' (Four), '5' (Five), '6' (Six), '7' (Seven),
                '8' (Eight), '9' (Nine), 'T' (Ten), 'J' (Jack), 'Q' (Queen), 'K' (King), 'A' (Ace).

        Five looks like Weight('5').
        """

        SYMBOLS = '123456789TJQKA'
        REAL_SYMBOLS = '23456789TJQKA'
        NAMES = 'Ace/Two/Three/Four/Five/Six/Seven/Eight/Nine/Ten/Jack/Queen/King/Ace'.split('/')
        NUMBERS_BY_SYMBOLS = {s: i for i, s in enumerate(SYMBOLS)}
        NAMES_BY_SYMBOLS = dict(zip(SYMBOLS, NAMES))

        @CardSymbolValidator(SYMBOLS, CardWeightSymbolError)
        def __init__(self, symbol):
            self.symbol = symbol
            self.number = self.NUMBERS_BY_SYMBOLS[symbol]
            self.name = self.NAMES_BY_SYMBOLS[symbol]

        def __str__(self):
            return self.symbol

        def __repr__(self):
            return self.symbol

        def __lt__(self, other):
            return self.number < other.number

        def __gt__(self, other):
            return self.number > other.number

        def __eq__(self, other):
            return self.number == other.number

        def __ne__(self, other):
            return self.number != other.number


    class Suit:
        """
        Card suit.
        May be clubs, diamonds, hearts or spades.

        Attributes:
            symbol -- one of 'c' (clubs), 'd' (diamonds), 'h' (hearts), 's' (spades).

        Spades looks like Suit('s').
        """

        SYMBOLS = 'cdhs'
        PRETTY_SYMBOLS = {
            'c': '\u2663',
            'd': '\u2666',
            'h': '\u2665',
            's': '\u2660'
        }
        NAMES = 'clubs/diamonds/hearts/spades'.split('/')
        NUMBERS_BY_SYMBOLS = {s: i for i, s in enumerate(SYMBOLS)}
        NAMES_BY_SYMBOLS = dict(zip(SYMBOLS, NAMES))

        @CardSymbolValidator(SYMBOLS, CardSuitSymbolError)
        def __init__(self, symbol):
            self.symbol = symbol
            self.number = self.NUMBERS_BY_SYMBOLS[symbol]
            self.name = self.NAMES_BY_SYMBOLS[symbol]

        def __str__(self):
            return self.pretty_symbol

        def __repr__(self):
            return self.pretty_symbol

        def __eq__(self, other):
            return self.symbol == other.symbol

        def __ne__(self, other):
            return self.symbol != other.symbol

        @property
        def pretty_symbol(self):
            return self.PRETTY_SYMBOLS[self.symbol]


    def __init__(self, sign):
        # standard card with weight and suit
        if len(sign[:2]) == 2:
            self.weight = self.Weight(sign[0])
            self.suit = self.Suit(sign[1])
            self.name = f"{self.weight.name} of {self.suit.name}"
        # abstract card
        else:
            # with weight only
            try:
                self.weight = self.Weight(sign)
                self.suit = None
                self.name = self.weight.name
            # with suit only
            except CardWeightSymbolError:
                self.weight = None
                self.suit = self.Suit(sign)
                self.name = self.suit.name
        self.in_hand = False

    def __str__(self):
        weight = str(self.weight) if self.weight else 'X'
        suit = str(self.suit) if self.suit else 'x'
        return f"{weight}{suit}"

    def __repr__(self):
        weight = repr(self.weight) if self.weight else 'X'
        suit = repr(self.suit) if self.suit else 'x'
        return f"{weight}{suit}"

    def __hash__(self):
        waight_number = (self.weight.number + 1 if self.weight else 0)
        suit_number = (self.suit.number + 1 if self.suit else 0)
        return 10 * waight_number + suit_number

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight if self.weight and other.weight else self.suit == other.suit

    def __ne__(self, other):
        return self.weight != other.weight if self.weight and other.weight else self.suit != other.suit


class Deck:
    """
    Standard 52 cards deck.
    There are
        13 weights (Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace)
    and
        4 suits (clubs, diamonds, hearts, spades).
    """

    def __init__(self, card=None):
        self.cards = []
        self.refresh()

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return repr(self.cards)

    @property
    def size(self):
        return len(self.cards)

    def push_cards(self, count):
        count_type = type(count)
        if not count_type is int:
            raise DeckCountTypeError(count_type)
        if count < 1 or count > len(self.cards):
            raise DeckCountNumberError(count)
        for i in range(count):
            yield self.cards.pop(random.choice(range(len(self.cards))))

    def refresh(self):
        self.cards = [Card(f'{w}{s}') for w in Card.Weight.REAL_SYMBOLS for s in Card.Suit.SYMBOLS]


class Cards:
    """
    Several cards.

    Cards could be set by cards string or by some iterable of Card instanses
    Cards set of (Three of diamonds, Ten of clubs and Ace of spades) looks like
        Cards('3d/Tc/As') or Cards([Card('3d'), Card('Tc'), Card('As')])

    Also cards could be set from deck after initialization
    """

    def __init__(self, cards_string=None, cards=None, max_count=52):
        self.max_count = max_count
        if cards_string:
            cards_string_type = type(cards_string)
            if not cards_string_type is str:
                raise CardsStringTypeError(cards_string_type)
            self.items = [Card(sign) for sign in cards_string.split('/')[:max_count]]
        elif cards:
            items = list(set(cards))[:max_count]
            for card in items:
                card_type = type(card)
                if not card_type is Card:
                    raise CardsCardTypeError(card_type)
            self.items = items
        else:
            self.items = []

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return repr(self.items)

    def __contains__(self, item):
        return item in self.items

    @property
    def size(self):
        return len(self.items)

    def pull(self, deck, count):
        max_to_add = self.max_count - self.size
        count_to_add = max_to_add if count > max_to_add else count
        if count_to_add > 0:
            self.items.extend(deck.push_cards(count_to_add))

    def clean(self):
        self.items = []
