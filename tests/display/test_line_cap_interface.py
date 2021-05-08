from random import randint

from retrying import retry

from apysc.display.line_cap_interface import LineCapInterface
from apysc import LineCaps, String


class TestLineCapInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_cap_if_not_initialized(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == LineCaps.BUTT.value

        interface._line_cap = String(LineCaps.ROUND.value)
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == LineCaps.ROUND.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_cap(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        assert interface.line_cap == LineCaps.BUTT.value

        interface.line_cap = LineCaps.ROUND
        assert interface.line_cap == LineCaps.ROUND.value
