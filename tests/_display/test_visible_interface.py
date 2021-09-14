from random import randint

from retrying import retry

import apysc as ap
from apysc._display.visible_interface import VisibleInterface
from apysc._expression import expression_data_util


class _TestVisible(VisibleInterface):

    def __init__(self) -> None:
        """
        Test class for VisibleInterface.
        """
        self.variable_name = 'test_visible'


class TestVisibleInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_visible_if_not_initialized(self) -> None:
        interface_1: VisibleInterface = VisibleInterface()
        interface_1._initialize_visible_if_not_initialized()
        assert interface_1._visible

        interface_1._visible.value = False
        interface_1._initialize_visible_if_not_initialized()
        assert not interface_1._visible

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_visible(self) -> None:
        interface_1: _TestVisible = _TestVisible()
        result: ap.Boolean = interface_1.visible
        assert result
        assert interface_1._visible.variable_name != result.variable_name

        bool_1: ap.Boolean = ap.Boolean(False)
        interface_1.visible = bool_1
        assert not interface_1.visible
        assert interface_1._visible.variable_name == bool_1.variable_name

        interface_1.visible = True  # type: ignore
        assert interface_1.visible

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_visible_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface_1: _TestVisible = _TestVisible()
        interface_1.visible = ap.Boolean(True)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface_1.variable_name}.show();'
        )
        assert expected in expression

        expression_data_util.empty_expression()
        interface_1.visible = ap.Boolean(False)
        expression = expression_data_util.get_current_expression()
        expected = (
            f'{interface_1.variable_name}.hide();'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface_1: _TestVisible = _TestVisible()
        snapshot_name: str = interface_1._get_next_snapshot_name()
        interface_1._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert interface_1._visible_snapshots == {snapshot_name: True}

        interface_1.visible = ap.Boolean(False)
        interface_1._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert interface_1._visible_snapshots == {snapshot_name: True}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface_1: _TestVisible = _TestVisible()
        snapshot_name: str = interface_1._get_next_snapshot_name()
        interface_1._run_all_revert_methods(snapshot_name=snapshot_name)

        interface_1._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        interface_1.visible = ap.Boolean(False)
        interface_1._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface_1.visible

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_visible_attr_linking_setting(self) -> None:
        interface: _TestVisible = _TestVisible()
        interface._initialize_visible_if_not_initialized()
        assert interface._attr_linking_stack['visible'] == [True]
