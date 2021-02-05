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


import pytest

from agstuff.cards.core import Card, Deck, Cards
from agstuff.exceptions.cards import (
    CardWeightSymbolError, CardSuitSymbolError,
    DeckCountTypeError, DeckCountNumberError,
    CardsStringTypeError, CardsCardTypeError
)


def get_parameters(func):
    def wrap(self, values):
        return func(self, **values)
    return wrap


class TestCard:
    def test_validation(self):
        with pytest.raises(CardWeightSymbolError):
            Card("Xd")
        with pytest.raises(CardSuitSymbolError):
            Card("Ty")
        with pytest.raises(CardSuitSymbolError):
            Card("0")
        with pytest.raises(CardSuitSymbolError):
            Card("")

    def test_name(self):
        assert Card("Td").name == "Ten of diamonds"
        assert Card("2h").name == "Two of hearts"
        assert Card("A").name == "Ace"
        assert Card("7").name == "Seven"
        assert Card("c").name == "clubs"
        assert Card("s").name == "spades"

    def test_comparative(self):
        assert Card("Ks") == Card("Kc")
        assert Card("6d") != Card("Ts")
        assert Card("8h") == Card("8")
        assert Card("4") != Card("Q")
        assert Card("Jd") > Card("5s")
        assert Card("3h") < Card("7c")
        assert Card("2") < Card("A")
        assert Card("9") > Card("3")
        assert Card("Ac") == Card("c")
        assert Card("5d") != Card("s")

    def test_hash(self):
        assert hash(Card("Kd")) == 132
        assert hash(Card("T")) == 100
        assert hash(Card("s")) == 4


class TestDeck:
    def test_validation(self):
        with pytest.raises(DeckCountTypeError):
            list(Deck().push_cards("3"))
        with pytest.raises(DeckCountNumberError):
            list(Deck().push_cards(53))

    def test_count(self):
        deck = Deck()
        assert deck.size == 52
        assert len(list(deck.push_cards(2))) == 2
        assert deck.size == 50


class TestCards:
    def test_validation(self):
        with pytest.raises(CardsStringTypeError):
            Cards(123)

    def test_items(self):
        assert Cards().items == []
        assert Cards("As/Ac/Ah/Ad").items == [Card("As"), Card("Ac"), Card("Ah"), Card("Ad")]

    def test_contains(self):
        assert Card("Ks") in Cards("As/Ks/Qs/Js/Ts")
        assert not Card("8h") in Cards("As/Ks/Qs/Js/Ts")

    def test_pull(self):
        deck = Deck()
        cards = Cards(max_count=7)
        assert cards.size == 0
        assert deck.size == 52
        cards.pull(deck, 3)
        assert cards.size == 3
        assert deck.size == 49
        cards.pull(deck, 2)
        assert cards.size == 5
        assert deck.size == 47
        cards.pull(deck, 10) # can add only 2 cards (Cards item limit is 7)
        assert cards.size == 7
        assert deck.size == 45
        cards.pull(deck, 5) # can't add cards (item limit has been reached)
        assert cards.size == 7
        assert deck.size == 45
