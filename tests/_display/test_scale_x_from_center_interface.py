from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface


class _TestInterface(ScaleXFromCenterInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the ScaleXFromCenterInterface.
        """
        self.variable_name = 'scale_x_from_center_interface'


class TestScaleXFromCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_x_from_center_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_x_from_center_if_not_initialized()
        assert interface._scale_x_from_center == 1.0
        interface._scale_x_from_center._value = 0.5
        assert interface._scale_x_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_scale_x_from_center(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.scale_x_from_center == 1.0
        interface.scale_x_from_center = ap.Number(0.5)
        assert interface.scale_x_from_center == 0.5

        interface.scale_x_from_center = 0.3  # type: ignore
        assert interface.scale_x_from_center == 0.3
