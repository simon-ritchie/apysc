import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestMultiLineText:
    @apply_test_settings(retrying_max_attempts_num=0)
    def test__initialize_with_base_value(self) -> None:
        text: ap.MultiLineText = ap.MultiLineText._initialize_with_base_value()
        assert text._text._value == "<span></span>"

    @apply_test_settings(retrying_max_attempts_num=0)
    def test___init__(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        text: ap.MultiLineText = ap.MultiLineText(
            text="test text",
            width=100,
            parent=sprite,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(text._text, ap.String)
        assert text._text._value == "<span>test text</span>"
        assert "test_suffix" in text._text.variable_name
        assert text.parent == sprite
