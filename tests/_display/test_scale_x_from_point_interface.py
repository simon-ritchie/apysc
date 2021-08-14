from apysc._expression import expression_file_util
from apysc._type.expression_string import ExpressionString
from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_point_interface import \
    ScaleXFromPointInterface
from apysc._display import scale_interface_helper


class _TestInterface(ScaleXFromPointInterface):

    def __init__(self) -> None:
        """
        The class for the testing for the `ScaleXFromPointInterface`
        class.
        """
        self.variable_name = 'scale_x_from_point_interface'


class TestScaleXFromPointInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_x_from_points_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_x_from_point_if_not_initialized()
        assert interface._scale_x_from_point == {}
        interface._scale_x_from_point['a'] = 10
        interface._initialize_scale_x_from_point_if_not_initialized()
        assert interface._scale_x_from_point == {'a': 10}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_get_scale_x_from_point(self) -> None:
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        interface: _TestInterface = _TestInterface()
        scale_x: ap.Number = interface.get_scale_x_from_point(
            x=x, y=y)
        assert scale_x == 1.0
        assert isinstance(scale_x, ap.Number)

        key_exp_str = scale_interface_helper.\
            get_point_key_for_expression(x=x, y=y)
        interface._scale_x_from_point[key_exp_str.value] = ap.Number(0.5)
        scale_x = interface.get_scale_x_from_point(x=x, y=y)
        assert scale_x == 0.5
        assert isinstance(scale_x, ap.Number)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_scale_x_from_point(self) -> None:
        interface: _TestInterface = _TestInterface()
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        interface.set_scale_x_from_point(
            scale_x=ap.Number(0.5), x=x, y=y)
        scale_x: ap.Number = interface.get_scale_x_from_point(x=x, y=y)
        assert scale_x == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_x_from_point_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        scale_x_1: ap.Number = ap.Number(0.5)
        scale_x_2: ap.Number = ap.Number(0.3)
        interface: _TestInterface = _TestInterface()
        interface.set_scale_x_from_point(scale_x=scale_x_1, x=x, y=y)
        interface.set_scale_x_from_point(scale_x=scale_x_2, x=x, y=y)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.scale(1 / {scale_x_1.variable_name}, '
            f'1, {x.variable_name}, {y.variable_name});'
            f'\n{interface.variable_name}.scale({scale_x_2.variable_name}, '
            f'1, {x.variable_name}, {y.variable_name});'
            f'\n'
        )
        assert expected in expression
