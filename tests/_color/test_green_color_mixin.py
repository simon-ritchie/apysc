import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestGreenColorMixIn:
    @apply_test_settings()
    def test_green_color(self) -> None:
        color: ap.Color = ap.Color("#a0f", variable_name_suffix="test_color")
        green_color: ap.Int = color.green_color
        assert green_color._value == 0
        assert "test_color" in green_color._variable_name_suffix
        assert "green_color" in green_color._variable_name_suffix
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{green_color.variable_name} = "
            f"parseInt({color.variable_name}.substring(3, 5), 16);"
        )
        assert expected in expression

        color = ap.Color("#00ffaa")
        green_color = color.green_color
        assert green_color._value == 255
