from random import randint

from retrying import retry

import apysc as ap
from apysc._display.width_interface import WidthInterface
from apysc._expression import expression_file_util


class TestWidthInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_width(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        width_interface.width = ap.Int(100)
        assert width_interface.width == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_width_update_expression(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        expression_file_util.remove_expression_file()
        width_interface.width = ap.Int(200)
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_width_interface.width(200);'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_update_width_and_skip_appending_exp(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        expression_file_util.remove_expression_file()
        width_interface._update_width_and_skip_appending_exp(
            value=ap.Int(300))
        assert width_interface.width == 300
        expression: str = expression_file_util.get_current_expression()
        assert 'width(' not in expression

        width_interface._update_width_and_skip_appending_exp(
            value=400)
        assert width_interface.width == 400

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_width_if_not_initialized(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        width_interface._initialize_width_if_not_initialized()
        assert width_interface.width == 0

        width_interface.width = ap.Int(10)
        width_interface._initialize_width_if_not_initialized()
        assert width_interface.width == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        width_interface.width = ap.Int(10)
        snapshot_name: str = 'snapshot_1'
        width_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert width_interface._width_snapshots[snapshot_name] == 10

        width_interface.width = ap.Int(15)
        width_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert width_interface._width_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        width_interface: WidthInterface = WidthInterface()
        width_interface.variable_name = 'test_width_interface'
        width_interface.width = ap.Int(10)
        snapshot_name: str = 'snapshot_1'
        width_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        width_interface.width = ap.Int(15)
        width_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert width_interface.width == 10

        width_interface.width = ap.Int(15)
        width_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert width_interface.width == 15
