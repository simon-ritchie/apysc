from apysc._display.svg_text_skip_fill_alpha_exp_appending_mixin import (
    SvgTextSkipFillAlphaExpAppendingMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSVGTextSkipFillAlphaExpAppendingMixIn:
    @apply_test_settings()
    def test__set_fill_alpha_expression_skipping_attr(self) -> None:
        mixin: SvgTextSkipFillAlphaExpAppendingMixIn
        mixin = SvgTextSkipFillAlphaExpAppendingMixIn()
        mixin._set_fill_alpha_expression_skipping_attr(fill_alpha=0.5)
        assert not mixin._skip_fill_alpha_expression_appending
        mixin._set_fill_alpha_expression_skipping_attr(fill_alpha=None)
        assert mixin._skip_fill_alpha_expression_appending
