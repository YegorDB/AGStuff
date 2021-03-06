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


from functools import wraps


class CardSymbolValidator:
    def __init__(self, symbols, exception):
        self._symbols = symbols
        self._exception = exception

    def __call__(self, init_function):
        @wraps(init_function)
        def wrap(init_self, symbol):
            symbol = str(symbol)
            if not symbol in set(self._symbols):
                raise self._exception(symbol)
            init_function(init_self, symbol)
        return wrap
