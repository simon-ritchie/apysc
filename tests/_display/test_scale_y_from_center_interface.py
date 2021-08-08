from apysc._expression import expression_file_util
from random import randint

from retrying import retry

import apysc as ap
from apysc._display.scale_y_from_center_interface import \
    ScaleYFromCenterInterface


class _TestInterface(ScaleYFromCenterInterface):

    def __init__(self) -> None:
        """
        The class for testing of the ScaleYFromCenterInterface.
        """
        self.variable_name = 'test_scale_y_from_center_interface'


class TestScaleYFromCenterInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_scale_y_from_center_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_y_from_center_if_not_initialized()
        assert interface._scale_y_from_center == 1.0
        interface._scale_y_from_center._value = 0.5
        interface._initialize_scale_y_from_center_if_not_initialized()
        assert interface._scale_y_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_scale_y_from_center(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.scale_y_from_center == 1.0
        interface.scale_y_from_center = ap.Number(0.5)
        assert interface.scale_y_from_center == 0.5

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_scale_y_from_center_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: _TestInterface = _TestInterface()
        num_1: ap.Number = ap.Number(0.5)
        num_2: ap.Number = ap.Number(0.3)
        interface.scale_y_from_center = num_1
        interface.scale_y_from_center = num_2
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.scale(1, 1 / {num_1.variable_name});'
            f'\n{interface.variable_name}.scale(1, {num_2.variable_name});'
        )
        assert expected in expression
