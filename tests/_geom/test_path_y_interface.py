from random import randint

from retrying import retry

from apysc._geom.path_y_interface import PathYInterface
import apysc as ap


class TestPathYInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_y(self) -> None:
        interface: PathYInterface = PathYInterface()
        interface._y = ap.Int(0)
        interface.y = ap.Int(20)
        assert interface.y == 20
