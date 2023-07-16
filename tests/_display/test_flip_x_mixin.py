import apysc as ap
from apysc._display.flip_x_mixin import FlipXMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class _TestMixIn(FlipXMixIn):
    def __init__(self) -> None:
        """
        The class for the testing of the FlipXMixIn class.
        """
        self.variable_name = "test_flip_x_interface"


class TestFlipXMixIn:
    @apply_test_settings()
    def test__initialize_flip_x_if_not_initialized(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface._initialize_flip_x_if_not_initialized()
        assert not interface._flip_x

        interface._flip_x._value = True
        interface._initialize_flip_x_if_not_initialized()
        assert interface._flip_x

    @apply_test_settings()
    def test_flip_x(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        assert not interface.flip_x

        interface.flip_x = ap.Boolean(True)
        assert interface.flip_x

    @apply_test_settings()
    def test__append_flip_x_update_expression(self) -> None:
        ap.Stage()
        interface: _TestMixIn = _TestMixIn()
        flip_x_1: ap.Boolean = ap.Boolean(True)
        flip_x_2: ap.Boolean = ap.Boolean(False)
        interface.flip_x = flip_x_1
        interface.flip_x = flip_x_2
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"if ({flip_x_1.variable_name}) {{"
            f'\n  {interface.variable_name}.flip("x");'
            "\n}"
            f"\nif ({flip_x_2.variable_name}) {{"
            f'\n  {interface.variable_name}.flip("x");'
            "\n}"
            f"\n{flip_x_1.variable_name} = {flip_x_2.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.flip_x = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if interface._flip_x_snapshots is None:
            raise AssertionError()
        assert interface._flip_x_snapshots[snapshot_name]

        interface.flip_x = ap.Boolean(False)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._flip_x_snapshots[snapshot_name]

    @apply_test_settings()
    def test__revert(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.flip_x = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.flip_x = ap.Boolean(False)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.flip_x

        interface.flip_x = ap.Boolean(False)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not interface.flip_x

    @apply_test_settings()
    def test__append_flip_x_attr_linking_setting(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface._initialize_flip_x_if_not_initialized()
        assert interface._attr_linking_stack["flip_x"] == [ap.Boolean(False)]
