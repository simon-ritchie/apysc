import apysc as ap
from apysc._display.y_mixin import YMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import value_util


class TestYMixIn:
    @apply_test_settings()
    def test_y(self) -> None:
        y_mixin: YMixIn = YMixIn()
        y_mixin.variable_name = "test_y_mixin"
        y_mixin.y = ap.Number(200)
        assert y_mixin.y == 200

        y: ap.Number = y_mixin.y
        assert y == y_mixin._y
        assert y.variable_name != y_mixin.y.variable_name

    @apply_test_settings()
    def test__append_y_update_expression(self) -> None:
        y_mixin: YMixIn = YMixIn()
        expression_data_util.empty_expression()
        y_mixin.variable_name = "test_y_mixin"
        y_mixin.y = ap.Number(300)
        expression: str = expression_data_util.get_current_expression()
        value_str: str = value_util.get_value_str_for_expression(value=y_mixin._y)
        expected: str = f"test_y_mixin.y({value_str});"
        assert expected in expression

    @apply_test_settings()
    def test__initialize_y_if_not_initialized(self) -> None:
        y_mixin: YMixIn = YMixIn()
        y_mixin.variable_name = "test_y_mixin"
        y_mixin._initialize_y_if_not_initialized()
        assert y_mixin.y == 0

        y_mixin.y = ap.Number(100)
        y_mixin._initialize_y_if_not_initialized()
        assert y_mixin.y == 100

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        y_mixin: YMixIn = YMixIn()
        y_mixin.variable_name = "test_y_mixin"
        y_mixin.y = ap.Number(100)
        snapshot_name: str = "snapshot_1"
        y_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert y_mixin._y_snapshots[snapshot_name] == 100

        y_mixin.y = ap.Number(150)
        y_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert y_mixin._y_snapshots[snapshot_name] == 100

    @apply_test_settings()
    def test__revert(self) -> None:
        y_mixin: YMixIn = YMixIn()
        y_mixin.variable_name = "test_y_mixin"
        y_mixin.y = ap.Number(100)
        snapshot_name: str = "snapshot_1"
        y_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        y_mixin.y = ap.Number(150)
        y_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert y_mixin.y == 100

        y_mixin.y = ap.Number(150)
        y_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert y_mixin.y == 150

    @apply_test_settings()
    def test__append_y_attr_linking_setting(self) -> None:
        mixin: YMixIn = YMixIn()
        mixin.variable_name = "test_y_mixin"
        mixin._initialize_y_if_not_initialized()
        assert mixin._attr_linking_stack["y"] == [ap.Number(0)]

    @apply_test_settings()
    def test__update_y_and_skip_appending_exp(self) -> None:
        mixin: YMixIn = YMixIn()
        mixin._update_y_and_skip_appending_exp(y=100)
        assert mixin.y == 100
        assert isinstance(mixin.y, ap.Number)

        mixin._update_y_and_skip_appending_exp(y=ap.Number(200))
        assert mixin.y == 200
        assert isinstance(mixin.y, ap.Number)
