import apysc as ap
from apysc._display.svg_text_delta_y_mixin import SVGTextDeltaYMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextDeltaYMixIn,
):
    pass


class TestSVGTextDeltaYMixIn:
    @apply_test_settings()
    def test_delta_y(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        mixin._delta_y = 30.5
        delta_y: ap.Number = mixin.delta_y
        assert delta_y == 30.5
        assert "test_suffix" in delta_y.variable_name
        assert "delta_y" in delta_y.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{delta_y.variable_name} = {mixin.variable_name}.dy();"
        assert expected in expression

        delta_y = ap.Number(50.5)
        mixin.delta_y = delta_y
        assert mixin.delta_y == ap.Number(50.5)
        expression = expression_data_util.get_current_expression()
        expected = f"{mixin.variable_name}.dy({delta_y.variable_name});"
