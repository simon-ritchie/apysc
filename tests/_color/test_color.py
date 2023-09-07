import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestColor:
    @apply_test_settings()
    def test___init__(self) -> None:
        color: ap.Color = ap.Color(
            "#0af",
            variable_name_suffix="test_color",
        )
        assert color._value == "#00aaff"
        assert isinstance(color._value, ap.String)
        assert "test_color" in color._value.variable_name

        color = ap.Color(ap.String("#00aaff"))
        assert color._value == ap.String("#00aaff")

    @apply_test_settings()
    def test___eq__(self) -> None:
        color_1: ap.Color = ap.Color("#0af")
        color_2: ap.Color = ap.Color("#00aaff")
        color_3: ap.Color = ap.Color("#f0a")
        result: ap.Boolean = color_1 == color_2
        assert result
        assert isinstance(result, ap.Boolean)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = {color_1._value.variable_name} "
            f"=== {color_2._value.variable_name};"
        )
        assert expected in expression

        result = color_1 == color_3
        assert not result
        assert isinstance(result, ap.Boolean)

        result = color_1 == 100  # type: ignore
        assert not result

        assert_raises(
            expected_error_class=TypeError,
            callable_=color_1.__eq__,
            other="#00aaff",
            match="The comparison between the `Color` class and `str`",
        )
        assert_raises(
            expected_error_class=TypeError,
            callable_=color_1.__eq__,
            other=ap.String("#00aaff"),
            match="The comparison between the `Color` class and `String`",
        )

    @apply_test_settings()
    def test___repr__(self) -> None:
        color: ap.Color = ap.Color("#0af")
        repr_str: str = repr(color)
        assert repr_str == 'Color("#00aaff")'

        delattr(color, "_value")
        repr_str = repr(color)
        assert repr_str == 'Color("")'

    @apply_test_settings()
    def test_variable_name(self) -> None:
        color: ap.Color = ap.Color("#0af")
        assert color.variable_name == color._value.variable_name

        color = ap.Color("#0af", variable_name_suffix="test_suffix")
        assert color.variable_name == color._value.variable_name
