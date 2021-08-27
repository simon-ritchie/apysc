from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_x_interface import SkewXInterface


class _TestInterface(SkewXInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the SkewXInterface.
        """
        self.variable_name = 'test_skew_x_interface'


class TestSkewXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_skew_x_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_skew_x_if_not_initialized()
        assert interface._skew_x == 0

        interface._skew_x = ap.Int(10)
        interface._initialize_skew_x_if_not_initialized()
        assert interface._skew_x == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_skew_x(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.skew_x == 0

        interface.skew_x = ap.Int(10)
        assert interface.skew_x == 10
