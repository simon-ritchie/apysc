from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._math import max_mixin
from apysc._math.max_mixin import MaxMixIn


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_max_float_value() -> None:
    max_value: float = max_mixin._get_max_float_value(
        values=ap.Array([10, 10.5, ap.Int(11), ap.Number(10.9)]),
    )
    assert max_value == 11.0
