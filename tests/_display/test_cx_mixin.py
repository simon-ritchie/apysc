# pyright: reportUnusedExpression=false

from random import randint

from retrying import retry

import apysc as ap
from apysc._display.cx_mixin import CxMixIn
from apysc._expression import expression_data_util


class TestCxMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_x_if_not_initialized(self) -> None:
        mixin: CxMixIn = CxMixIn()
        mixin._initialize_x_if_not_initialized()
        assert mixin._x == 0

        mixin._x = ap.Int(10)
        mixin._initialize_x_if_not_initialized()
        assert mixin._x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        mixin: CxMixIn = CxMixIn()
        mixin.variable_name = "test_x_mixin"
        assert mixin.x == 0

        mixin.x = ap.Int(10)
        assert mixin.x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: CxMixIn = CxMixIn()
        mixin.variable_name = "test_x_mixin"
        x: ap.Int = ap.Int(10)
        mixin.x = x
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.cx({x.variable_name});"
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: CxMixIn = CxMixIn()
        mixin.variable_name = "test_x_mixin"
        mixin.x = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._x_snapshots[snapshot_name] == 10

        mixin.x = ap.Int(20)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._x_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: CxMixIn = CxMixIn()
        mixin.variable_name = "test_x_mixin"
        mixin.x = ap.Int(10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.x = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.x == 10

        mixin.x = ap.Int(20)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.x == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_x_attr_linking_setting(self) -> None:
        mixin: CxMixIn = CxMixIn()
        mixin.variable_name = "test_x_mixin"
        mixin._initialize_x_if_not_initialized()
        mixin._attr_linking_stack["x"] == [ap.Int(0)]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_x_and_skip_appending_exp(self) -> None:
        mixin: CxMixIn = CxMixIn()
        mixin._update_x_and_skip_appending_exp(x=100)
        assert mixin.x == 100
        assert isinstance(mixin.x, ap.Int)

        mixin._update_x_and_skip_appending_exp(x=ap.Int(200))
        assert mixin.x == 200
        assert isinstance(mixin.x, ap.Int)
