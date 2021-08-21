from random import randint

from retrying import retry

import apysc as ap
from apysc._display import flip_interface_helper


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_make_flip_update_expression() -> None:
    before_value: ap.Boolean = ap.Boolean(True)
    after_value: ap.Boolean = ap.Boolean(False)
    expression: str = flip_interface_helper.make_flip_update_expression(
        before_value=before_value, after_value=after_value,
        axis=flip_interface_helper.Axis.Y,
        interface_variable_name='test_interface')
    expected: str = (
        f'if ({before_value.variable_name}) {{'
        '\n  test_interface.flip("y");'
        '\n}'
        f'\nif ({after_value.variable_name}) {{'
        f'\n  test_interface.flip("y");'
        '\n}'
        f'\n{before_value.variable_name} = {after_value.variable_name};'
    )
    assert expression == expected
