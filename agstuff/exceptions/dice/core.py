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


class DiceEmptyInialItemsError(Exception):
    def __init__(self):
        super().__init__(
            "To dice creation "
            "whether \"faces_count\" or \"faces_items\" "
            "argsuments need to be passed."
        )


class DiceWrongFacesCountTypeError(Exception):
    def __init__(self):
        super().__init__("Dice \"faces_count\" argsument type need to be \"int\".")


class DiceWrongFacesCountError(Exception):
    def __init__(self, min_count):
        super().__init__(f"Dice \"faces_count\" argsument need to be greater or equal to {min_count}.")


class DiceWrongFacesItemsTypeError(Exception):
    def __init__(self):
        super().__init__("Dice \"faces_items\" argsument need to be iterable.")


class DiceWrongFacesItemsCountError(Exception):
    def __init__(self, min_count):
        super().__init__(f"Dice \"faces_items\" count need to be greater or equal to {min_count}.")


class DiceBoxWrongItemAdditionError(Exception):
    def __init__(self):
        super().__init__("Dice instance expected.")
