import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.svg_text_font_family_mixin import SVGTextFontFamilyMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextFontFamilyMixIn,
):
    pass


class TestSVGTextFontFamilyMixIn:
    @apply_test_settings()
    def test__initialize_font_family_if_not_initialized(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._variable_name_suffix = "test_suffix"
        mixin._initialize_font_family_if_not_initialized()
        assert mixin._font_family == ap.Array([ap.String("")])
        assert "font_family" in mixin._font_family._variable_name_suffix

        mixin._font_family[0].value = "Impact"
        mixin._initialize_font_family_if_not_initialized()
        assert mixin._font_family == ap.Array([ap.String("Impact")])

    @apply_test_settings()
    def test__append_font_family_string_getter_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        font_family_string: ap.String = ap.String("Impact")
        mixin._append_font_family_string_getter_expression(
            font_family_string=font_family_string
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{font_family_string.variable_name} = "
            f'{mixin.variable_name}.font("family");'
        )
        assert expected in expression

    @apply_test_settings()
    def test_font_family(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        font_family: ap.Array[ap.String] = mixin.font_family
        expression: str = expression_data_util.get_current_expression()
        match_: Optional[Match] = re.search(
            pattern=rf"{font_family.variable_name} = .*\.split\(.*?\);",
            string=expression,
        )
        assert match_ is not None, expression

        font_family = font_family._copy()
        mixin.font_family = font_family
        expression = expression_data_util.get_current_expression()
        match_ = re.search(
            pattern=rf'{mixin.variable_name}.font\({{"family": .*}}\);',
            string=expression,
        )
        assert match_ is not None, expression
