from typing import Union
import apysc as ap
from apysc._display.svg_text_singleton_for_text_span import SVGTextSingletonForTextSpan
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._display import svg_text_span
from tests._display.test_graphics_expression import assert_fill_attr_expression_exists


class TestSVGTextSpan:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        ap.Stage()
        svg_text_span: ap.SVGTextSpan = ap.SVGTextSpan(
            text="test_text_span",
            fill_color="#0af",
        )
        svg_text: ap.SVGText = SVGTextSingletonForTextSpan.get_instance()
        expression: str = expression_data_util.get_current_expression()
        assert (
            f"var {svg_text_span.variable_name} = {svg_text.variable_name}\n  .tspan()"
            in expression
        )
        assert "\n  .attr({" in expression
        assert "\n});" in expression
        assert_fill_attr_expression_exists(expression=expression)

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        svg_text_span: ap.SVGTextSpan = ap.SVGTextSpan(text="test_text_span")
        repr_str: str = repr(svg_text_span)
        assert repr_str == f'SVGTextSpan("{svg_text_span.variable_name}")'


@apply_test_settings()
def test__get_init_fill_color_str() -> None:
    fill_color_: Union[str, ap.String] = svg_text_span._get_init_fill_color_str(
        fill_color="#0af"
    )
    assert fill_color_ == "#0af"

    fill_color_ = svg_text_span._get_init_fill_color_str(fill_color=ap.String("#0af"))
    assert fill_color_ == ap.String("#0af")

    fill_color_ = svg_text_span._get_init_fill_color_str(fill_color=None)
    assert fill_color_ == ""
