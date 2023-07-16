from apysc._event.stop_propagation_mixin import StopPropagationMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestStopPropagationMixIn:
    @apply_test_settings()
    def test_stop_propagation(self) -> None:
        ap.Stage()
        mixin: StopPropagationMixIn = StopPropagationMixIn()
        mixin.variable_name = "test_stop_propagation_mixin"
        mixin.stop_propagation()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.stopPropagation();"
        assert expected in expression
