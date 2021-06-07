from random import randint

from retrying import retry

from apysc.display.cx_interface import CxInterface
from apysc.expression import expression_file_util
from apysc import Int


class TestCxInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_cx_if_not_initialized(self) -> None:
        interface: CxInterface = CxInterface()
        interface._initialize_cx_if_not_initialized()
        assert interface._cx == 0

        interface._cx = Int(10)
        interface._initialize_cx_if_not_initialized()
        assert interface._cx == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_cx(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        assert interface.cx == 0

        interface.cx = Int(10)
        assert interface.cx == 10

        interface.cx = 20  # type: ignore
        assert interface.cx == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_cx_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        cx: Int = Int(10)
        interface.cx = cx
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.cx({cx.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = 'test_cx_interface'
        interface.cx = Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._cx_snapshots[snapshot_name] == 10

        interface.cx = Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._cx_snapshots[snapshot_name] == 10
