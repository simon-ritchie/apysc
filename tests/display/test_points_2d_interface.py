from random import randint
from typing import List, Match, Optional
import re

import pytest
from retrying import retry

from apysc import Array
from apysc import Point2D
from apysc.display.points_2d_interface import Points2DInterface
from apysc.expression import expression_file_util


class TestPoints2DInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_points_if_not_initialized(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        interface._initialize_points_if_not_initialized()
        assert interface._points == []

        interface._initialize_points_if_not_initialized()
        assert interface._points == []

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_points(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        interface.variable_name = 'test_point_2d_interface'
        assert interface.points == []

        interface.points = Array([Point2D(10, 20), Point2D(30, 40)])
        assert interface.points == [Point2D(10, 20), Point2D(30, 40)]

        with pytest.raises(ValueError):  # type: ignore
            interface.points = Array([10, 20])

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_points_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: Points2DInterface = Points2DInterface()
        interface.variable_name = 'test_point_2d_interface'
        interface._initialize_points_if_not_initialized()
        pre_var_name: str = interface.points.variable_name
        arr_1: Array = Array([Point2D(10, 20)])
        interface.points = arr_1
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{pre_var_name} = {arr_1.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        point_1: Point2D = Point2D(10, 20)
        interface.points = Array([point_1])
        interface.variable_name = 'test_point_2d_interface'
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._points._value_snapshots == {snapshot_name: [point_1]}
        assert interface._points_snapshots == {snapshot_name: Array([point_1])}

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        interface.variable_name = 'test_point_2d_interface'
        point_1: Point2D = Point2D(10, 20)
        interface.points = Array([point_1])
        snapshot_name: str = point_1._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.points = Array([])
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        interface.points == [point_1]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_make_2dim_points_expression(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        interface.variable_name = 'test_point_2d_interface'
        variable_name: str
        expression: str
        variable_name, expression = interface.make_2dim_points_expression()
        expected_patterns: List[str] = [
            rf'var {variable_name} = \[\];',
            r'\nfor \(var i.+? \= 0\; i.+ \< .+?\.length\; i.+?\+\+\) \{',
            r'\n  var .+? = .+?\[i.+?\]\;',
            rf'\n  {variable_name}\.push\(\[.+?\[\"x\"\]\, .+?\[\"y\"\]\]\)',
            r'}',
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern, string=expression,
                flags=re.MULTILINE)
            assert match is not None, f'expected pattern: {expected_pattern}'
