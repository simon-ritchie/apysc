import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn
from apysc._display.svg_text_delta_x_mixin import SVGTextDeltaXMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextDeltaXMixIn,
):
    pass


class TestSVGTextDeltaXMixIn:
    @apply_test_settings()
    def test_delta_x(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        mixin._delta_x = 30.5
        delta_x: ap.Number = mixin.delta_x
        assert delta_x == ap.Number(30.5)
        assert "test_suffix" in delta_x.variable_name
        assert "delta_x" in delta_x.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{delta_x.variable_name} = {mixin.variable_name}.dx();"
        assert expected in expression
