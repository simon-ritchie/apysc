import apysc as ap
from apysc._display.svg_text_delta_y_mixin import SvgTextDeltaYMixIn
from apysc._display.svg_text_set_delta_y_mixin import SvgTextSetDeltaYMixIn
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SvgTextDeltaYMixIn,
    SvgTextSetDeltaYMixIn,
):
    pass


class TestSVGTextSetDeltaYMixIn:
    # @apply_test_settings()
    def test__set_delta_y(self) -> None:
        mixin_1: SvgTextSetDeltaYMixIn = SvgTextSetDeltaYMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_delta_y,
            match="This method is only supported an ",
            delta_y=10.5,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.variable_name = "test_mixin"
        mixin_2._variable_name_suffix = "test_suffix"
        mixin_2._set_delta_y(delta_y=20.5)
        delta_y: ap.Number = mixin_2.delta_y
        assert delta_y == ap.Number(20.5)
        assert "test_suffix" in delta_y.variable_name
        assert "delta_y" in delta_y.variable_name

        delta_y = ap.Number(30.5)
        mixin_2._set_delta_y(delta_y=delta_y)
        assert mixin_2.delta_y == ap.Number(30.5)
