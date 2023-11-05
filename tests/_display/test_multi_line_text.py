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
            x=100,
            y=200,
            width=100,
            fill_color=ap.Color("#333333"),
            fill_alpha=0.5,
            bold=True,
            italic=True,
            text_align=ap.CssTextAlign.CENTER,
            text_align_last=ap.CssTextAlignLast.RIGHT,
            parent=sprite,
            variable_name_suffix="test_suffix",
        )
        assert isinstance(text._text, ap.String)
        assert text._text._value == "<span>test text</span>"
        assert text.x._value == 100
        assert text.y._value == 200
        assert text._width._value == 100
        assert text._fill_color == ap.Color("#333333")
        assert text._fill_alpha._value == 0.5
        assert text._bold == ap.True_
        assert text.parent == sprite
        assert "test_suffix" in text._text.variable_name
