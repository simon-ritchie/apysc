from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_x2_interface import PathControlX2Interface


class TestPathControlX2Interface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_x2(self) -> None:
        interface: PathControlX2Interface = PathControlX2Interface()
        interface._control_x2 = ap.Int(0)
        interface.control_x2 = ap.Int(10)
        assert interface.control_x2 == 10
