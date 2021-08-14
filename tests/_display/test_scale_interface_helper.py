from random import randint

from retrying import retry

import apysc as ap
from apysc._display import scale_interface_helper
from apysc._type.expression_string import ExpressionString


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_point_key_for_expression() -> None:
    key_exp_str: ExpressionString = scale_interface_helper.\
        get_point_key_for_expression(x=10, y=20)
    assert key_exp_str.value == 'String(10) + "_" + String(20)'

    x: ap.Int = ap.Int(10)
    y: ap.Int = ap.Int(20)
    key_exp_str = scale_interface_helper.get_point_key_for_expression(
        x=x, y=y)
    expected: str = (
        f'String({x.variable_name}) + "_" + String({y.variable_name})')
    assert key_exp_str.value == expected
