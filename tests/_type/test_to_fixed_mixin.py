import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestToFixedMixIn:
    @apply_test_settings()
    def test_to_fixed(self) -> None:
        expression_data_util.empty_expression()
        num: ap.Number = ap.Number(10.789789)
        result_str: ap.String = num.to_fixed(digits=2)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result_str.variable_name} = {num.variable_name}.toFixed("
        )
        assert expected in expression
        assert result_str == ap.String("10.79")

        expression_data_util.empty_expression()
        int_val: ap.Int = ap.Int(10)
        digits: ap.Int = ap.Int(3)
        result_str = int_val.to_fixed(digits=digits)
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{result_str.variable_name} = {int_val.variable_name}"
            f".toFixed({digits.variable_name});"
        )
        assert expected in expression
        assert result_str == ap.String("10.000")
