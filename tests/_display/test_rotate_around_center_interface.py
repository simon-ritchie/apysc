from random import randint

from retrying import retry

from apysc._display.rotate_around_center_interface import \
    RotateAroundCenterInterface
from apysc._expression import expression_file_util


class TestRotateAroundCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_rotate_around_center(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: RotateAroundCenterInterface = RotateAroundCenterInterface()
        interface.variable_name = 'test_rotate_around_center_interface'

        interface.rotate_around_center(additional_rotation=10)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            'test_rotate_around_center_interface.rotate(10);'
        )
        assert expected in expression
