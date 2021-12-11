from random import randint

from retrying import retry

from apysc._geom.path_x_interface import PathXInterface
import apysc as ap


class TestPathXInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_x(self) -> None:
        interface: PathXInterface = PathXInterface()
        interface._x = ap.Int(10)
        x: ap.Int = interface.x
        assert x == 10
