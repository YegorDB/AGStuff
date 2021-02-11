# Cards


## Core


### Card(sign)

Some card from standard 52 cards deck.

```python
>>> from agstuff.cards.core import Card

>>> card = Card('As')
>>> card
A♠
>>> card.name
'Ace of spades'
```

#### Card sign
Whether two symbols (1st symbol is card weight, 2nd symbol is card suit) or single one (weight or suit).

> Sign symbols are ignored since 3rd one.

##### Card weight symbols
- Deuce - `'2'`
- Three - `'3'`
- Four - `'4'`
- Five - `'5'`
- Six - `'6'`
- Seven - `'7'`
- Eight - `'8'`
- Nine - `'9'`
- Ten - `'T'`
- Jack - `'J'`
- Queen - `'Q'`
- King - `'K'`
- Ace - `'A'`

##### Card suit symbols
- Сlubs - `'c'`
- Diamonds - `'d'`
- Hearts - `'h'`
- Spades - `'s'`

#### Card comparison

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

#### Card weights/suits directly comparison

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

#### Abstract cards

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

### Deck()

Standard 52 cards deck.

```python
>>> from agstuff.cards.core import Deck

>>> deck = Deck()
>>> deck
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
>>> list(cards)
[6♦, 4♣, J♠]
>>> deck.size
49
>>> deck.refresh()
>>> deck.size
52
```

### Cards(cards_string=None, cards=None, max_count=52)

Several cards.

#### Cards creation by cards string

```python
>>> from agstuff.cards.core import Cards

>>> cards = Cards("2c/3c/4c/5c/6c")
>>> cards
[2♣, 3♣, 4♣, 5♣, 6♣]
```

#### Cards creation by iterable of Card instanses

```python
>>> from agstuff.cards.core import Card, Cards

>>> cards = Cards(cards=[Card("Jd"), Card("2s"), Card("6c")])
>>> cards
[2♠, 6♣, J♦]
```

#### Cards fill from deck

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
>>> cards
[4♣, 5♠, 7♦]

>>> cards.pull(deck, 2) # add 2 more cards
>>> cards.size
5
>>> cards
[4♣, 5♠, 7♦, 9♥, J♠]

>>> cards.clean()
>>> cards.size
0
>>> cards
[]
```

#### Cards inclusion

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

#### Cards items max count

> By default Cards items max count is 52

```python
>>> from agstuff.cards.core import Deck, Cards

>>> cards1 = Cards(max_count=7)
>>> deck = Deck()
>>> cards1.pull(deck, 10)
>>> cards1
[5♣, 3♥, Q♠, J♣, J♦, 8♠, 9♣]

>>> cards2 = Cards("2s/3s/4s/5s/6s/7s/8s/9s/Ts/Js/Qs/Ks/As", max_count=5)
>>> cards2
[2♠, 3♠, 4♠, 5♠, 6♠]
```
