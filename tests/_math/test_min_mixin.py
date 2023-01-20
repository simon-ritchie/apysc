from random import randint

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
