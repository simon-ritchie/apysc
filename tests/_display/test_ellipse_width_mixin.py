from random import randint

from retrying import retry

import apysc as ap
from apysc._display.ellipse_width_mixin import EllipseWidthMixIn
from apysc._expression import expression_data_util


class TestEllipseWidthMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ellipse_width_if_not_initialized(self) -> None:
        mixin: EllipseWidthMixIn = EllipseWidthMixIn()
        mixin._initialize_ellipse_width_if_not_initialized()
        assert mixin._ellipse_width == 0

        mixin._ellipse_width.value = 10
        mixin._initialize_ellipse_width_if_not_initialized()
        assert mixin._ellipse_width == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_ellipse_width(self) -> None:
        mixin: EllipseWidthMixIn = EllipseWidthMixIn()
        mixin.variable_name = "test_ellipse_width_mixin"
        assert mixin.ellipse_width == 0

        mixin.ellipse_width = ap.Int(10)
        assert mixin.ellipse_width == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_width_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: EllipseWidthMixIn = EllipseWidthMixIn()
        mixin.variable_name = "test_ellipse_width_mixin"
        ellipse_width: ap.Int = ap.Int(10)
        mixin.ellipse_width = ellipse_width
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.radius({ellipse_width.variable_name}" ", 0);"
        )
        assert expected in expression

        expression_data_util.empty_expression()
        ellipse_height: ap.Int = ap.Int(20)
        setattr(mixin, "_ellipse_height", ellipse_height)
        mixin.ellipse_width = ellipse_width
        expression = expression_data_util.get_current_expression()
        expected = (
            f"{mixin.variable_name}.radius({ellipse_width.variable_name}"
            f", {ellipse_height.variable_name});"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: EllipseWidthMixIn = EllipseWidthMixIn()
        mixin.variable_name = "test_ellipse_width_mixin"
        mixin.ellipse_width = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._ellipse_width_snapshots[snapshot_name] == 10

        mixin.ellipse_width = ap.Int(20)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._ellipse_width_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: EllipseWidthMixIn = EllipseWidthMixIn()
        mixin.variable_name = "test_ellipse_width_mixin"
        mixin.ellipse_width = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.ellipse_width = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.ellipse_width == 10

        mixin.ellipse_width = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.ellipse_width == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_width_attr_linking_setting(self) -> None:
        mixin: EllipseWidthMixIn = EllipseWidthMixIn()
        mixin.variable_name = "test_ellipse_width_mixin"
        mixin._initialize_ellipse_width_if_not_initialized()
        assert mixin._attr_linking_stack["ellipse_width"] == [ap.Int(0)]
