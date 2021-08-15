from typing import Dict, List, Match, Optional
from apysc._expression import expression_file_util
from random import randint
import re

from retrying import retry

import apysc as ap
from apysc._display.scale_y_from_point_interface import \
    ScaleYFromPointInterface
from apysc._type.expression_string import ExpressionString
from apysc._display import scale_interface_helper


class _TestInterface(ScaleYFromPointInterface):

    def __init__(self) -> None:
        """
        Class for the testing of the `ScaleYFromPointInterface` class.
        """
        self.variable_name = 'test_scale_y_from_point_interface'


class TestScaleYFromPointInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_y_from_point_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_y_from_point_if_not_initialized()
        assert interface._scale_y_from_point == {}

        interface._scale_y_from_point['a'] = ap.Number(10)
        interface._initialize_scale_y_from_point_if_not_initialized()
        assert interface._scale_y_from_point == {'a': ap.Number(10)}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_get_scale_y_from_point(self) -> None:
        interface: _TestInterface = _TestInterface()
        scale_y: ap.Number = interface.get_scale_y_from_point(y=ap.Int(10))
        assert scale_y == 1.0

        key_exp_str: ExpressionString = scale_interface_helper.\
            get_coordinate_key_for_expression(coordinate=10)
        interface._scale_y_from_point[key_exp_str] = ap.Number(0.5)
        scale_y = interface.get_scale_y_from_point(y=ap.Int(10))
        assert scale_y == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_scale_y_from_point(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.set_scale_y_from_point(
            scale_y=ap.Number(0.5), y=ap.Int(100))
        scale_y: ap.Number = interface.get_scale_y_from_point(y=ap.Int(100))
        assert scale_y == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_y_from_point_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: _TestInterface = _TestInterface()
        scale_y: ap.Number = ap.Number(0.5)
        y: ap.Int = ap.Int(100)
        interface.set_scale_y_from_point(scale_y=scale_y, y=y)
        expression: str = expression_file_util.get_current_expression()
        patterns: List[str] = [
            rf'{interface.variable_name}'
            rf'\.scale\(1, 1 / .+?, 0, {y.variable_name}\);',
            rf'{interface.variable_name}'
            rf'.scale\(1, {scale_y.variable_name}, 0, {y.variable_name}\);',
        ]
        for pattern in patterns:
            match: Optional[Match] = re.search(
                pattern=pattern, string=expression, flags=re.MULTILINE)
            assert match is not None, (
                f'expression: {expression}\npattern: {pattern}')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface.set_scale_y_from_point(
            scale_y=ap.Number(0.5), y=ap.Int(100))
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        pre_dict: Dict[str, ap.Number] = {
            **interface._scale_y_from_point._value}
        assert interface._scale_y_from_point_snapshots == {
            snapshot_name: pre_dict}

        interface.set_scale_y_from_point(
            scale_y=ap.Number(0.3), y=ap.Int(100))
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._scale_y_from_point_snapshots == {
            snapshot_name: pre_dict}
