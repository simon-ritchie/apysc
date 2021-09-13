from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_y_interface import SkewYInterface
from apysc._expression import expression_data_util


class _TestInterface(SkewYInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the SkewYInterface class.
        """
        self.variable_name = 'test_skew_y_interface'


class TestSkewYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_skew_y_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_skew_y_if_not_initialized()
        assert interface._skew_y == 0

        interface._skew_y = ap.Int(10)
        interface._initialize_skew_y_if_not_initialized()
        assert interface._skew_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_skew_y(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.skew_y == 0

        interface.skew_y = ap.Int(10)
        assert interface.skew_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_skew_y_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestInterface = _TestInterface()
        before_value: ap.Int = ap.Int(10)
        interface.skew_y = before_value
        after_value: ap.Int = ap.Int(20)
        interface.skew_y = after_value
        expression: str = expression_data_util.get_current_expression()
        interface_name: str = interface.variable_name
        expected: str = (
            f'{interface_name}.skew(0, -{before_value.variable_name});'
            f'\n{interface_name}.skew(0, {after_value.variable_name});'
            f'\n{before_value.variable_name} = {after_value.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.skew_y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._skew_y_snapshot[snapshot_name] == 10

        interface.skew_y = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._skew_y_snapshot[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.skew_y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.skew_y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.skew_y == 10

        interface.skew_y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.skew_y == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_skew_y_attr_linking_setting(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_skew_y_if_not_initialized()
        assert interface._attr_linking_stack['skew_y'] == [0]
