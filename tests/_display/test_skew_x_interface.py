from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_x_interface import SkewXInterface
from apysc._expression import expression_data_util


class _TestInterface(SkewXInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the SkewXInterface.
        """
        self.variable_name = 'test_skew_x_interface'


class TestSkewXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_skew_x_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_skew_x_if_not_initialized()
        assert interface._skew_x == 0

        interface._skew_x = ap.Int(10)
        interface._initialize_skew_x_if_not_initialized()
        assert interface._skew_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_skew_x(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.skew_x == 0

        interface.skew_x = ap.Int(10)
        assert interface.skew_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_skew_x_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestInterface = _TestInterface()
        before_value: ap.Int = ap.Int(10)
        interface.skew_x = before_value
        after_value: ap.Int = ap.Int(20)
        interface.skew_x = after_value
        interface_name: str = interface.variable_name
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_name}.skew(-{before_value.variable_name}, 0);'
            f'\n{interface_name}.skew({after_value.variable_name}, 0);'
            f'\n{before_value.variable_name} = {after_value.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.skew_x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._skew_x_snapshots[snapshot_name] == 10

        interface.skew_x = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._skew_x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.skew_x = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.skew_x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._skew_x == 10

        interface.skew_x = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._skew_x == 20
