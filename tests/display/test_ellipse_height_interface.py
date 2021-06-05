from random import randint

from retrying import retry

from apysc import Int
from apysc.display.ellipse_height_interface import EllipseHeightInterface


class TestEllipseHeightInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ellipse_height_if_not_initialized(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface._initialize_ellipse_height_if_not_initialized()
        assert interface._ellipse_height == 0

        interface._ellipse_height = Int(10)
        interface._initialize_ellipse_height_if_not_initialized()
        assert interface._ellipse_height == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_ellipse_height(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface.variable_name = 'test_ellipse_height_interface'
        assert interface.ellipse_height == 0

        interface.ellipse_height = Int(10)
        assert interface.ellipse_height == 10

        interface.ellipse_height = 20  # type: ignore
        assert interface.ellipse_height == 20
