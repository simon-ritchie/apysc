from random import randint

from retrying import retry

from apysc import Int
from apysc._display.height_interface import HeightInterface
from apysc._expression import expression_file_util


class TestHeightInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_height(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        height_interface.height = Int(200)
        assert height_interface.height == 200

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_height_update_expression(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        expression_file_util.remove_expression_file()
        height_interface.height = Int(300)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'test_height_interface.height(300);'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_height_and_skip_appending_exp(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        expression_file_util.remove_expression_file()
        height_interface._update_height_and_skip_appending_exp(
            value=Int(300))
        assert height_interface.height == 300

        expression: str = expression_file_util.get_current_expression()
        assert 'height(' not in expression

        height_interface._update_height_and_skip_appending_exp(
            value=400)
        assert height_interface.height == 400

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_height_if_not_initialized(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        height_interface._initialize_height_if_not_initialized()
        assert height_interface.height == 0

        height_interface.height = Int(10)
        height_interface._initialize_height_if_not_initialized()
        assert height_interface.height == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        height_interface.height = Int(10)
        snapshot_name: str = 'snapshot_1'
        height_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert height_interface._height_snapshots[snapshot_name] == 10

        height_interface.height = Int(5)
        height_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert height_interface._height_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        height_interface.height = Int(10)
        snapshot_name: str = 'snapshot_1'
        height_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        height_interface.height = Int(5)
        height_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert height_interface.height == 10

        height_interface.height = Int(5)
        height_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert height_interface.height == 5
