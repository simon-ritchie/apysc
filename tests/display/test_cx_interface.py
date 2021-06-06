from random import randint

from retrying import retry

from apysc.display.cx_interface import CxInterface
from apysc import Int


class TestCxInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_cx_if_not_initialized(self) -> None:
        interface: CxInterface = CxInterface()
        interface._initialize_cx_if_not_initialized()
        assert interface._cx == 0

        interface._cx = Int(10)
        interface._initialize_cx_if_not_initialized()
        assert interface._cx == 10
