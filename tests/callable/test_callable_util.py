from typing import Any, Dict
from apyscript.callable import callable_util


def test_get_func_default_vals() -> None:

    def _test_func(a: int, b: int = 100, c: str = 'Hello!') -> None:
        ...

    default_vals: Dict[str, Any] = callable_util.get_func_default_vals(
        func=_test_func)
    expected: Dict[str, Any] = {
        'a': callable_util.empty,
        'b': 100,
        'c': 'Hello!',
    }
    assert default_vals == expected
