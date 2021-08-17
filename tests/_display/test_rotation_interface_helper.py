from random import randint

from retrying import retry

import apysc as ap
from apysc._display import rotation_interface_helper
from apysc._type.expression_string import ExpressionString


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_coordinates_key_for_expression() -> None:
    key_exp_str: ExpressionString = rotation_interface_helper.\
        get_coordinates_key_for_expression(x=100, y=200)
    assert key_exp_str.value == 'String(100) + "_" + String(200)'

    x: ap.Int = ap.Int(100)
    y: ap.Int = ap.Int(200)
    key_exp_str = rotation_interface_helper.\
        get_coordinates_key_for_expression(x=x, y=y)
    assert key_exp_str.value == (
        f'String({x.variable_name}) + "_" + String({y.variable_name})'
    )
