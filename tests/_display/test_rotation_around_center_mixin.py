# pyright: reportUnusedExpression=false

import apysc as ap
from apysc._display.rotation_around_center_mixin import RotationAroundCenterMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class _TestMixIn(RotationAroundCenterMixIn):
    def __init__(self) -> None:
        """
        The class for the testing of the RotationAroundCenterMixIn.
        """
        self.variable_name = "test_rotation_around_center_mixin"


class TestRotationAroundCenterMixIn:
    @apply_test_settings()
    def test__initialize_rotation_around_center_if_not_initialized(self) -> None:
        mixin: RotationAroundCenterMixIn = RotationAroundCenterMixIn()
        mixin._initialize_rotation_around_center_if_not_initialized()
        assert mixin._rotation_around_center == 0
        mixin._rotation_around_center._value = 10
        mixin._initialize_rotation_around_center_if_not_initialized()
        assert mixin._rotation_around_center == 10

    @apply_test_settings()
    def test_rotation_around_center(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        assert mixin.rotation_around_center == 0
        mixin.rotation_around_center = ap.Int(10)
        assert mixin.rotation_around_center == 10

    @apply_test_settings()
    def test__append_rotation_around_center_update_expression(self) -> None:
        ap.Stage()
        mixin: _TestMixIn = _TestMixIn()
        int_1: ap.Int = ap.Int(10)
        int_2: ap.Int = ap.Int(20)
        mixin.rotation_around_center = int_1
        mixin.rotation_around_center = int_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{mixin.variable_name}.rotate(-{int_1.variable_name});"
            f"\n{mixin.variable_name}.rotate({int_2.variable_name});"
            f"\n{int_1.variable_name} = {int_2.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin.rotation_around_center = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if mixin._rotation_around_center_snapshots is None:
            raise AssertionError()
        mixin._rotation_around_center_snapshots[snapshot_name] == 10

        mixin.rotation_around_center = ap.Int(20)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._rotation_around_center_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin.rotation_around_center = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.rotation_around_center = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.rotation_around_center == 10

        mixin.rotation_around_center = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.rotation_around_center == 20

    @apply_test_settings()
    def test__append_rotation_around_center_attr_linking_setting(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._initialize_rotation_around_center_if_not_initialized()
        assert mixin._attr_linking_stack["rotation_around_center"] == [ap.Int(0)]
