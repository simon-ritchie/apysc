from random import randint

from retrying import retry

import apysc as ap
from apysc._type import type_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_same_class_instance() -> None:
    result: bool = type_util.is_same_class_instance(class_=bool, instance=1)
    assert not result

    result = type_util.is_same_class_instance(class_=int, instance=1)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_float_or_number() -> None:
    result: bool = type_util.is_float_or_number(value=100.5)
    assert result

    result = type_util.is_float_or_number(value=ap.Number(value=10.5))
    assert result

    result = type_util.is_float_or_number(value=100)
    assert not result

    result = type_util.is_float_or_number(value=ap.Int(value=10))
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_number() -> None:
    result: bool = type_util.is_number(value=ap.Number(value=10.5))
    assert result

    result = type_util.is_number(value=10.5)
    assert not result

    result = type_util.is_number(value=ap.Int(value=10))
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_bool() -> None:
    result: bool = type_util.is_bool(value=True)
    assert result
    result = type_util.is_bool(value=False)
    assert result
    result = type_util.is_bool(value=ap.Boolean(True))
    assert result
    result = type_util.is_bool(value=1)
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_is_immutable_type() -> None:
    result: bool = type_util.is_immutable_type(value=10)
    assert result

    result = type_util.is_immutable_type(value=ap.Int(10))
    assert result

    result = type_util.is_immutable_type(value=[10])
    assert not result
