from random import randint
from typing import List, Match, Optional
import re

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_point_interface import \
    RotationAroundPointInterface
from apysc._expression import expression_file_util
from apysc._type.expression_string import ExpressionString
from apysc._display import rotation_interface_helper
from apysc._expression import var_names


class _TestInterface(RotationAroundPointInterface):

    def __init__(self) -> None:
        """
        The class for the testing.
        """
        self.variable_name = 'test_rotation_around_point_interface'


class TestRotationAroundPointInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_rotate_around_point(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: _TestInterface = _TestInterface()
        additional_rotation: ap.Int = ap.Int(10)
        x: ap.Int = ap.Int(20)
        y: ap.Int = ap.Int(30)
        interface.rotate_around_point(
            additional_rotation=additional_rotation, x=x, y=y)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.rotate('
            f'{additional_rotation.variable_name}, '
            f'{x.variable_name}, {y.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_rotation_around_point_if_not_initialized(
            self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_rotation_around_point_if_not_initialized()
        assert interface._rotation_around_point == {}

        interface._rotation_around_point['a'] = ap.Int(10)
        interface._initialize_rotation_around_point_if_not_initialized()
        assert interface._rotation_around_point == {'a': ap.Int(10)}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_get_rotation_around_point(self) -> None:
        interface: _TestInterface = _TestInterface()
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        rotation: ap.Int = interface.get_rotation_around_point(x=x, y=y)
        assert rotation == 0

        key_exp_str: ExpressionString = rotation_interface_helper.\
            get_coordinates_key_for_expression(x=100, y=200)
        interface._rotation_around_point[key_exp_str.value] = ap.Int(50)
        rotation = interface.get_rotation_around_point(x=x, y=y)
        assert rotation == 50

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_rotation_around_point(self) -> None:
        interface: _TestInterface = _TestInterface()
        rotation: ap.Int = ap.Int(50)
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        interface.set_rotation_around_point(rotation=rotation, x=x, y=y)
        rotation = interface.get_rotation_around_point(x=x, y=y)
        assert rotation == 50

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_rotation_around_point_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: _TestInterface = _TestInterface()
        rotation: ap.Int = ap.Int(50)
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        key_exp_str: ExpressionString = rotation_interface_helper.\
            get_coordinates_key_for_expression(x=x, y=y)
        key_exp_value: str= key_exp_str.value
        key_exp_value = key_exp_value.replace('(', '\\(')
        key_exp_value = key_exp_value.replace(')', '\\)')
        key_exp_value = key_exp_value.replace('+', '\\+')
        interface.set_rotation_around_point(rotation=rotation, x=x, y=y)
        expression: str = expression_file_util.get_current_expression()
        patterns: List[str] = [
            rf'if \({key_exp_value} in '
            rf'{interface._rotation_around_point.variable_name}\) {{',
            rf'\n  var {var_names.INT}_.+? = '
            rf'{interface._rotation_around_point.variable_name}\['
            rf'{key_exp_value}\];',
            r'\n}else {'
            rf'\n  {var_names.INT}_.+? = 0;',
            r'\n}',
            rf'\n{interface.variable_name}\.rotate\('
            rf'-{var_names.INT}_.+?, {x.variable_name}, {y.variable_name}\);',
            rf'\n{interface.variable_name}\.rotate\('
            rf'{rotation.variable_name}, {x.variable_name}, '
            rf'{y.variable_name}\);',
            rf'\n{interface._rotation_around_point.variable_name}\['
            rf'{key_exp_value}\] = {rotation.variable_name};'
        ]
        for i, pattern in enumerate(patterns):
            match: Optional[Match] = re.search(
                pattern=pattern,
                string=expression,
                flags=re.MULTILINE | re.DOTALL)
            assert match is not None, \
                f'index: {i}, \n{expression}\n\n{pattern}'
