import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_thickness_mixin import LineThicknessMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names


class TestLineThicknessMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_thickness(self) -> None:
        line_thickness_mixin: LineThicknessMixIn = LineThicknessMixIn()
        line_thickness_mixin.variable_name = "test_line_thickness_mixin"
        line_thickness_mixin.line_thickness = ap.Int(3)
        assert line_thickness_mixin.line_thickness == 3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_thickness_update_expression(self) -> None:
        line_thickness_mixin: LineThicknessMixIn = LineThicknessMixIn()
        line_thickness_mixin.variable_name = "test_line_thickness_mixin"
        expression_data_util.empty_expression()
        line_thickness_mixin.line_thickness = ap.Int(2)
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_line_thickness_mixin\.attr"
                rf'\({{"stroke-width": {var_names.INT}_.+?}}\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_thickness_and_skip_appending_exp(self) -> None:
        line_thickness_mixin: LineThicknessMixIn = LineThicknessMixIn()
        line_thickness_mixin.variable_name = "test_line_thickness_mixin"
        expression_data_util.empty_expression()
        line_thickness_mixin._update_line_thickness_and_skip_appending_exp(
            value=ap.Int(5)
        )
        assert line_thickness_mixin.line_thickness == 5
        expression: str = expression_data_util.get_current_expression()
        assert "stroke-width" not in expression

        line_thickness_mixin._update_line_thickness_and_skip_appending_exp(value=6)
        assert line_thickness_mixin.line_thickness == 6

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_thickness_if_not_initialized(self) -> None:
        line_thickness_mixin: LineThicknessMixIn = LineThicknessMixIn()
        line_thickness_mixin.variable_name = "test_line_thickness_mixin"
        line_thickness_mixin._initialize_line_thickness_if_not_initialized()
        assert line_thickness_mixin.line_thickness == 1

        line_thickness_mixin.line_thickness = ap.Int(2)
        line_thickness_mixin._initialize_line_thickness_if_not_initialized()
        assert line_thickness_mixin.line_thickness == 2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        line_thickness_mixin: LineThicknessMixIn = LineThicknessMixIn()
        line_thickness_mixin.variable_name = "test_line_thickness_mixin"
        line_thickness_mixin.line_thickness = ap.Int(3)
        snapshot_name: str = "snapshot_1"
        line_thickness_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert line_thickness_mixin._line_thickness_snapshots[snapshot_name] == 3

        line_thickness_mixin.line_thickness = ap.Int(2)
        line_thickness_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert line_thickness_mixin._line_thickness_snapshots[snapshot_name] == 3

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        line_thickness_mixin: LineThicknessMixIn = LineThicknessMixIn()
        line_thickness_mixin.variable_name = "test_line_thickness_mixin"
        line_thickness_mixin.line_thickness = ap.Int(3)
        snapshot_name: str = "snapshot_1"
        line_thickness_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        line_thickness_mixin.line_thickness = ap.Int(2)
        line_thickness_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert line_thickness_mixin.line_thickness == 3

        line_thickness_mixin.line_thickness = ap.Int(2)
        line_thickness_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert line_thickness_mixin.line_thickness == 2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_thickness_attr_linking_setting(self) -> None:
        mixin: LineThicknessMixIn = LineThicknessMixIn()
        mixin.variable_name = "test_line_thickness_mixin"
        mixin._initialize_line_thickness_if_not_initialized()
        assert mixin._attr_linking_stack["line_thickness"] == [ap.Int(1)]
