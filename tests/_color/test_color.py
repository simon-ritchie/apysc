import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


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
