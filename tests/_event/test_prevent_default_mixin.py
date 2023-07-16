from apysc._event.prevent_default_mixin import PreventDefaultMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


class TestPreventDefaultMixIn:
    @apply_test_settings()
    def test_prevent_default(self) -> None:
        ap.Stage()
        mixin: PreventDefaultMixIn = PreventDefaultMixIn()
        mixin.variable_name = "test_prevent_default_mixin"
        mixin.prevent_default()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.preventDefault();"
        assert expected in expression
