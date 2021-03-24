import inspect
from typing import Any
from typing import List
from typing import Tuple

from apysc.expression import var_names


def test_const_values_not_duplicated() -> None:
    members: List[Tuple[str, Any]] = inspect.getmembers(var_names)
    constants: List[str] = []
    for member_name, member_val in members:
        if not isinstance(member_val, str):
            continue
        if not member_name.isupper():
            continue
        constants.append(member_val)

    original_len: int = len(constants)
    unique_len: int = len(set(constants))
    assert original_len == unique_len
