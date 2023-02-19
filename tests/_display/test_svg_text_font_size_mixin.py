
import apysc as ap
from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestSVGTextFontSizeMixIn:
    @apply_test_settings()
    def test__append_font_size_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: SVGTextFontSizeMixIn = SVGTextFontSizeMixIn()
        mixin.variable_name = "test_mixin"
        font_size: ap.Int = ap.Int(15)
        mixin._append_font_size_getter_expression(font_size=font_size)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{font_size.variable_name} = {mixin.variable_name}.font("size");'
        )
        assert expected in expression

    @apply_test_settings()
    def test_font_size(self) -> None:
        expression_data_util.empty_expression()
        mixin: SVGTextFontSizeMixIn = SVGTextFontSizeMixIn()
        mixin.variable_name = "test_mixin"
        font_size: ap.Int = mixin.font_size
        assert font_size == ap.Int(mixin._font_size)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{font_size.variable_name} = {mixin.variable_name}.font("size");'
        )
        assert expected in expression

        font_size = ap.Int(18)
        mixin.font_size = font_size
        assert mixin.font_size == ap.Int(18)
        expression = expression_data_util.get_current_expression()
        expected = f'{mixin.variable_name}.font("size", {font_size.variable_name});'

    @apply_test_settings()
    def test__make_snapshot_and__revert(self) -> None:
        mixin: SVGTextFontSizeMixIn = SVGTextFontSizeMixIn()
        mixin._font_size = 18
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._font_size = 20
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._font_size == 18

        mixin._font_size = 20
        mixin._run_all_revert_methods(snapshot_name="not_existing_snapshot")
        assert mixin._font_size == 20
