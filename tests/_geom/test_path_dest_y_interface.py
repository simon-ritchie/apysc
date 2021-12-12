from random import randint

from retrying import retry

from apysc._geom.path_dest_y_interface import PathDestYInterface
import apysc as ap


class TestPathDestYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_dest_y(self) -> None:
        interface: PathDestYInterface = PathDestYInterface()
        interface._dest_y = ap.Int(0)
        interface.dest_y = ap.Int(10)
        assert interface.dest_y == 10
