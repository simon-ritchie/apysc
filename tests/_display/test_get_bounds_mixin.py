import apysc as ap
from apysc._display.get_bounds_mixin import GetBoundsMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestMixIn(
    GetBoundsMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestGetBoundsMixIn:
    @apply_test_settings()
    def test_get_bounds(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        mixin._variable_name_suffix = "test_suffix"
        bounding_box: ap.RectangleGeom = mixin.get_bounds()

        assert "test_suffix" in bounding_box.left_x.variable_name
        assert "left_x" in bounding_box.left_x.variable_name

        assert "test_suffix" in bounding_box.center_x.variable_name
        assert "center_x" in bounding_box.center_x.variable_name

        assert "test_suffix" in bounding_box.right_x.variable_name
        assert "right_x" in bounding_box.right_x.variable_name

        assert "test_suffix" in bounding_box.top_y.variable_name
        assert "top_y" in bounding_box.top_y.variable_name

        assert "test_suffix" in bounding_box.center_y.variable_name
        assert "center_y" in bounding_box.center_y.variable_name

        assert "test_suffix" in bounding_box.bottom_y.variable_name
        assert "bottom_y" in bounding_box.bottom_y.variable_name

        assert "test_suffix" in bounding_box.width.variable_name
        assert "width" in bounding_box.width.variable_name

        assert "test_suffix" in bounding_box.height.variable_name
        assert "height" in bounding_box.height.variable_name

        expression: str = expression_data_util.get_current_expression()
        assert f"{mixin.variable_name}.rbox(" in expression

    @apply_test_settings()
    def test__append_get_bounds_expression(self) -> None:
        stage: ap.Stage = ap.Stage()
        mixin: _TestMixIn = _TestMixIn()
        mixin.variable_name = "test_mixin"
        bounding_box: ap.RectangleGeom = mixin.get_bounds()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var box = {mixin.variable_name}.rbox({stage.variable_name});"
            f"\n{bounding_box.left_x.variable_name} = box.x;"
            f"\n{bounding_box.center_x.variable_name} = box.cx;"
            f"\n{bounding_box.right_x.variable_name} = box.x2;"
            f"\n{bounding_box.top_y.variable_name} = box.y;"
            f"\n{bounding_box.center_y.variable_name} = box.cy;"
            f"\n{bounding_box.bottom_y.variable_name} = box.y2;"
            f"\n{bounding_box.width.variable_name} = box.width;"
            f"\n{bounding_box.height.variable_name} = box.height;"
        )
        assert expected in expression
