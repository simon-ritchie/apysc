import apysc as ap
from apysc._display.ellipse_width_mixin import EllipseWidthMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    EllipseWidthMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestEllipseWidthMixIn:
    @apply_test_settings()
    def test__initialize_ellipse_width_if_not_initialized(self) -> None:
        instance: _TestObject = _TestObject()
        instance._initialize_ellipse_width_if_not_initialized()
        assert instance._ellipse_width == 0

        instance._ellipse_width.value = 10
        instance._initialize_ellipse_width_if_not_initialized()
        assert instance._ellipse_width == 10

    @apply_test_settings()
    def test_ellipse_width(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_ellipse_width_mixin"
        assert instance.ellipse_width == 0

        instance.ellipse_width = ap.Int(10)
        assert instance.ellipse_width == 10

    @apply_test_settings()
    def test__append_ellipse_width_update_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_ellipse_width_mixin"
        ellipse_width: ap.Int = ap.Int(10)
        instance.ellipse_width = ellipse_width
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{instance.variable_name}.radius({ellipse_width.variable_name}" ", 0);"
        )
        assert expected in expression

        ap.Stage()
        ellipse_height: ap.Int = ap.Int(20)
        setattr(instance, "_ellipse_height", ellipse_height)
        instance.ellipse_width = ellipse_width
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{instance.variable_name}.radius({ellipse_width.variable_name}"
            f", {ellipse_height.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_ellipse_width_mixin"
        instance.ellipse_width = ap.Int(10)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if instance._ellipse_width_snapshots is None:
            raise AssertionError()
        assert instance._ellipse_width_snapshots[snapshot_name] == 10

        instance.ellipse_width = ap.Int(20)
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._ellipse_width_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_ellipse_width_mixin"
        instance.ellipse_width = ap.Int(10)
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance.ellipse_width = ap.Int(20)
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.ellipse_width == 10

        instance.ellipse_width = ap.Int(20)
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        assert instance.ellipse_width == 20

    @apply_test_settings()
    def test__append_ellipse_width_attr_linking_setting(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_ellipse_width_mixin"
        instance._initialize_ellipse_width_if_not_initialized()
        assert instance._attr_linking_stack["ellipse_width"] == [ap.Int(0)]
