from random import randint

from retrying import retry

import apysc as ap
from apysc._display.flip_x_interface import FlipXInterface


class _TestInterface(FlipXInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the FlipXInterface class.
        """
        self.variable_name = 'test_flip_x_interface'


class TestFlipXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_flip_x_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_flip_x_if_not_initialized()
        assert interface._flip_x == False

        interface._flip_x._value = True
        interface._initialize_flip_x_if_not_initialized()
        assert interface._flip_x == True

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_flip_x(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert not interface.flip_x

        interface._flip_x._value = True
        assert interface.flip_x
