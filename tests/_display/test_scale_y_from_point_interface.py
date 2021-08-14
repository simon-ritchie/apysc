from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_y_from_point_interface import \
    ScaleYFromPointInterface


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
