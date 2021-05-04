from apysc.display.points_2d_interface import Points2DInterface


class TestPoints2DInterface:

    def test__initialize_points_if_not_initialized(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        interface._initialize_points_if_not_initialized()
        assert interface._points == []

        interface._initialize_points_if_not_initialized()
        assert interface._points == []
