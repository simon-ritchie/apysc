from apysc._display.svg_text_skip_line_thickness_exp_appending_mixin import (
    SvgTextSkipLineThicknessExpAppendingMixIn,
)
from apysc._testing.testing_helper import apply_test_settings


class TestSVGTextSkipLineThicknessExpAppendingMixIn:
    @apply_test_settings()
    def test__set_line_thickness_expression_skipping_attr(self) -> None:
        mixin: SvgTextSkipLineThicknessExpAppendingMixIn
        mixin = SvgTextSkipLineThicknessExpAppendingMixIn()
        mixin._set_line_thickness_expression_skipping_attr(line_thickness=3)
        assert not mixin._skip_line_thickness_expression_appending
        mixin._set_line_thickness_expression_skipping_attr(line_thickness=None)
        assert mixin._skip_line_thickness_expression_appending
