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

from agstuff.exceptions.dice.core import (
    DiceEmptyInialItemsError,
    DiceWrongFacesCountTypeError, DiceWrongFacesCountError,
    DiceWrongFacesItemsTypeError, DiceWrongFacesItemsCountError,
    DiceBoxWrongItemAdditionError,
)


class Dice:
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

    def rolling(self):
        return random.choice(self.items)


class DiceBox:
    def __init__(self):
        self.items = []

    def add(self, dice):
        if not isinstance(dice, Dice):
            raise DiceBoxWrongItemAdditionError()
        self.items.append(dice)

    def rolling(self):
        return [dice.rolling() for dice in self.items]
