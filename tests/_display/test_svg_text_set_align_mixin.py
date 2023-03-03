import apysc as ap
from apysc._expression import expression_data_util
from apysc._display.svg_text_align_mixin import SVGTextAlignMixIn
from apysc._display.svg_text_set_align_mixin import SVGTextSetAlignMixIn
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._display.svg_text_align_mixin import SVGTextAlign


class _TestMixIn(
    SVGTextAlignMixIn,
    SVGTextSetAlignMixIn,
):
    pass


class TestSVGTextSetAlignMixIn:
    @apply_test_settings()
    def test__set_align(self) -> None:
        mixin_1: SVGTextSetAlignMixIn = SVGTextSetAlignMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_align,
            match="This method is only supported a ",
            align=SVGTextAlign.CENTER,
        )

        expression_data_util.empty_expression()
        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2._set_align(align=SVGTextAlign.CENTER)
        assert mixin_2.align == SVGTextAlign.CENTER
        expression: str = expression_data_util.get_current_expression()
        assert '.font("anchor", "middle")' in expression
