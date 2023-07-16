from apysc._display.svg_text_align_mixin import SVGTextAlign
from apysc._display.svg_text_align_mixin import SVGTextAlignMixIn
from apysc._display.svg_text_set_align_mixin import SVGTextSetAlignMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
import apysc as ap


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
            match="This method is only supported an ",
            align=SVGTextAlign.CENTER,
        )

        ap.Stage()
        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2._set_align(align=SVGTextAlign.CENTER)
        assert mixin_2.align == SVGTextAlign.CENTER
        expression: str = expression_data_util.get_current_expression()
        assert '.font("anchor", "middle")' in expression
