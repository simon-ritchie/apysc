from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_center_interface import \
    RotationAroundCenterInterface
from apysc._expression import expression_file_util


class _TestInterface(RotationAroundCenterInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the RotationAroundCenterInterface.
        """
        self.variable_name = 'test_rotation_around_center_interface'


class TestRotationAroundCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_rotation_around_center_if_not_initialized(
            self) -> None:
        interface: RotationAroundCenterInterface = \
            RotationAroundCenterInterface()
        interface._initialize_rotation_around_center_if_not_initialized()
        assert interface._rotation_around_center == 0
        interface._rotation_around_center._value = 10
        interface._initialize_rotation_around_center_if_not_initialized()
        assert interface._rotation_around_center == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_rotation_around_center(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.rotation_around_center == 0
        interface.rotation_around_center = ap.Int(10)
        assert interface.rotation_around_center == 10

        interface.rotation_around_center = 20  # type: ignore
        assert interface.rotation_around_center == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_rotation_around_center_update_expression(self) -> None:
        expression_file_util.empty_expression()
        interface: _TestInterface = _TestInterface()
        int_1: ap.Int = ap.Int(10)
        int_2: ap.Int = ap.Int(20)
        interface.rotation_around_center = int_1
        interface.rotation_around_center = int_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.rotate(-{int_1.variable_name});'
            f'\n{interface.variable_name}.rotate({int_2.variable_name});'
            f'\n{int_1.variable_name} = {int_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.rotation_around_center = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._rotation_around_center_snapshots[snapshot_name] == 10

        interface.rotation_around_center = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._rotation_around_center_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.rotation_around_center = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.rotation_around_center = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.rotation_around_center == 10

        interface.rotation_around_center = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.rotation_around_center == 20
