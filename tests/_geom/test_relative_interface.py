from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.relative_interface import RelativeInterface


class TestRelativeInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_relative(self) -> None:
        interface: RelativeInterface = RelativeInterface()
        interface._relative = ap.Boolean(False)
        interface.relative = ap.Boolean(True)
        assert interface.relative
