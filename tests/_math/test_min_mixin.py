from random import randint
from typing import Union

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._math import min_mixin
from apysc._math.min_mixin import MinMixIn


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_min_float_value() -> None:
    min_value: float = min_mixin._get_min_float_value(
        values=ap.Array([10, 10.5, ap.Int(9), ap.Number(8.5)])
    )
    assert min_value == 8.5


class TestMinMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_min(self) -> None:
        expression_data_util.empty_expression()
        values: ap.Array = ap.Array([10, 9.5, ap.Int(9), ap.Number(9.5)])
        min_value: ap.Number = MinMixIn.min(
            values=values,
        )
        assert min_value == ap.Number(9)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{min_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.max(a, b)});"
        )
        assert expected in expression
