import apysc as ap
from apysc._display.svg_text import SVGText
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from tests._display.test_graphics_expression import (
    assert_fill_opacity_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_opacity_attr_expression_exists,
)
from tests._display.test_graphics_expression import (
    assert_stroke_width_attr_expression_exists,
)


class TestSVGText:
    @apply_test_settings()
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text",
            x=50,
            y=100,
            fill_color="#0af",
            fill_alpha=0.5,
            line_color="#fff",
            line_alpha=0.3,
            line_thickness=1,
            variable_name_suffix="test_suffix",
        )
        assert var_names.SVG_TEXT in svg_text.variable_name
        assert_attrs(
            expected_attrs={
                "_x": 50,
                "_y": 100,
                "_fill_color": "#00aaff",
                "_fill_alpha": 0.5,
                "_line_color": "#ffffff",
                "_line_alpha": 0.3,
                "_line_thickness": 1,
                "_parent": stage,
            },
            any_obj=svg_text,
        )
        assert svg_text._variable_name_suffix == "test_suffix"

        expression: str = expression_data_util.get_current_expression()
        assert "text(" in expression
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_fill_opacity_attr_expression_exists(expression=expression)
        assert_stroke_opacity_attr_expression_exists(expression=expression)
        assert_stroke_width_attr_expression_exists(expression=expression)

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

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text 1",
        )
        repr_str: str = repr(svg_text)
        expected: str = f'SVGText("{svg_text.variable_name}")'
        assert repr_str == expected

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        svg_text: SVGText = SVGText(
            text="test text 1",
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {svg_text.variable_name} = {stage.variable_name}" "\n  .text()"
        )
        assert expected in expression