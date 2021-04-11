from typing import Any
from typing import Dict

from apysc import Boolean
from apysc.callable import callable_util


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


def test_get_arg_name_at() -> None:

    def _test_func(a: int, b: int) -> None:
        ...

    arg_name: str = callable_util.get_arg_name_at(func=_test_func, index=0)
    assert arg_name == 'a'

    arg_name = callable_util.get_arg_name_at(func=_test_func, index=1)
    assert arg_name == 'b'


def test_get_name_and_arg_value_dict_from_args() -> None:

    def _test_func(a: int, b: str, c: int) -> None:
        ...

    name_and_arg_value_dict: Dict[str, Any] = callable_util.\
        get_name_and_arg_value_dict_from_args(
            func=_test_func,
            args=[100, 'Hello!'],
            kwargs={'c': 200})
    expected: Dict[str, Any] = {
        'a': 100,
        'b': 'Hello!',
        'c': 200,
    }
    assert name_and_arg_value_dict == expected


def test_get_method_class_name() -> None:
    class_name: str = callable_util.get_method_class_name(
        method=print)
    assert class_name == ''

    bool_1: Boolean = Boolean(True)
    class_name = callable_util.get_method_class_name(
        method=bool_1._get_bool_from_arg_value)
    assert class_name == 'Boolean'

    class_name = callable_util.get_method_class_name(
        method=bool_1._append_ne_expression)
    assert class_name == 'Boolean'
