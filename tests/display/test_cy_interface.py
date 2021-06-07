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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        interface: CyInterface = CyInterface()
        interface.variable_name = 'test_cy_interface'
        assert interface.y == 0

        interface.y = Int(10)
        assert interface.y == 10

        interface.y = 20  # type: ignore
        assert interface.y == 20
