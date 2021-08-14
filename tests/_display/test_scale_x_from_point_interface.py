import re
from random import randint
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display import scale_interface_helper
from apysc._display.scale_x_from_point_interface import \
    ScaleXFromPointInterface
from apysc._expression import expression_file_util
from apysc._expression import var_names
from apysc._type.expression_string import ExpressionString


class _TestInterface(ScaleXFromPointInterface):

    def __init__(self) -> None:
        """
        The class for the testing for the `ScaleXFromPointInterface`
        class.
        """
        self.variable_name = 'scale_x_from_point_interface'


class TestScaleXFromPointInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_x_from_point_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_x_from_point_if_not_initialized()
        assert interface._scale_x_from_point == {}
        interface._scale_x_from_point['a'] = ap.Number(10)
        interface._initialize_scale_x_from_point_if_not_initialized()
        assert interface._scale_x_from_point == {'a': 10}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_get_scale_x_from_point(self) -> None:
        x: ap.Int = ap.Int(100)
        interface: _TestInterface = _TestInterface()
        scale_x: ap.Number = interface.get_scale_x_from_point(x=x)
        assert scale_x == 1.0
        assert isinstance(scale_x, ap.Number)

        key_exp_str: ExpressionString = scale_interface_helper.\
            get_coordinate_key_for_expression(
                coordinate=int(x._value))
        interface._scale_x_from_point[key_exp_str.value] = ap.Number(0.5)
        scale_x = interface.get_scale_x_from_point(x=x)
        assert scale_x == 0.5
        assert isinstance(scale_x, ap.Number)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_scale_x_from_point(self) -> None:
        interface: _TestInterface = _TestInterface()
        x: ap.Int = ap.Int(100)
        interface.set_scale_x_from_point(
            scale_x=ap.Number(0.5), x=x)
        scale_x: ap.Number = interface.get_scale_x_from_point(x=x)
        assert scale_x == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_x_from_point_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        x: ap.Int = ap.Int(100)
        scale_x_1: ap.Number = ap.Number(0.5)
        scale_x_2: ap.Number = ap.Number(0.3)
        interface: _TestInterface = _TestInterface()
        interface.set_scale_x_from_point(scale_x=scale_x_1, x=x)
        interface.set_scale_x_from_point(scale_x=scale_x_2, x=x)
        expression: str = expression_file_util.get_current_expression()
        key_exp_str: ExpressionString = scale_interface_helper.\
            get_coordinate_key_for_expression(coordinate=x)
        patterns: List[str] = [
            rf'if \(.+? in '
            rf'{interface._scale_x_from_point.variable_name}\) {{',
            rf'\n  var {var_names.NUMBER}_.+? = '
            rf'{interface._scale_x_from_point.variable_name}'
            rf'\[.+?\];',
            r'\n}else {',
            rf'\n  {var_names.NUMBER}_.+? = 1.0;',
            r'\n}',
            rf'\n{interface.variable_name}'
            rf'\.scale\(1 / {var_names.NUMBER}_.+?, ',
        ]
        for pattern in patterns:
            match: Optional[Match] = re.search(
                pattern=pattern,
                string=expression, flags=re.MULTILINE | re.DOTALL)
            assert match is not None, pattern
        expected = (
            f'\n{interface.variable_name}.scale({scale_x_2.variable_name}, '
            f'1, {x.variable_name}, 0);'
            f'\n{interface._scale_x_from_point.variable_name}'
            f'[{key_exp_str.value}] = {scale_x_2.variable_name};'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: _TestInterface = _TestInterface()
        x: ap.Int = ap.Int(100)
        interface.set_scale_x_from_point(scale_x=ap.Number(0.5), x=x)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        key_exp_str: ExpressionString = scale_interface_helper.\
            get_coordinate_key_for_expression(
                coordinate=int(x._value))
        assert interface._scale_x_from_point_snapshots[snapshot_name] == {
            key_exp_str.value: 0.5}

        interface.set_scale_x_from_point(scale_x=ap.Number(0.3), x=x)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._scale_x_from_point_snapshots[snapshot_name] == {
            key_exp_str.value: 0.5}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: _TestInterface = _TestInterface()
        x: ap.Int = ap.Int(100)
        interface.set_scale_x_from_point(scale_x=ap.Number(0.5), x=x)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.set_scale_x_from_point(scale_x=ap.Number(0.3), x=x)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.get_scale_x_from_point(x=x) == 0.5

        interface.set_scale_x_from_point(scale_x=ap.Number(0.3), x=x)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.get_scale_x_from_point(x=x) == 0.3
