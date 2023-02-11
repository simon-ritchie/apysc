import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import expression_data_util
from apysc._display.svg_text import SVGText
from apysc._expression import var_names


class TestSVGText:
    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text",
            variable_name_suffix="test_suffix",
        )
        assert var_names.SVG_TEXT in svg_text.variable_name
        assert svg_text._variable_name_suffix == "test_suffix"

    @apply_test_settings()
    def test__set_text_value(self) -> None:
        ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text 1",
            variable_name_suffix="test_suffix",
        )
        assert svg_text.text == ap.String("test text 1")
        assert svg_text._text == "test text 1"

        text_: ap.String = svg_text._set_text_value(text="test text 2")
        assert text_ == ap.String("test text 2")
        assert svg_text.text == ap.String("test text 2")
