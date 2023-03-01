import apysc as ap
from apysc._display.svg_text_singleton_for_text_span import SVGTextSingletonForTextSpan
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestSVGTextSpan:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        ap.Stage()
        svg_text_span: ap.SVGTextSpan = ap.SVGTextSpan(text="test_text_span")
        svg_text: ap.SVGText = SVGTextSingletonForTextSpan.get_instance()
        expression: str = expression_data_util.get_current_expression()
        assert (
            f"var {svg_text_span.variable_name} = {svg_text.variable_name}\n  .tspan()"
            in expression
        )
        assert "\n  .attr({" in expression
        assert "\n});" in expression

    @apply_test_settings()
    def test___repr__(self) -> None:
        ap.Stage()
        svg_text_span: ap.SVGTextSpan = ap.SVGTextSpan(text="test_text_span")
        repr_str: str = repr(svg_text_span)
        assert repr_str == f'SVGTextSpan("{svg_text_span.variable_name}")'
