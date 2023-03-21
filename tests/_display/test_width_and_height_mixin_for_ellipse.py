import apysc as ap
from apysc._display.width_and_height_mixin_for_ellipse import (
    WidthAndHeightMixInForEllipse,
)
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestWidthAndHeightMixInForEllipse:
    @apply_test_settings()
    def test__initialize_width_and_height_if_not_initialized(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin._initialize_width_and_height_if_not_initialized()
        assert mixin._width == 0
        assert mixin._height == 0

        mixin._width = ap.Int(10)
        mixin._height = ap.Int(20)
        mixin._initialize_width_and_height_if_not_initialized()
        assert mixin._width == 10
        assert mixin._height == 20

    @apply_test_settings()
    def test_width(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        assert mixin.width == 0

        mixin.width = ap.Int(10)
        assert mixin.width == 10

    @apply_test_settings()
    def test_height(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        assert mixin.height == 0

        mixin.height = ap.Int(10)
        assert mixin.height == 10

    @apply_test_settings()
    def test__append_ellipse_width_and_height_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        width: ap.Int = ap.Int(10)
        mixin.width = width
        height: ap.Int = ap.Int(20)
        mixin.height = height
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.radius("
            f"Math.trunc({width.variable_name} / 2), "
            f"Math.trunc({height.variable_name}) / 2);"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        mixin.width = ap.Int(10)
        mixin.height = ap.Int(20)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin._width_snapshots is None:
            raise AssertionError()
        assert mixin._width_snapshots[snapshot_name] == 10
        if mixin._height_snapshots is None:
            raise AssertionError()
        assert mixin._height_snapshots[snapshot_name] == 20

        mixin.width = ap.Int(30)
        mixin.height = ap.Int(40)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._width_snapshots[snapshot_name] == 10
        assert mixin._height_snapshots[snapshot_name] == 20

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        mixin.width = ap.Int(10)
        mixin.height = ap.Int(20)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.width = ap.Int(30)
        mixin.height = ap.Int(40)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.width == 10
        assert mixin.height == 20

        mixin.width = ap.Int(30)
        mixin.height = ap.Int(40)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.width == 30
        assert mixin.height == 40

    @apply_test_settings()
    def test__append_width_attr_linking_setting(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        mixin._initialize_width_and_height_if_not_initialized()
        assert mixin._attr_linking_stack["width"] == [ap.Int(0)]

    @apply_test_settings()
    def test__append_height_attr_linking_setting(self) -> None:
        mixin: WidthAndHeightMixInForEllipse = WidthAndHeightMixInForEllipse()
        mixin.variable_name = "test_width_and_height_mixins_for_ellipse"
        mixin._initialize_width_and_height_if_not_initialized()
        assert mixin._attr_linking_stack["height"] == [ap.Int(0)]
