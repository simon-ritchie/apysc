from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_x_interface import PathXInterface


class TestPathXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        interface: PathXInterface = PathXInterface()
        interface._x = ap.Int(10)
        assert interface.x == 10

        interface.x = ap.Int(20)
        assert interface.x == 20
