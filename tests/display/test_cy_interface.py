from random import randint

from retrying import retry

from apysc.display.cy_interface import CyInterface
from apysc import Int


class TestCyInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_cy_if_not_initialized(self) -> None:
        interface: CyInterface = CyInterface()
        interface._initialize_cy_if_not_initialized()
        assert interface._cy == 0

        interface._cy = Int(10)
        interface._initialize_cy_if_not_initialized()
        assert interface._cy == 10
