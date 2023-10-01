import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestRedColorMixIn:
    @apply_test_settings()
    def test_red_color(self) -> None:
        color: ap.Color = ap.Color("#0af", variable_name_suffix="test_color")
        red_color: ap.Int = color.red_color
        assert red_color._value == 0
        assert "test_color" in red_color._variable_name_suffix
        assert "red_color" in red_color._variable_name_suffix
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{red_color.variable_name} = "
            f"parseInt({color.variable_name}.substring(1, 3), 16);"
        )
        assert expected in expression

        color = ap.Color("#ff00aa")
        red_color = color.red_color
        assert red_color._value == 255
