from random import randint

from retrying import retry

from apysc._expression import expression_data_util
from apysc._event.prevent_default_interface import PreventDefaultInterface


class TestPreventDefaultInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        expression_data_util.empty_expression()
        interface: PreventDefaultInterface = PreventDefaultInterface()
        interface.variable_name = 'test_prevent_default_interface'
        interface.prevent_default()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.preventDefault();'
        )
        assert expected in expression
