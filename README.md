# Abstract games stuff

## Install

`pip install AGStuff`

### Requirements

* Python 3.6 or higher

## Usage

### Cards

#### Core

##### Card(sign)

Some card from standard 52 cards deck.

Sign consisting of two symbols (1st symbol is card weight, 2nd symbol is card suit).

Weight symbols: `'2'` (Two), `'3'` (Three), `'4'` (Four), `'5'` (Five), `'6'` (Six), `'7'` (Seven), `'8'` (Eight), `'9'` (Nine), `'T'` (Ten), `'J'` (Jack), `'Q'` (Queen), `'K'` (King), `'A'` or `'1'` (Ace).

Suit symbols: `'c'` (clubs), `'d'` (diamonds), `'h'` (hearts), `'s'` (spades).

> Sign symbols are ignored since 3rd one.

```python
>>> from agstuff.cards.core import Card

>>> card = Card('As')
>>> print(card)
A♠
>>> card.name
'Ace of spades'
```

Сards can be compared

```python
>>> from agstuff.cards.core import Card

>>> card1 = Card('9h')
>>> card2 = Card('5d')
>>> card1 != card2
True
>>> card1 < card2
False
>>> card1 > card2
True
>>> card1 == card2
False

>>> card3 = Card('Qc')
>>> card4 = Card('Qs')
>>> card3 != card4
False
>>> card3 < card4
False
>>> card3 > card4
False
>>> card3 == card4
True
```

Card weights or suits can be compared directly

```python
>>> from agstuff.cards.core import Card

>>> card1 = Card('Td')
>>> card2 = Card('3d')
>>> card1.weight != card2.weight
True
>>> card1.weight < card2.weight
False
>>> card1.weight > card2.weight
True
>>> card1.weight == card2.weight
False
>>> card1.suit != card2.suit
False
>>> card1.suit == card2.suit
True

>>> card3 = Card('7h')
>>> card4 = Card('7c')
>>> card3.weight != card4.weight
False
>>> card3.weight < card4.weight
False
>>> card3.weight > card4.weight
False
>>> card3.weight == card4.weight
True
>>> card3.suit != card4.suit
True
>>> card3.suit == card4.suit
False
```

Also possible use abstract cards

```python
>>> from agstuff.cards.core import Card

>>> card1 = Card('8s')
>>> card2 = Card('K') # abstract king card
>>> card3 = Card('8') # abstract eight card
>>> card1 != card2
True
>>> card1 < card2
True
>>> card1 > card2
False
>>> card1 == card2
False
>>> card1 != card3
False
>>> card1 < card3
False
>>> card1 > card3
False
>>> card1 == card3
True

>>> card4 = Card('4h')
>>> card5 = Card('d') # abstract diamonds card
>>> card6 = Card('h') # abstract hearts card
>>> card4 != card5
True
>>> card4 == card5
False
>>> card4 != card6
False
>>> card4 == card6
True
```

##### Deck()

Standard 52 cards deck.

There are 13 weights (Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King, Ace) and 4 suits (clubs, diamonds, hearts, spades).

```python
>>> from agstuff.cards.core import Deck

>>> deck = Deck()
>>> print(deck)
[
    2♣, 2♦, 2♥, 2♠,
    3♣, 3♦, 3♥, 3♠,
    4♣, 4♦, 4♥, 4♠,
    5♣, 5♦, 5♥, 5♠,
    6♣, 6♦, 6♥, 6♠,
    7♣, 7♦, 7♥, 7♠,
    8♣, 8♦, 8♥, 8♠,
    9♣, 9♦, 9♥, 9♠,
    T♣, T♦, T♥, T♠,
    J♣, J♦, J♥, J♠,
    Q♣, Q♦, Q♥, Q♠,
    K♣, K♦, K♥, K♠,
    A♣, A♦, A♥, A♠
]
>>> deck.size
52
>>> cards = deck.push_cards(3)
>>> cards # generator of 3 random cards
<generator object Deck.push_cards at 0x7f5b1d52e228>
>>> print(list(cards))
[6♦, 4♣, J♠]
>>> deck.size
49
>>> deck.refresh()
>>> deck.size
52
```

##### Cards(cards_string=None, cards=None, max_count=52)

Several cards.

Cards could be set from deck

```python
>>> from agstuff.cards.core import Deck, Cards

>>> cards = Cards()
>>> cards.size
0
>>> cards
[]

>>> deck = Deck()
>>> deck.size
52
>>> cards.pull(deck, 3) # pull 3 random cards
>>> deck.size
49
>>> cards.size
3
>>> print(cards)
[4♣, 5♠, 7♦]

>>> cards.pull(deck, 2) # add 2 more cards
>>> cards.size
5
>>> print(cards)
[4♣, 5♠, 7♦, 9♥, J♠]

>>> cards.clean()
>>> cards.size
0
>>> cards
[]
```

Also cards could be set by cards string

```python
>>> from agstuff.cards.core import Cards

>>> cards = Cards("2c/3c/4c/5c/6c")
>>> print(cards)
[2♣, 3♣, 4♣, 5♣, 6♣]
```

Also cards could be set by iterable of Card instanses

```python
>>> from agstuff.cards.core import Card, Cards

>>> cards = Cards(cards=[Card("Jd"), Card("2s"), Card("6c")])
>>> print(cards)
[2♠, 6♣, J♦]
```

There is a possibility to find out whether the cards contain a card or not

```python
>>> from agstuff.cards.core import Card, Cards

>>> card1 = Card("Qd")
>>> card2 = Card("8s")
>>> cards = Cards("Ad/Kd/Qd/Jd/Td")
>>> card1 in cards
True
>>> card2 in cards
False
```

By default Cards can contain no more than 52 items, and it could be changed

```python
>>> from agstuff.cards.core import Deck, Cards

>>> cards1 = Cards(max_count=7)
>>> deck = Deck()
>>> cards1.pull(deck, 10)
>>> print(cards1)
[5♣, 3♥, Q♠, J♣, J♦, 8♠, 9♣]

>>> cards2 = Cards("2s/3s/4s/5s/6s/7s/8s/9s/Ts/Js/Qs/Ks/As", max_count=5)
>>> print(cards2)
[2♠, 3♠, 4♠, 5♠, 6♠]
```
