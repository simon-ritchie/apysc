from random import randint

from retrying import retry

from apysc._expression import expression_data_util
from apysc._event.stop_propagation_interface import StopPropagationInterface


class TestStopPropagationInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stop_propagation(self) -> None:
        expression_data_util.empty_expression()
        interface: StopPropagationInterface = StopPropagationInterface()
        interface.variable_name = 'test_stop_propagation_interface'
        interface.stop_propagation()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.stopPropagation();'
        )
        assert expected in expression
