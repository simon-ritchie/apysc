from random import randint

from retrying import retry

from apysc._display.rotation_around_center_interface import \
    RotationAroundCenterInterface
from apysc._expression import expression_file_util


class TestRotationAroundCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_rotation_around_center_if_not_initialized(
            self) -> None:
        interface: RotationAroundCenterInterface = \
            RotationAroundCenterInterface()
        interface._initialize_rotation_around_center_if_not_initialized()
        assert interface._rotation_around_center == 0
        interface._rotation_around_center._value = 10
        interface._initialize_rotation_around_center_if_not_initialized()
        assert interface._rotation_around_center == 10
