import apysc as ap
from apysc._display.ellipse_height_mixin import EllipseHeightMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestEllipseHeightMixIn:
    @apply_test_settings()
    def test__initialize_ellipse_height_if_not_initialized(self) -> None:
        mixin: EllipseHeightMixIn = EllipseHeightMixIn()
        mixin._initialize_ellipse_height_if_not_initialized()
        assert mixin._ellipse_height == 0

        mixin._ellipse_height = ap.Int(10)
        mixin._initialize_ellipse_height_if_not_initialized()
        assert mixin._ellipse_height == 10

    @apply_test_settings()
    def test_ellipse_height(self) -> None:
        mixin: EllipseHeightMixIn = EllipseHeightMixIn()
        mixin.variable_name = "test_ellipse_height_mixin"
        assert mixin.ellipse_height == 0

        mixin.ellipse_height = ap.Int(10)
        assert mixin.ellipse_height == 10

    @apply_test_settings()
    def test__append_ellipse_height_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: EllipseHeightMixIn = EllipseHeightMixIn()
        mixin.variable_name = "test_ellipse_height_mixin"
        ellipse_height: ap.Int = ap.Int(10)
        mixin.ellipse_height = ellipse_height
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.radius(0, " f"{ellipse_height.variable_name});"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        ellipse_width: ap.Int = ap.Int(20)
        setattr(mixin, "_ellipse_width", ellipse_width)
        mixin.ellipse_height = ellipse_height
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{mixin.variable_name}.radius("
            f"{ellipse_width.variable_name}, "
            f"{ellipse_height.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: EllipseHeightMixIn = EllipseHeightMixIn()
        mixin.variable_name = "test_ellipse_height_mixin"
        mixin.ellipse_height = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._ellipse_height_snapshots[snapshot_name] == 10

        mixin.ellipse_height = ap.Int(20)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._ellipse_height_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: EllipseHeightMixIn = EllipseHeightMixIn()
        mixin.variable_name = "test_ellipse_height_mixin"
        mixin.ellipse_height = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.ellipse_height = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.ellipse_height == 10

        mixin.ellipse_height = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.ellipse_height == 20

    @apply_test_settings()
    def test__append_ellipse_height_attr_linking_setting(self) -> None:
        mixin: EllipseHeightMixIn = EllipseHeightMixIn()
        mixin.variable_name = "test_ellipse_height_mixin"
        mixin._initialize_ellipse_height_if_not_initialized()
        assert mixin._attr_linking_stack["ellipse_height"] == [ap.Int(0)]
