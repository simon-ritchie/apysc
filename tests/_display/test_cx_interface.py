from random import randint

from retrying import retry

import apysc as ap
from apysc._display.cx_interface import CxInterface
from apysc._expression import expression_file_util


class TestCxInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_cx_if_not_initialized(self) -> None:
        interface: CxInterface = CxInterface()
        interface._initialize_cx_if_not_initialized()
        assert interface._cx == 0

        interface._cx = ap.Int(10)
        interface._initialize_cx_if_not_initialized()
        assert interface._cx == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        assert interface.x == 0

        interface.x = ap.Int(10)
        assert interface.x == 10

        interface.x = 20  # type: ignore
        assert interface.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_cx_update_expression(self) -> None:
        expression_file_util.empty_expression()
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        x: ap.Int = ap.Int(10)
        interface.x = x
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.cx({x.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        interface.x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._cx_snapshots[snapshot_name] == 10

        interface.x = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._cx_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        interface.x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.x == 10

        interface.x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.x == 20
