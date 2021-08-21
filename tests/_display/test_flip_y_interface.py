from apysc._expression import expression_file_util
from random import randint

from retrying import retry

import apysc as ap
from apysc._display.flip_y_interface import FlipYInterface


class _TestInterface(FlipYInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the FlipYInterface.
        """
        self.variable_name = 'test_flip_y_interface'


class TestFlipYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_flip_y_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_flip_y_if_not_initialized()
        assert not interface._flip_y

        interface._flip_y._value = True
        interface._initialize_flip_y_if_not_initialized()
        assert interface._flip_y

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_flip_y(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert not interface.flip_y

        interface.flip_y = ap.Boolean(True)
        assert interface.flip_y

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_flip_y_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: _TestInterface = _TestInterface()
        interface.flip_y = ap.Boolean(True)
        expression: str = expression_file_util.get_current_expression()
        assert '.flip("y");' in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.flip_y = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._flip_y_snapshots[snapshot_name]

        interface.flip_y = ap.Boolean(False)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._flip_y_snapshots[snapshot_name]
