# pyright: reportUnusedExpression=false

from random import randint

from retrying import retry

import apysc as ap
from apysc._display.cx_interface import CxInterface
from apysc._expression import expression_data_util


class TestCxInterface:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_x_if_not_initialized(self) -> None:
        interface: CxInterface = CxInterface()
        interface._initialize_x_if_not_initialized()
        assert interface._x == 0

        interface._x = ap.Int(10)
        interface._initialize_x_if_not_initialized()
        assert interface._x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = "test_x_interface"
        assert interface.x == 0

        interface.x = ap.Int(10)
        assert interface.x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: CxInterface = CxInterface()
        interface.variable_name = "test_x_interface"
        x: ap.Int = ap.Int(10)
        interface.x = x
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{interface.variable_name}.cx({x.variable_name});"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = "test_x_interface"
        interface.x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._x_snapshots[snapshot_name] == 10

        interface.x = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = "test_x_interface"
        interface.x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.x == 10

        interface.x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_attr_linking_setting(self) -> None:
        interface: CxInterface = CxInterface()
        interface.variable_name = "test_x_interface"
        interface._initialize_x_if_not_initialized()
        interface._attr_linking_stack["x"] == [ap.Int(0)]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_x_and_skip_appending_exp(self) -> None:
        interface: CxInterface = CxInterface()
        interface._update_x_and_skip_appending_exp(x=100)
        assert interface.x == 100
        assert isinstance(interface.x, ap.Int)

        interface._update_x_and_skip_appending_exp(x=ap.Int(200))
        assert interface.x == 200
        assert isinstance(interface.x, ap.Int)
