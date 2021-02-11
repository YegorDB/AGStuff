# Abstract games stuff


## Install
`pip install AGStuff`


## Requirements
- python>=3.6


## Usage

### Cards

```python
>>> from agstuff.cards.core import Card, Cards, Deck
>>>
>>> card1 = Card('As')
>>> print(card1)
A♠
>>> card2 = Card('8d')
>>> print(card2)
8♦
>>> card1 > card2
True
>>>
>>> cards = Cards('As/Ks/Qs')
>>> cards
[A♠, K♠, Q♠]
>>> card1 in cards
True
>>>
>>> cards = Cards(cards=(card2, Card('Tc'), Card('4h')))
>>> cards
[8♦, 4♥, T♣]
>>> card2 in cards
True
>>>
>>> deck = Deck()
>>> cards = Cards()
>>> cards.pull(deck, 5)
>>> cards
[9♥, 2♦, 8♣, 6♠, K♥]
```
