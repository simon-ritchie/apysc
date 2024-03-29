import apysc as ap
from apysc._display import rotation_interface_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.expression_string import ExpressionString


@apply_test_settings()
def test_get_coordinates_key_for_expression() -> None:
    key_exp_str: ExpressionString = (
        rotation_interface_helper.get_coordinates_key_for_expression(x=100, y=200)
    )
    assert key_exp_str.value == 'String(100.000) + "_" + String(200.000)'

    x: ap.Number = ap.Number(100)
    y: ap.Number = ap.Number(200)
    key_exp_str = rotation_interface_helper.get_coordinates_key_for_expression(x=x, y=y)
    assert key_exp_str.value == (
        f'String({x.variable_name}) + "_" + String({y.variable_name})'
    )
