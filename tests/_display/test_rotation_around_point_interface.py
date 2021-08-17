from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_point_interface import \
    RotationAroundPointInterface
from apysc._expression import expression_file_util


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
