from random import randint

from retrying import retry

from apysc._type import _delete
import apysc as ap
from apysc._expression import expression_data_util


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__append_delete_expression() -> None:
    expression_data_util.empty_expression()

    value: ap.Int = ap.Int(10)
    _delete._append_delete_expression(value=value)
    expression: str = expression_data_util.get_current_expression()
    expected: str = (
        f'delete {value.variable_name};'
        f'\n{value.variable_name} = undefined;'
    )
    assert expected in expression
