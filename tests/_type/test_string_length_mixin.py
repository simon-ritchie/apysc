import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestStringLengthMixIn:
    @apply_test_settings()
    def test_length(self) -> None:
        expression_data_util.empty_expression()
        string: ap.String = ap.String('abc')
        length: ap.Int = string.length(variable_name_suffix="test_suffix")
        assert "test_suffix" in length.variable_name
        assert length == ap.Int(3)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{length.variable_name} = [...{string.variable_name}];"
        )
        assert expected in expression
