from random import randint

from retrying import retry

from apysc._event.stop_propagation_mixin import StopPropagationMixIn
from apysc._expression import expression_data_util


class TestStopPropagationMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stop_propagation(self) -> None:
        expression_data_util.empty_expression()
        mixin: StopPropagationMixIn = StopPropagationMixIn()
        mixin.variable_name = "test_stop_propagation_mixin"
        mixin.stop_propagation()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.stopPropagation();"
        assert expected in expression
