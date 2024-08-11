# pyright: reportUnusedExpression=false

import re
from typing import List
from typing import Match
from typing import Optional

import pytest

import apysc as ap
from apysc._display.points_2d_mixin import Points2DMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_attr_or_var_mixin import (
    VariableNameSuffixAttrOrVarMixIn,
)
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class _TestObject(
    Points2DMixIn,
    VariableNameMixIn,
    VariableNameSuffixMixIn,
    VariableNameSuffixAttrOrVarMixIn,
):
    pass


class TestPoints2DMixIn:
    @apply_test_settings()
    def test__initialize_points_if_not_initialized(self) -> None:
        instance: _TestObject = _TestObject()
        instance._initialize_points_if_not_initialized()
        assert instance._points == []

        instance._initialize_points_if_not_initialized()
        assert instance._points == []

    @apply_test_settings()
    def test_points(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_point_2d_mixin"
        assert instance.points == []

        instance.points = ap.Array([ap.Point2D(10, 20), ap.Point2D(30, 40)])
        assert instance.points == [ap.Point2D(10, 20), ap.Point2D(30, 40)]

        with pytest.raises(ValueError):  # type: ignore
            instance.points = ap.Array([10, 20])  # type: ignore

    @apply_test_settings()
    def test__append_points_update_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_point_2d_mixin"
        instance._initialize_points_if_not_initialized()
        pre_var_name: str = instance.points.variable_name
        arr_1: ap.Array = ap.Array([ap.Point2D(10, 20)])
        instance.points = arr_1
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{pre_var_name} = {arr_1.variable_name};"
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        instance: _TestObject = _TestObject()
        point_1: ap.Point2D = ap.Point2D(10, 20)
        instance.points = ap.Array([point_1])
        instance.variable_name = "test_point_2d_mixin"
        snapshot_name: str = instance._get_next_snapshot_name()
        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert instance._points._value_snapshots == {snapshot_name: [point_1]}
        assert instance._points_snapshots == {snapshot_name: ap.Array([point_1])}

        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    @apply_test_settings()
    def test__revert(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_point_2d_mixin"
        point_1: ap.Point2D = ap.Point2D(10, 20)
        instance.points = ap.Array([point_1])
        snapshot_name: str = point_1._get_next_snapshot_name()
        instance._run_all_revert_methods(snapshot_name=snapshot_name)

        instance._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        instance.points = ap.Array([])  # type: ignore
        instance._run_all_revert_methods(snapshot_name=snapshot_name)
        instance.points == [point_1]

    @apply_test_settings()
    def test__make_2dim_points_expression(self) -> None:
        instance: _TestObject = _TestObject()
        instance.variable_name = "test_point_2d_mixin"
        variable_name: str
        expression: str
        variable_name, expression = instance._make_2dim_points_expression()
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
