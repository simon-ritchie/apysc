from random import randint

from retrying import retry

from apysc._geom.path_control_x1_interface import PathControlX1Interface
import apysc as ap


class TestPathControlX1Interface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_x1(self) -> None:
        interface: PathControlX1Interface = PathControlX1Interface()
        interface._control_x1 = ap.Int(0)
        interface.control_x1 = ap.Int(10)
        assert interface.control_x1 == 10
