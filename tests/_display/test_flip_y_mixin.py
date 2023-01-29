import apysc as ap
from apysc._display.flip_y_mixin import FlipYMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class _TestInterface(FlipYMixIn):
    def __init__(self) -> None:
        """
        The class for the testing of the FlipYMixIn.
        """
        self.variable_name = "test_flip_y_interface"


class TestFlipYMixIn:
    @apply_test_settings()
    def test__initialize_flip_y_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_flip_y_if_not_initialized()
        assert not interface._flip_y

        interface._flip_y._value = True
        interface._initialize_flip_y_if_not_initialized()
        assert interface._flip_y

    @apply_test_settings()
    def test_flip_y(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert not interface.flip_y

        interface.flip_y = ap.Boolean(True)
        assert interface.flip_y

    @apply_test_settings()
    def test__append_flip_y_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestInterface = _TestInterface()
        interface.flip_y = ap.Boolean(True)
        expression: str = expression_data_util.get_current_expression()
        assert '.flip("y");' in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.flip_y = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._flip_y_snapshots[snapshot_name]

        interface.flip_y = ap.Boolean(False)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._flip_y_snapshots[snapshot_name]

    @apply_test_settings()
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.flip_y = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.flip_y = ap.Boolean(False)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.flip_y

        interface.flip_y = ap.Boolean(False)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not interface.flip_y

    @apply_test_settings()
    def test__append_flip_y_attr_linking_setting(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_flip_y_if_not_initialized()
        assert interface._attr_linking_stack["flip_y"] == [ap.Boolean(False)]
