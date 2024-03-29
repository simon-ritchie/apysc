import apysc as ap
from apysc._display.svg_text_skip_line_color_exp_appending_mixin import (
    SvgTextSkipLineColorExpAppendingMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSvgTextSkipLineColorExpAppendingMixIn:
    @apply_test_settings()
    def test__set_line_color_expression_skipping_attr(self) -> None:
        mixin: SvgTextSkipLineColorExpAppendingMixIn
        mixin = SvgTextSkipLineColorExpAppendingMixIn()
        mixin._set_line_color_expression_skipping_attr(line_color=ap.Color("#0af"))
        assert not mixin._skip_line_color_expression_appending
        mixin._set_line_color_expression_skipping_attr(line_color=None)
        assert mixin._skip_line_color_expression_appending
