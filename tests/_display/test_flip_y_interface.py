from random import randint

from retrying import retry

from apysc._display.flip_y_interface import FlipYInterface


class _TestInterface(FlipYInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the FlipYInterface.
        """
        self.variable_name = 'test_flip_y_interface'


class TestFlipYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_flip_y_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_flip_y_if_not_initialized()
        assert not interface._flip_y

        interface._flip_y._value = True
        interface._initialize_flip_y_if_not_initialized()
        assert interface._flip_y
