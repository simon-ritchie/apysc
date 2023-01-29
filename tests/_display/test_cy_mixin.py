import apysc as ap
from apysc._display.cy_mixin import CyMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestCyMixIn:
    @apply_test_settings()
    def test__initialize_y_if_not_initialized(self) -> None:
        mixin: CyMixIn = CyMixIn()
        mixin._initialize_y_if_not_initialized()
        assert mixin._y == 0

        mixin._y = ap.Int(10)
        mixin._initialize_y_if_not_initialized()
        assert mixin._y == 10

    @apply_test_settings()
    def test_y(self) -> None:
        mixin: CyMixIn = CyMixIn()
        mixin.variable_name = "test_y_mixin"
        assert mixin.y == 0

        mixin.y = ap.Int(10)
        assert mixin.y == 10

    @apply_test_settings()
    def test__append_y_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: CyMixIn = CyMixIn()
        mixin.variable_name = "test_y_mixin"
        y: ap.Int = ap.Int(10)
        mixin.y = y
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.cy({y.variable_name});"
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: CyMixIn = CyMixIn()
        mixin.variable_name = "test_y_mixin"
        mixin.y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._y_snapshots[snapshot_name] == 10

        mixin.y = ap.Int(20)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._y_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: CyMixIn = CyMixIn()
        mixin.variable_name = "test_y_mixin"
        mixin.y = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.y = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.y == 10

        mixin.y = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.y == 20

    @apply_test_settings()
    def test__append_y_attr_linking_setting(self) -> None:
        mixin: CyMixIn = CyMixIn()
        mixin.variable_name = "test_y_mixin"
        mixin._initialize_y_if_not_initialized()
        assert mixin._attr_linking_stack["y"] == [ap.Int(0)]

    @apply_test_settings()
    def test__update_y_and_skip_appending_exp(self) -> None:
        mixin: CyMixIn = CyMixIn()
        mixin._update_y_and_skip_appending_exp(y=100)
        assert mixin.y == 100
        assert isinstance(mixin.y, ap.Int)

        mixin._update_y_and_skip_appending_exp(y=ap.Int(200))
        assert mixin.y == 200
        assert isinstance(mixin.y, ap.Int)
