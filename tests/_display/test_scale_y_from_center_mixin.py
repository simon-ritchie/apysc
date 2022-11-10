from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_y_from_center_mixin import ScaleYFromCenterMixIn
from apysc._expression import expression_data_util


class _TestMixIn(ScaleYFromCenterMixIn):
    def __init__(self) -> None:
        """
        The class for testing of the ScaleYFromCenterMixIn.
        """
        self.variable_name = "test_scale_y_from_center_mixin"


class TestScaleYFromCenterMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_y_from_center_if_not_initialized(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._initialize_scale_y_from_center_if_not_initialized()
        assert mixin._scale_y_from_center == 1.0
        mixin._scale_y_from_center._value = 0.5
        mixin._initialize_scale_y_from_center_if_not_initialized()
        assert mixin._scale_y_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_scale_y_from_center(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        assert mixin.scale_y_from_center == 1.0
        mixin.scale_y_from_center = ap.Number(0.5)
        assert mixin.scale_y_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_y_from_center_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        num_1: ap.Number = ap.Number(0.5)
        num_2: ap.Number = ap.Number(0.3)
        mixin.scale_y_from_center = num_1
        mixin.scale_y_from_center = num_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.scale(1, 1 / {num_1.variable_name});"
            f"\n{mixin.variable_name}.scale(1, {num_2.variable_name});"
            f"\n{num_1.variable_name} = {num_2.variable_name};"
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin.scale_y_from_center = ap.Number(0.5)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._scale_y_from_center_snapshots[snapshot_name] == 0.5
        mixin.scale_y_from_center = ap.Number(0.3)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._scale_y_from_center_snapshots[snapshot_name] == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin.scale_y_from_center = ap.Number(0.5)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.scale_y_from_center = ap.Number(0.3)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.scale_y_from_center == 0.5

        mixin.scale_y_from_center = ap.Number(0.3)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.scale_y_from_center == 0.3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_y_from_center_attr_linking_setting(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._initialize_scale_y_from_center_if_not_initialized()
        assert mixin._attr_linking_stack["scale_y_from_center"] == [ap.Number(1.0)]
