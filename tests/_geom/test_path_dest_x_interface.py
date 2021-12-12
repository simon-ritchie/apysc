from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.path_dest_x_interface import PathDestXInterface


class TestPathDestXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dest_x(self) -> None:
        interface: PathDestXInterface = PathDestXInterface()
        interface._dest_x = ap.Int(0)
        interface.dest_x = ap.Int(10)
        assert interface.dest_x == 10
