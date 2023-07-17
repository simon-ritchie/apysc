import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.to_string_mixin import ToStringMixIn


class TestToStringMixIn:
    @apply_test_settings()
    def test_to_string(self) -> None:
        mixin: ToStringMixIn = ToStringMixIn()
        mixin.variable_name = "test_mixin"
        string: ap.String = mixin.to_string()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{string.variable_name} = String({mixin.variable_name});"
        assert expected in expression
