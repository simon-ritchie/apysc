from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_control_y_interface import PathControlYInterface


class TestPathControlYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_control_y(self) -> None:
        interface: PathControlYInterface = PathControlYInterface()
        interface._control_y = ap.Int(0)
        interface.control_y = ap.Int(10)
        assert interface.control_y == 10
