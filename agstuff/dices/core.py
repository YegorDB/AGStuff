# Copyright 2019-2021 Yegor Bitensky

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

from collections.abc import Iterable

from agstuff.exceptions.dices.core import (
    DiceEmptyInialItemsError,
    DiceWrongFacesCountTypeError, DiceWrongFacesCountError,
    DiceWrongFacesItemsTypeError, DiceWrongFacesItemsCountError,
    DiceBoxWrongItemAdditionError,
)


class Dice:
    """
    Customizable dice.

    Could be created by faces count or faces items.

    Faces count is an integer greater or equal MIN_FACES_COUNT.
    If dice is created by faces count its faces will be integers from 1 to faces count number.
    ```python
    >>> dice = Dice(faces_count=6)
    >>> print(dice.items)
    [1, 2, 3, 4, 5, 6]
    ```

    Faces items is an iterable contains comparable and addible to each other objects.
    ```python
    >>> dice = Dice(faces_items='QWERTY')
    >>> print(dice.items)
    ['Q', 'W', 'E', 'R', 'T', 'Y']
    ```
    """

    MIN_FACES_COUNT = 2

    def __init__(self, faces_count=None, faces_items=None):
        if faces_count:
            if not isinstance(faces_count, int):
                raise DiceWrongFacesCountTypeError()
            if faces_count < self.MIN_FACES_COUNT:
                raise DiceWrongFacesCountError(self.MIN_FACES_COUNT)
            self.items = list(range(1, faces_count + 1))
        elif faces_items:
            if not isinstance(faces_items, Iterable):
                raise DiceWrongFacesItemsTypeError()
            faces_items = list(faces_items)
            if len(faces_items) < self.MIN_FACES_COUNT:
                raise DiceWrongFacesItemsCountError(self.MIN_FACES_COUNT)
            self.items = faces_items
        else:
            raise DiceEmptyInialItemsError()

        self._value = None
        self.rolling()

    def __str__(self):
        return f'{self._value} of {self.items}'

    def __repr__(self):
        return f'{self._value} of {self.items}'

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __add__(self, other):
        if not other:
            return self.value
        elif isinstance(other, Dice):
            return self.value + other.value
        return self.value + other

    @property
    def value(self):
        return self._value

    def rolling(self):
        self._value = random.choice(self.items)
        return self._value


class DiceBox:
    """
    Multiple dices handler.
    """

    def __init__(self):
        self.items = []

    def add(self, dice):
        if not isinstance(dice, Dice):
            raise DiceBoxWrongItemAdditionError()
        self.items.append(dice)

    def rolling(self):
        result = None
        for dice in self.items:
            dice.rolling()
            result = dice + result
        return result
