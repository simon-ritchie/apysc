from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_y_from_center_interface import \
    ScaleYFromCenterInterface
from apysc._expression import expression_data_util


class _TestInterface(ScaleYFromCenterInterface):

    def __init__(self) -> None:
        """
        The class for testing of the ScaleYFromCenterInterface.
        """
        self.variable_name = 'test_scale_y_from_center_interface'


class TestScaleYFromCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_y_from_center_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_y_from_center_if_not_initialized()
        assert interface._scale_y_from_center == 1.0
        interface._scale_y_from_center._value = 0.5
        interface._initialize_scale_y_from_center_if_not_initialized()
        assert interface._scale_y_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_scale_y_from_center(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.scale_y_from_center == 1.0
        interface.scale_y_from_center = ap.Number(0.5)
        assert interface.scale_y_from_center == 0.5

        interface.scale_y_from_center = 0.3  # type: ignore
        assert interface.scale_y_from_center == 0.3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_y_from_center_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestInterface = _TestInterface()
        num_1: ap.Number = ap.Number(0.5)
        num_2: ap.Number = ap.Number(0.3)
        interface.scale_y_from_center = num_1
        interface.scale_y_from_center = num_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.scale(1, 1 / {num_1.variable_name});'
            f'\n{interface.variable_name}.scale(1, {num_2.variable_name});'
            f'\n{num_1.variable_name} = {num_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.scale_y_from_center = ap.Number(0.5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._scale_y_from_center_snapshots[snapshot_name] == 0.5
        interface.scale_y_from_center = ap.Number(0.3)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._scale_y_from_center_snapshots[snapshot_name] == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.scale_y_from_center = ap.Number(0.5)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.scale_y_from_center = ap.Number(0.3)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.scale_y_from_center == 0.5

        interface.scale_y_from_center = ap.Number(0.3)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.scale_y_from_center == 0.3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_y_from_center_attr_linking_setting(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_y_from_center_if_not_initialized()
        assert interface._attr_linking_stack['scale_y_from_center'] == \
            [ap.Number(1.0)]
