from random import randint

from retrying import retry

from apysc.display.ellipse_size_interface import EllipseSizeInterface
from apysc import Int


class TestEllipseSizeInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ellipse_size_if_not_initialized(self) -> None:
        interface: EllipseSizeInterface = EllipseSizeInterface()
        interface._initialize_ellipse_size_if_not_initialized()
        assert interface._ellipse_size == 0

        interface._ellipse_size.value = 10
        interface._initialize_ellipse_size_if_not_initialized()
        assert interface._ellipse_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_ellipse_size(self) -> None:
        interface: EllipseSizeInterface = EllipseSizeInterface()
        assert interface.ellipse_size == 0

        interface.ellipse_size = Int(10)
        assert interface.ellipse_size == 10

        interface.ellipse_size = 20  # type: ignore
        assert interface.ellipse_size == 20
