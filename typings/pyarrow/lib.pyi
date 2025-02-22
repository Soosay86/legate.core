# Copyright 2021-2022 NVIDIA Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any

class DataType:
    id: int
    num_fields: int
    num_buffers: int
    def equals(self, other: object) -> bool: ...
    def to_pandas_dtype(self) -> Any: ...

def binary(length: int) -> DataType: ...
def bool_() -> DataType: ...
def int8() -> DataType: ...
def int16() -> DataType: ...
def int32() -> DataType: ...
def int64() -> DataType: ...
def uint8() -> DataType: ...
def uint16() -> DataType: ...
def uint32() -> DataType: ...
def uint64() -> DataType: ...
def float16() -> DataType: ...
def float32() -> DataType: ...
def float64() -> DataType: ...
def string() -> DataType: ...
