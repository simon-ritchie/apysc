from apysc.display.line_cap_interface import LineCapInterface
from apysc import LineCaps


class TestLineCapInterface:

    def test__initialize_line_cap_if_not_initialized(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == LineCaps.BUTT

        interface._line_cap = LineCaps.ROUND
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == LineCaps.ROUND
