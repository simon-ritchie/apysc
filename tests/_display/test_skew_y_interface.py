from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_y_interface import SkewYInterface


class _TestInterface(SkewYInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the SkewYInterface class.
        """
        self.variable_name = 'test_skew_y_interface'


class TestSkewYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_skew_y_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_skew_y_if_not_initialized()
        assert interface._skew_y == 0

        interface._skew_y = ap.Int(10)
        interface._initialize_skew_y_if_not_initialized()
        assert interface._skew_y == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_skew_y(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.skew_y == 0

        interface.skew_y = ap.Int(10)
        assert interface.skew_y == 10
