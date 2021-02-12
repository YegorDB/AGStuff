# Dices


## Dice(faces_count=None, faces_items=None)

> Customizable dice.

### Dice creation by faces count

> Faces count is an integer greater or equal than 2.

```python
>>> from agstuff.dices.core import Dice
>>>
>>> dice = Dice(faces_count=6)
>>> print(dice.items)
[1, 2, 3, 4, 5, 6]
```

### Dice creation by faces items

> Faces items is an iterable contains comparable and addible to each other objects.

```python
>>> from agstuff.dices.core import Dice
>>>
>>> dice = Dice(faces_items='QWERTY')
>>> print(dice.items)
['Q', 'W', 'E', 'R', 'T', 'Y']
```

### Dice rolling

```python
>>> from agstuff.dices.core import Dice
>>> 
>>> dice = Dice(6)
>>> dice.value
1
>>> dice.rolling()
4
>>> dice.value
4
>>> dice
4 of [1, 2, 3, 4, 5, 6]
```

### Dices interaction

```python
>>> from agstuff.dices.core import Dice
>>> 
>>> dice1 = Dice(10)
>>> dice1.value
2
>>> dice2 = Dice(4)
>>> dice2.value
3
>>> dice1 > dice2
False
>>> dice1 + dice2
5
```


## DiceBox()

> Multiple dices handler.

### DiceBox rolling

```python
>>> from agstuff.dices.core import Dice, DiceBox
>>>
>>> dice_box = DiceBox()
>>> dice1 = Dice(8)
>>> dice_box.add(dice1)
>>> dice2 = Dice(4)
>>> dice_box.add(dice2)
>>> dice_box.rolling()
6
>>> dice1.value
2
>>> dice2.value
4
```
