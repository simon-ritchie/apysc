from random import randint

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
            get_point_key_for_expression(coordinate=10)
        interface._scale_y_from_point[key_exp_str] = ap.Number(0.5)
        scale_y = interface.get_scale_y_from_point(y=ap.Int(10))
        assert scale_y == 0.5
