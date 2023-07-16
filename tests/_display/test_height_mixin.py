import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.height_mixin import HeightMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestHeightMixIn:
    @apply_test_settings()
    def test_height(self) -> None:
        height_mixin: HeightMixIn = HeightMixIn()
        height_mixin.variable_name = "test_height_mixin"
        height_mixin.height = ap.Int(200)
        assert height_mixin.height == 200

    @apply_test_settings()
    def test__append_height_update_expression(self) -> None:
        height_mixin: HeightMixIn = HeightMixIn()
        height_mixin.variable_name = "test_height_mixin"
        ap.Stage()
        height_mixin.height = ap.Int(300)
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(rf"test_height_mixin\.height\({var_names.INT}_.+?\);"),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__update_height_and_skip_appending_exp(self) -> None:
        height_mixin: HeightMixIn = HeightMixIn()
        ap.Stage()
        height_mixin._update_height_and_skip_appending_exp(value=ap.Int(300))
        assert height_mixin.height == 300

        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=r"height\(\d+?\)",
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is None

        height_mixin._update_height_and_skip_appending_exp(value=400)
        assert height_mixin.height == 400

    @apply_test_settings()
    def test__initialize_height_if_not_initialized(self) -> None:
        height_mixin: HeightMixIn = HeightMixIn()
        height_mixin.variable_name = "test_height_mixin"
        height_mixin._initialize_height_if_not_initialized()
        assert height_mixin.height == 0

        height_mixin.height = ap.Int(10)
        height_mixin._initialize_height_if_not_initialized()
        assert height_mixin.height == 10

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        height_mixin: HeightMixIn = HeightMixIn()
        height_mixin.variable_name = "test_height_mixin"
        height_mixin.height = ap.Int(10)
        snapshot_name: str = "snapshot_1"
        height_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if height_mixin._height_snapshots is None:
            raise AssertionError()
        assert height_mixin._height_snapshots[snapshot_name] == 10

        height_mixin.height = ap.Int(5)
        height_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert height_mixin._height_snapshots[snapshot_name] == 10

    @apply_test_settings()
    def test__revert(self) -> None:
        height_mixin: HeightMixIn = HeightMixIn()
        height_mixin.variable_name = "test_height_mixin"
        height_mixin.height = ap.Int(10)
        snapshot_name: str = "snapshot_1"
        height_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        height_mixin.height = ap.Int(5)
        height_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert height_mixin.height == 10

        height_mixin.height = ap.Int(5)
        height_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert height_mixin.height == 5

    @apply_test_settings()
    def test__append_height_attr_linking_setting(self) -> None:
        mixin: HeightMixIn = HeightMixIn()
        mixin.variable_name = "test_height_mixin"
        mixin._initialize_height_if_not_initialized()
        assert mixin._attr_linking_stack["height"] == [ap.Int(0)]
