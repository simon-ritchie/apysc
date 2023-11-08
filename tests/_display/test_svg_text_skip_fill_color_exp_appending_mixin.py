import apysc as ap
from apysc._display.svg_text_skip_fill_color_exp_appending_mixin import (
    SvgTextSkipFillColorExpAppendingMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSVGTextSkipFillColorExpAppendingMixIn:
    @apply_test_settings()
    def test__set_fill_color_expression_skipping_attr(self) -> None:
        mixin: SvgTextSkipFillColorExpAppendingMixIn
        mixin = SvgTextSkipFillColorExpAppendingMixIn()
        mixin._set_fill_color_expression_skipping_attr(fill_color=ap.Color("#0af"))
        assert not mixin._skip_fill_color_expression_appending
        mixin._set_fill_color_expression_skipping_attr(fill_color=None)
        assert mixin._skip_fill_color_expression_appending
