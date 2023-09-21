import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestStringLowerMixIn:
    @apply_test_settings()
    def test_lower(self) -> None:
        string: ap.String = ap.String(value='AbC1_')
        result_string: ap.String = string.lower()
        assert result_string._value == 'abc1_'
        assert result_string.variable_name != string.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result_string.variable_name} = {string.variable_name}.toLowerCase();"
        )
        assert expected in expression
