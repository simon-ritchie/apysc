import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._display.svg_text_font_size_mixin import SVGTextFontSizeMixIn


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
