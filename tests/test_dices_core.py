# Copyright 2021 Yegor Bitensky

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

from agstuff.dices.core import Dice, DiceBox
from agstuff.exceptions.dices.core import (
    DiceEmptyInialItemsError,
    DiceWrongFacesCountTypeError, DiceWrongFacesCountError,
    DiceWrongFacesItemsTypeError, DiceWrongFacesItemsCountError,
    DiceBoxWrongItemAdditionError,
)


class TestDice:
    def test_creation(self):
        with pytest.raises(DiceEmptyInialItemsError):
            Dice()
        with pytest.raises(DiceWrongFacesCountTypeError):
            Dice('6')
        with pytest.raises(DiceWrongFacesCountError):
            Dice(1)
        with pytest.raises(DiceWrongFacesItemsTypeError):
            Dice(faces_items=6)
        with pytest.raises(DiceWrongFacesItemsCountError):
            Dice(faces_items=[1])

    def test_interactions(self):
        dice1 = Dice(6)
        dice1._value = 5
        dice2 = Dice(6)
        dice2._value = 2
        assert dice1 > dice2
        assert not dice1 < dice2
        assert not dice1 == dice2
        assert dice1 != dice2
        assert dice1 + dice2 == 7

    def test_rolling(self):
        dice = Dice(6)
        assert dice.rolling() == dice.value


class TestDiceBox:
    def test_add(self):
        dice_box = DiceBox()
        with pytest.raises(DiceBoxWrongItemAdditionError):
            dice_box.add([i for i in range(1, 7)])
        assert len(dice_box.items) == 0
        dice_box.add(Dice(6))
        assert len(dice_box.items) == 1
        dice_box.add(Dice(6))
        assert len(dice_box.items) == 2

    def test_rolling(self):
        dice_box = DiceBox()
        dice_box.add(Dice(6))
        dice_box.add(Dice(6))
        assert dice_box.rolling() == dice_box.items[0] + dice_box.items[1]
