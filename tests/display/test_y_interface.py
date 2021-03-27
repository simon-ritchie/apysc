from random import randint

from retrying import retry

from apysc.display.y_interface import YInterface
from apysc.expression import expression_file_util
from apysc.type import Int
from apysc.type import value_util


class TestYInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_y(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = Int(200)
        assert y_interface.y == 200

        y: Int = y_interface.y
        assert y == y_interface._y
        assert y.variable_name != y_interface.y.variable_name

        y_interface.y = 300  # type: ignore
        assert y_interface.y == 300

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_y_update_expression(self) -> None:
        y_interface: YInterface = YInterface()
        expression_file_util.remove_expression_file()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = Int(300)
        expression: str = expression_file_util.get_current_expression()
        value_str: str = value_util.get_value_str_for_expression(
            value=y_interface._y)
        expected: str = f'test_y_interface.y({value_str});'
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_y_if_not_initialized(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface._initialize_y_if_not_initialized()
        assert y_interface.y == 0

        y_interface.y = Int(100)
        y_interface._initialize_y_if_not_initialized()
        assert y_interface.y == 100

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = Int(100)
        snapshot_name: str = 'snapshot_1'
        y_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert y_interface._y_snapshots[snapshot_name] == 100

        y_interface.y = Int(150)
        y_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert y_interface._y_snapshots[snapshot_name] == 100

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = Int(100)
        snapshot_name: str = 'snapshot_1'
        y_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        y_interface.y = Int(150)
        y_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert y_interface.y == 100

        y_interface.y = Int(150)
        y_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert y_interface.y == 150
