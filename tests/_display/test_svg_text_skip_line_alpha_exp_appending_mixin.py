from apysc._display.svg_text_skip_line_alpha_exp_appending_mixin import (
    SvgTextSkipLineAlphaExpAppendingMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSvgTextSkipLineAlphaExpAppendingMixIn:
    @apply_test_settings()
    def test__set_line_alpha_expression_skipping_attr(self) -> None:
        mixin: SvgTextSkipLineAlphaExpAppendingMixIn
        mixin = SvgTextSkipLineAlphaExpAppendingMixIn()
        mixin._set_line_alpha_expression_skipping_attr(line_alpha=0.5)
        assert not mixin._skip_line_alpha_expression_appending
        mixin._set_line_alpha_expression_skipping_attr(line_alpha=None)
        assert mixin._skip_line_alpha_expression_appending
