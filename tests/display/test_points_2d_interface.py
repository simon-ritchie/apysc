from random import randint

from retrying import retry

from apysc.display.points_2d_interface import Points2DInterface


class TestPoints2DInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_points_if_not_initialized(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        interface._initialize_points_if_not_initialized()
        assert interface._points == []

        interface._initialize_points_if_not_initialized()
        assert interface._points == []

    def test_points(self) -> None:
        interface: Points2DInterface = Points2DInterface()
        assert interface.points == []
