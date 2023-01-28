# pyright: reportUnusedExpression=false

import re
from random import randint
from typing import List
from typing import Match
from typing import Optional

import pytest
from retrying import retry

import apysc as ap
from apysc._display.points_2d_mixin import Points2DMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestPoints2DMixIn:
    @apply_test_settings()
    def test__initialize_points_if_not_initialized(self) -> None:
        mixin: Points2DMixIn = Points2DMixIn()
        mixin._initialize_points_if_not_initialized()
        assert mixin._points == []

        mixin._initialize_points_if_not_initialized()
        assert mixin._points == []

    @apply_test_settings()
    def test_points(self) -> None:
        mixin: Points2DMixIn = Points2DMixIn()
        mixin.variable_name = "test_point_2d_mixin"
        assert mixin.points == []

        mixin.points = ap.Array([ap.Point2D(10, 20), ap.Point2D(30, 40)])
        assert mixin.points == [ap.Point2D(10, 20), ap.Point2D(30, 40)]

        with pytest.raises(ValueError):  # type: ignore
            mixin.points = ap.Array([10, 20])  # type: ignore

    @apply_test_settings()
    def test__append_points_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: Points2DMixIn = Points2DMixIn()
        mixin.variable_name = "test_point_2d_mixin"
        mixin._initialize_points_if_not_initialized()
        pre_var_name: str = mixin.points.variable_name
        arr_1: ap.Array = ap.Array([ap.Point2D(10, 20)])
        mixin.points = arr_1
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{pre_var_name} = {arr_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: Points2DMixIn = Points2DMixIn()
        point_1: ap.Point2D = ap.Point2D(10, 20)
        mixin.points = ap.Array([point_1])
        mixin.variable_name = "test_point_2d_mixin"
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._points._value_snapshots == {snapshot_name: [point_1]}
        assert mixin._points_snapshots == {snapshot_name: ap.Array([point_1])}

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: Points2DMixIn = Points2DMixIn()
        mixin.variable_name = "test_point_2d_mixin"
        point_1: ap.Point2D = ap.Point2D(10, 20)
        mixin.points = ap.Array([point_1])
        snapshot_name: str = point_1._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)

        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.points = ap.Array([])  # type: ignore
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        mixin.points == [point_1]

    @apply_test_settings()
    def test__make_2dim_points_expression(self) -> None:
        mixin: Points2DMixIn = Points2DMixIn()
        mixin.variable_name = "test_point_2d_mixin"
        variable_name: str
        expression: str
        variable_name, expression = mixin._make_2dim_points_expression()
        expected_patterns: List[str] = [
            rf"var {variable_name} = \[\];",
            r"\nfor \(var i.+? \= 0\; i.+ \< .+?\.length\; i.+?\+\+\) \{",
            r"\n  var .+? = .+?\[i.+?\]\;",
            rf"\n  {variable_name}\.push\(\[.+?\[\"x\"\]\, .+?\[\"y\"\]\]\)",
            r"}",
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern, string=expression, flags=re.MULTILINE
            )
            assert match is not None, f"expected pattern: {expected_pattern}"
