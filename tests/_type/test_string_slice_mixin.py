import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestStringSliceMixIn:
    @apply_test_settings()
    def test_slice(self) -> None:
        string: ap.String = ap.String("012345")
        result_string: ap.String = string.slice(
            start=0, variable_name_suffix="test_suffix"
        )
        assert result_string._value == "012345"
        assert result_string._variable_name_suffix == "test_suffix"
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result_string.variable_name} = " f"{string.variable_name}.slice("
        )
        assert expected in expression

        result_string = string.slice(start=ap.Int(0))
        assert result_string._value == "012345"

        result_string = string.slice(start=1)
        assert result_string._value == "12345"

        result_string = string.slice(start=ap.Int(1))
        assert result_string._value == "12345"

        result_string = string.slice(start=0, end=2)
        assert result_string._value == "01"

        result_string = string.slice(start=ap.Int(0), end=ap.Int(2))
        assert result_string._value == "01"

        result_string = string.slice(start=2, end=4)
        assert result_string._value == "23"

        result_string = string.slice(start=ap.Int(2), end=ap.Int(4))
        assert result_string._value == "23"

        result_string = string.slice(start=-2)
        assert result_string._value == "45"

        result_string = string.slice(start=ap.Int(-2))
        assert result_string._value == "45"

        result_string = string.slice(start=-3, end=-1)
        assert result_string._value == "34"

        result_string = string.slice(start=ap.Int(-3), end=ap.Int(-1))
        assert result_string._value == "34"
