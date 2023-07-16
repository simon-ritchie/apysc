import apysc as ap
from apysc._display.x_mixin import XMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import value_util


class TestXMixIn:
    @apply_test_settings()
    def test_x(self) -> None:
        x_mixin = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin.x = ap.Number(100)
        assert x_mixin.x == 100

        x: ap.Number = x_mixin.x
        assert x == x_mixin._x
        assert x.variable_name != x_mixin._x.variable_name

    @apply_test_settings()
    def test__append_x_update_expression(self) -> None:
        x_mixin = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        ap.Stage()
        x_mixin.x = ap.Number(200)
        expression: str = expression_data_util.get_current_expression()
        value_str: str = value_util.get_value_str_for_expression(value=x_mixin._x)
        expected: str = f"test_x_mixin.x({value_str});"
        assert expected in expression

    @apply_test_settings()
    def test__initialize_x_if_not_initialized(self) -> None:
        x_mixin = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin._initialize_x_if_not_initialized()
        assert x_mixin.x == 0

        x_mixin.x = ap.Number(100)
        x_mixin._initialize_x_if_not_initialized()
        assert x_mixin.x == 100

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        x_mixin = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin.x = ap.Number(100)
        snapshot_name: str = "snapshot_1"
        x_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if x_mixin._x_snapshots is None:
            raise AssertionError()
        assert x_mixin._x_snapshots[snapshot_name] == 100

        x_mixin.x = ap.Number(150)
        x_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert x_mixin._x_snapshots[snapshot_name] == 100

    @apply_test_settings()
    def test__revert(self) -> None:
        x_mixin = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin.x = ap.Number(100)
        snapshot_name: str = "snapshot_1"
        x_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        x_mixin.x = ap.Number(150)
        x_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert x_mixin.x == 100

        x_mixin.x = ap.Number(150)
        x_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert x_mixin.x == 150

    @apply_test_settings()
    def test__append_x_attr_linking_setting(self) -> None:
        x_mixin = XMixIn()
        x_mixin.variable_name = "test_x_mixin"
        x_mixin._initialize_x_if_not_initialized()
        assert x_mixin._attr_linking_stack["x"] == [ap.Number(0)]

    @apply_test_settings()
    def test__update_x_and_skip_appending_exp(self) -> None:
        x_mixin = XMixIn()
        x_mixin._update_x_and_skip_appending_exp(x=100)
        assert x_mixin.x == 100
        assert isinstance(x_mixin.x, ap.Number)

        x_mixin._update_x_and_skip_appending_exp(x=ap.Number(200))
        assert x_mixin.x == 200
        assert isinstance(x_mixin.x, ap.Number)
