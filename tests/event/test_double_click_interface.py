from apysc.event.double_click_interface import DoubleClickInterface


class TestDoubleClickInterface:

    def test__initialize_dbclick_handlers_if_not_initialized(self) -> None:
        interface_1: DoubleClickInterface = DoubleClickInterface()
        interface_1._initialize_dbclick_handlers_if_not_initialized()
        assert interface_1._dbclick_handlers == {}

        interface_1._initialize_dbclick_handlers_if_not_initialized()
