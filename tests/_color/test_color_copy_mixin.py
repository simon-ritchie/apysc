from copy import deepcopy

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestColorCopyMixIn:
    @apply_test_settings()
    def test__get_copy_expression(self) -> None:
        color: ap.Color = ap.Color("#333333")
        copied_color: ap.Color = deepcopy(color)
        expression: str = color._get_copy_expression(result=copied_color)
        assert expression == (
            f"var {copied_color._value.variable_name} = {color._value.variable_name};"
        )

    _handler_expected_expression: str

    def _test_handler_1(self, e: ap.TimerEvent, options: dict) -> None:
        color: ap.Color = ap.Color("#333333")
        copied_color: ap.Color = color._copy()
        self._handler_expected_expression = color._get_copy_expression(
            result=copied_color
        )

    @apply_test_settings(retrying_max_attempts_num=0)
    def test__copy(self) -> None:
        color: ap.Color = ap.Color("#333333")
        copied_color: ap.Color = color._copy()
        assert copied_color._value == "#333333"
        assert copied_color._value.variable_name != color._value.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = color._get_copy_expression(result=copied_color)
        assert expected in expression

        ap.Stage()
        ap.Timer(handler=self._test_handler_1, delay=1000, repeat_count=1).start()
        expression = expression_data_util.get_current_expression()
        print(expression)
        assert self._handler_expected_expression in expression
        expression = expression_data_util.get_current_event_handler_scope_expression()
        assert self._handler_expected_expression in expression
