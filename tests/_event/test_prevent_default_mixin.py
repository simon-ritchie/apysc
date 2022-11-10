from random import randint

from retrying import retry

from apysc._event.prevent_default_mixin import PreventDefaultMixIn
from apysc._expression import expression_data_util


class TestPreventDefaultMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_prevent_default(self) -> None:
        expression_data_util.empty_expression()
        mixin: PreventDefaultMixIn = PreventDefaultMixIn()
        mixin.variable_name = "test_prevent_default_mixin"
        mixin.prevent_default()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.preventDefault();"
        assert expected in expression
