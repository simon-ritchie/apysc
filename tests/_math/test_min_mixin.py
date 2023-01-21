from random import randint
from typing import Union

from retrying import retry

import apysc as ap
from apysc._math import min_mixin


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__all_values_are_int() -> None:
    result: bool = min_mixin._all_values_are_int(
        values=ap.Array([10, ap.Int(20), 30])
    )
    assert result

    result = min_mixin._all_values_are_int(
        values=ap.Array([10, ap.Int(20), 10.5, 30])
    )
    assert not result

    result = min_mixin._all_values_are_int(
        values=ap.Array([10, ap.Int(20), 10.5, 30])
    )
    assert not result

    result = min_mixin._all_values_are_int(
        values=ap.Array([10, ap.Number(20.5), 10.5, 30])
    )
    assert not result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_min_int_value() -> None:
    min_value: int = min_mixin._get_min_int_value(
        values=ap.Array([10, 10.5, ap.Int(9), ap.Number(8.5)])
    )
    assert min_value == 8


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_min_float_value() -> None:
    min_value: float = min_mixin._get_min_float_value(
        values=ap.Array([10, 10.5, ap.Int(9), ap.Number(8.5)])
    )
    assert min_value == 8.5
