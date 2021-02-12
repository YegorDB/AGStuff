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
>>> card1
A♠
>>> card2 = Card('8d')
>>> card2
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

### Dices

```python
>>> from agstuff.dices.core import Dice, DiceBox
>>>
>>> dice1 = Dice(faces_count=6)
>>> dice1
1 of [1, 2, 3, 4, 5, 6]
>>> dice2 = Dice(6)
>>> dice2
6 of [1, 2, 3, 4, 5, 6]
>>> dice1.rolling()
5
>>> dice1
5 of [1, 2, 3, 4, 5, 6]
>>> dice2.rolling()
1
>>> dice2
1 of [1, 2, 3, 4, 5, 6]
>>> dice1 + dice2
6
>>> dice1 > dice2
True
>>>
>>> dice3 = Dice(faces_items=('Q', 'W', 'E', 'R', 'T', 'Y'))
>>> dice3
E of ['Q', 'W', 'E', 'R', 'T', 'Y']
>>> dice3.rolling()
'Y'
>>> dice3
Y of ['Q', 'W', 'E', 'R', 'T', 'Y']
>>>
>>> dice_box = DiceBox()
>>> dice_box.add(dice1)
>>> dice_box.add(dice2)
>>> dice_box.rolling()
8
>>> dice1
5 of [1, 2, 3, 4, 5, 6]
>>> dice2
3 of [1, 2, 3, 4, 5, 6]
>>> dice1.value
5
>>> dice2.value
3
```
