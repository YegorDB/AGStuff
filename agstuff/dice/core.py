# Copyright 2019 Yegor Bitensky

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


class Dice:
    def __init__(self, faces_count=None, faces_items=None):
        if faces_count:
            self.items = list(range(1, faces_count + 1))
        elif faces_items:
            self.items = list(faces_items)
        else:
            raise ValueError

    def rolling(self):
        return random.choice(self.items)


class DiceBox:
    def __init__(self, dice_instanses=None, count=None, faces_count=None, faces_items=None):
        if dice_instanses:
            self.items = list(dice_instanses)
        elif count:
            self.items = [Dice(faces_count=faces_count, faces_items=faces_items) for i in range(count)]
        else:
            raise ValueError

    def rolling(self):
        return [dice.rolling() for dice in self.items]
