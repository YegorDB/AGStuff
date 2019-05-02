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


class DeckCountTypeError(Exception):
    def __init__(self, count_type):
        super().__init__(f"Type of count cards to push need to be 'int' not '{count_type}'.")


class DeckCountNumberError(Exception):
    def __init__(self, count_number):
        super().__init__(f"{count_number} is out of current deck cards count.")
