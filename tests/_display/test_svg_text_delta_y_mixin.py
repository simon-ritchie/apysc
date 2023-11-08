import apysc as ap
from apysc._display.svg_text_delta_y_mixin import SvgTextDeltaYMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SvgTextDeltaYMixIn,
):
    pass


class TestSvgTextDeltaYMixIn:
    @apply_test_settings()
    def test_delta_y(self) -> None:
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

    @apply_test_settings()
    def test__make_snapshot_and__revert(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._delta_y = 50.5
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._delta_y = 60.5
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.delta_y == ap.Number(50.5)
