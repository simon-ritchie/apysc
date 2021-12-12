from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_x_interface import PathControlXInterface


class TestPathControlXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_x(self) -> None:
        interface: PathControlXInterface = PathControlXInterface()
        interface._control_x = ap.Int(0)
        interface.control_x = ap.Int(10)
        assert interface.control_x == 10
