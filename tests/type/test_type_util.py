from apyscript.type import Int
from apyscript.type import Number
from apyscript.type import type_util


def test_is_same_class_instance() -> None:
    result: bool = type_util.is_same_class_instance(class_=bool, instance=1)
    assert not result

    result = type_util.is_same_class_instance(class_=int, instance=1)
    assert result


def test_is_float_or_number() -> None:
    result: bool = type_util.is_float_or_number(value=100.5)
    assert result

    result = type_util.is_float_or_number(value=Number(value=10.5))
    assert result

    result = type_util.is_float_or_number(value=100)
    assert not result

    result = type_util.is_float_or_number(value=Int(value=10))
    assert not result


def test_is_number() -> None:
    result: bool = type_util.is_number(value=Number(value=10.5))
    assert result

    result = type_util.is_number(value=10.5)
    assert not result

    result = type_util.is_number(value=Int(value=10))
    assert not result
