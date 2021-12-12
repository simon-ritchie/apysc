from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_y1_interface import PathControlY1Interface


class TestPathControlY1Interface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_y1(self) -> None:
        interface: PathControlY1Interface = PathControlY1Interface()
        interface._control_y1 = ap.Int(0)
        interface.control_y1 = ap.Int(10)
        assert interface.control_y1 == 10
