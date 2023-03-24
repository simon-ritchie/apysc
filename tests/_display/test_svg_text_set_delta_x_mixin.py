import apysc as ap
from apysc._display.svg_text_delta_x_mixin import SVGTextDeltaXMixIn
from apysc._display.svg_text_set_delta_x_mixin import SVGTextSetDeltaXMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    VariableNameSuffixAttrOrVarMixIn,
    VariableNameSuffixMixIn,
    SVGTextDeltaXMixIn,
    SVGTextSetDeltaXMixIn,
):
    pass


class TestSVGTextSetDeltaXMixIn:
    @apply_test_settings()
    def test__set_delta_x(self) -> None:
        mixin_1: SVGTextSetDeltaXMixIn = SVGTextSetDeltaXMixIn()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_1._set_delta_x,
            match="This method is only supported an ",
            delta_x=10.5,
        )

        mixin_2: _TestMixIn = _TestMixIn()
        mixin_2.variable_name = "test_mixin"
        mixin_2._variable_name_suffix = "test_suffix"
        mixin_2._set_delta_x(delta_x=10.5)
        assert "test_suffix" in mixin_2.delta_x.variable_name
        assert "delta_x" in mixin_2.delta_x.variable_name
        assert mixin_2.delta_x == ap.Number(10.5)
        mixin_2._set_delta_x(delta_x=ap.Number(20.5))
        assert mixin_2.delta_x == ap.Number(20.5)
