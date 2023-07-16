import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestToNumberMixIn:
    @apply_test_settings()
    def test_to_number(self) -> None:
        ap.Stage()
        int_val: ap.Int = ap.Int(5)
        number: ap.Number = int_val.to_number(variable_name_suffix="test_suffix")
        assert number == ap.Number(5)
        assert "test_suffix" in number.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{number.variable_name} = Number({int_val.variable_name});"
        assert expected in expression
