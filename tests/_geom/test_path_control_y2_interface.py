from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_y2_interface import PathControlY2Interface


class TestPathControlY2Interface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_y2(self) -> None:
        interface: PathControlY2Interface = PathControlY2Interface()
        interface._control_y2 = ap.Int(0)
        interface.control_y2 = ap.Int(10)
        assert interface.control_y2 == 10
