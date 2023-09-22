import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestStringUpperMixIn:
    @apply_test_settings()
    def test_upper(self) -> None:
        string: ap.String = ap.String(value='aBc1_')
        result_string: ap.String = string.upper()
        assert result_string._value == 'ABC1_'
        assert result_string.variable_name != string.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result_string.variable_name} = {string.variable_name}.toUpperCase();"
        )
        assert expected in expression
