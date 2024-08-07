from random import randint

from retrying import retry

import apysc as ap
from apysc._display.y_interface import YInterface
from apysc._expression import expression_data_util
from apysc._type import value_util


class TestYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = ap.Int(200)
        assert y_interface.y == 200

        y: ap.Int = y_interface.y
        assert y == y_interface._y
        assert y.variable_name != y_interface.y.variable_name

        y_interface.y = 300  # type: ignore
        assert y_interface.y == 300

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_update_expression(self) -> None:
        y_interface: YInterface = YInterface()
        expression_data_util.empty_expression()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = ap.Int(300)
        expression: str = expression_data_util.get_current_expression()
        value_str: str = value_util.get_value_str_for_expression(
            value=y_interface._y)
        expected: str = f'test_y_interface.y({value_str});'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_y_if_not_initialized(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface._initialize_y_if_not_initialized()
        assert y_interface.y == 0

        y_interface.y = ap.Int(100)
        y_interface._initialize_y_if_not_initialized()
        assert y_interface.y == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = ap.Int(100)
        snapshot_name: str = 'snapshot_1'
        y_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert y_interface._y_snapshots[snapshot_name] == 100

        y_interface.y = ap.Int(150)
        y_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert y_interface._y_snapshots[snapshot_name] == 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        y_interface: YInterface = YInterface()
        y_interface.variable_name = 'test_y_interface'
        y_interface.y = ap.Int(100)
        snapshot_name: str = 'snapshot_1'
        y_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        y_interface.y = ap.Int(150)
        y_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert y_interface.y == 100

        y_interface.y = ap.Int(150)
        y_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert y_interface.y == 150

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_y_attr_linking_setting(self) -> None:
        interface: YInterface = YInterface()
        interface.variable_name = 'test_y_interface'
        interface._initialize_y_if_not_initialized()
        assert interface._attr_linking_stack['y'] == [ap.Int(0)]
