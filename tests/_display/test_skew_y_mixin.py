import apysc as ap
from apysc._display.skew_y_mixin import SkewYMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class _TestMixIn(SkewYMixIn):
    def __init__(self) -> None:
        """
        The class for the testing of the SkewYMixIn class.
        """
        self.variable_name = "test_skew_y_interface"


class TestSkewYMixIn:
    @apply_test_settings()
    def test__initialize_skew_y_if_not_initialized(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface._initialize_skew_y_if_not_initialized()
        assert interface._skew_y == 0

        interface._skew_y = ap.Int(10)
        interface._initialize_skew_y_if_not_initialized()
        assert interface._skew_y == 10

    @apply_test_settings()
    def test_skew_y(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        assert interface.skew_y == 0

        interface.skew_y = ap.Int(10)
        assert interface.skew_y == 10

    @apply_test_settings()
    def test__append_skew_y_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestMixIn = _TestMixIn()
        before_value: ap.Int = ap.Int(10)
        interface.skew_y = before_value
        after_value: ap.Int = ap.Int(20)
        interface.skew_y = after_value
        expression: str = expression_data_util.get_current_expression()
        interface_name: str = interface.variable_name
        expected: str = (
            f"{interface_name}.skew(0, -{before_value.variable_name});"
            f"\n{interface_name}.skew(0, {after_value.variable_name});"
            f"\n{before_value.variable_name} = {after_value.variable_name};"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.skew_y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if interface._skew_y_snapshot is None:
            raise AssertionError()
        assert interface._skew_y_snapshot[snapshot_name] == 10

        interface.skew_y = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._skew_y_snapshot[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.skew_y = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.skew_y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.skew_y == 10

        interface.skew_y = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.skew_y == 20

    @apply_test_settings()
    def test__append_skew_y_attr_linking_setting(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface._initialize_skew_y_if_not_initialized()
        assert interface._attr_linking_stack["skew_y"] == [ap.Int(0)]
