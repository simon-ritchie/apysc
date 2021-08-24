from random import randint

from retrying import retry

import apysc as ap
from apysc._display.cy_interface import CyInterface
from apysc._expression import expression_data_util


class TestCyInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_cy_if_not_initialized(self) -> None:
        interface: CyInterface = CyInterface()
        interface._initialize_cy_if_not_initialized()
        assert interface._cy == 0

        interface._cy = ap.Int(10)
        interface._initialize_cy_if_not_initialized()
        assert interface._cy == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        interface: CyInterface = CyInterface()
        interface.variable_name = 'test_cy_interface'
        assert interface.y == 0

        interface.y = ap.Int(10)
        assert interface.y == 10

        interface.y = 20  # type: ignore
        assert interface.y == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_cy_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: CyInterface = CyInterface()
        interface.variable_name = 'test_cy_interface'
        y: ap.Int = ap.Int(10)
        interface.y = y
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.cy({y.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: CyInterface = CyInterface()
        interface.variable_name = 'test_cy_interface'
        interface.y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._cy_snapshots[snapshot_name] == 10

        interface.y = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._cy_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: CyInterface = CyInterface()
        interface.variable_name = 'test_cy_interface'
        interface.y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.y == 10

        interface.y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.y == 20
