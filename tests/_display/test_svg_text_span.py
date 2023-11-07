from typing import Union

import apysc as ap
from apysc._display import svg_text_span
from apysc._display.svg_text_singleton_for_text_span import SVGTextSingletonForTextSpan
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from tests._display.test_graphics_expression import assert_fill_attr_expression_exists


class TestSvgTextSpan:
    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        svg_text_span: ap.SvgTextSpan = ap.SvgTextSpan(
            text="test_text_span",
            fill_color=ap.Color("#0af"),
        )
        svg_text: ap.SvgText = SVGTextSingletonForTextSpan.get_instance()
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
        svg_text_span: ap.SvgTextSpan = ap.SvgTextSpan(text="test_text_span")
        repr_str: str = repr(svg_text_span)
        assert repr_str == f'SvgTextSpan("{svg_text_span.variable_name}")'

    @apply_test_settings()
    def test___init__(self) -> None:
        svg_text_span: ap.SvgTextSpan = ap.SvgTextSpan(
            text="test_text_span",
            variable_name_suffix="test_span",
        )
        assert svg_text_span._skip_fill_color_expression_appending
        assert svg_text_span._skip_fill_alpha_expression_appending
        assert svg_text_span._skip_line_color_expression_appending
        assert svg_text_span._skip_line_alpha_expression_appending
        assert svg_text_span._skip_line_thickness_expression_appending
        expression: str = expression_data_util.get_current_expression()
        assert ".tspan" in expression
        assert svg_text_span.text == "test_text_span"
        assert var_names.SVG_TEXT_SPAN in svg_text_span.variable_name
        assert "test_span" in svg_text_span.variable_name

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            fill_color=ap.Color("#0af"),
        )
        assert not svg_text_span._skip_fill_color_expression_appending

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            fill_alpha=0.5,
        )
        assert not svg_text_span._skip_fill_alpha_expression_appending

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            line_color=ap.Color("#0af"),
        )
        assert not svg_text_span._skip_line_color_expression_appending

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            line_alpha=0.3,
        )
        assert not svg_text_span._skip_line_alpha_expression_appending

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            line_thickness=3,
        )
        assert not svg_text_span._skip_line_thickness_expression_appending

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            delta_x=50.5,
        )
        assert svg_text_span.delta_x == ap.Number(50.5)

        svg_text_span = ap.SvgTextSpan(
            text="test_text_span",
            delta_y=60.5,
        )
        assert svg_text_span.delta_y == ap.Number(60.5)

    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        svg_text_span_: ap.SvgTextSpan = ap.SvgTextSpan._initialize_with_base_value()
        assert svg_text_span_.text == ap.String("")
        assert svg_text_span_.visible == ap.Boolean(False)


@apply_test_settings()
def test__get_init_fill_color() -> None:
    fill_color_: ap.Color = svg_text_span._get_init_fill_color(
        fill_color=ap.Color("#0af")
    )
    assert fill_color_ == ap.Color("#0af")

    fill_color_ = svg_text_span._get_init_fill_color(fill_color=None)
    assert fill_color_ == ap.COLORLESS


@apply_test_settings()
def test__get_init_fill_alpha_num() -> None:
    fill_alpha_: Union[float, ap.Number] = svg_text_span._get_init_fill_alpha_num(
        fill_alpha=0.5,
    )
    assert fill_alpha_ == 0.5

    fill_alpha_ = svg_text_span._get_init_fill_alpha_num(fill_alpha=ap.Number(0.8))
    assert fill_alpha_ == ap.Number(0.8)

    fill_alpha_ = svg_text_span._get_init_fill_alpha_num(fill_alpha=None)
    assert fill_alpha_ == 1.0


@apply_test_settings()
def test__get_init_line_color() -> None:
    line_color_: ap.Color = svg_text_span._get_init_line_color(
        line_color=ap.Color("#0af"),
    )
    assert line_color_ == ap.Color("#0af")

    line_color_ = svg_text_span._get_init_line_color(line_color=None)
    assert line_color_ == ap.COLORLESS


@apply_test_settings()
def test__get_init_line_alpha_num() -> None:
    line_alpha_: Union[float, ap.Number] = svg_text_span._get_init_line_alpha_num(
        line_alpha=0.5
    )
    assert line_alpha_ == 0.5

    line_alpha_ = svg_text_span._get_init_line_alpha_num(line_alpha=ap.Number(0.8))
    assert line_alpha_ == ap.Number(0.8)

    line_alpha_ = svg_text_span._get_init_line_alpha_num(line_alpha=None)
    assert line_alpha_ == 1.0


@apply_test_settings()
def test__get_init_line_thickness_num() -> None:
    line_thickness_: Union[int, ap.Int] = svg_text_span._get_init_line_thickness_num(
        line_thickness=3,
    )
    assert line_thickness_ == 3

    line_thickness_ = svg_text_span._get_init_line_thickness_num(
        line_thickness=ap.Int(5)
    )
    assert line_thickness_ == ap.Int(5)

    line_thickness_ = svg_text_span._get_init_line_thickness_num(line_thickness=None)
    assert line_thickness_ == 1
