from random import randint

from retrying import retry

from apysc.display.ellipse_width_interface import EllipseWidthInterface


class TestEllipseWidthInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ellipse_width_if_not_initialized(self) -> None:
        interface: EllipseWidthInterface = EllipseWidthInterface()
        interface._initialize_ellipse_width_if_not_initialized()
        assert interface._ellipse_width == 0

        interface._ellipse_width.value = 10
        interface._initialize_ellipse_width_if_not_initialized()
        assert interface._ellipse_width == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_ellipse_width(self) -> None:
        interface: EllipseWidthInterface = EllipseWidthInterface()
        interface.variable_name = 'test_ellipse_width_interface'
        assert interface.ellipse_width == 0

        interface._ellipse_width.value = 10
        assert interface.ellipse_width == 10
