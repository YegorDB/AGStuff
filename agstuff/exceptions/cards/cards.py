# Copyright 2018-2019 Yegor Bitensky

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class CardsStringTypeError(Exception):
    def __init__(self, cards_string_type):
        super().__init__(
            f"Type of 'cards_string' argument need to be 'str' not '{cards_string_type}'."
        )


class CardsCardTypeError(Exception):
    def __init__(self, card_type):
        super().__init__(f"Type of card in 'cards' argument can not be '{card_type}'.")
