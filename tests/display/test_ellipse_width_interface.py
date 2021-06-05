from random import randint

from retrying import retry

from apysc.display.ellipse_width_interface import EllipseWidthInterface
from apysc.expression import expression_file_util
from apysc import Int


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

        interface.ellipse_width = Int(10)
        assert interface.ellipse_width == 10

        interface.ellipse_width = 20  # type: ignore
        assert interface.ellipse_width == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_width_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: EllipseWidthInterface = EllipseWidthInterface()
        interface.variable_name = 'test_ellipse_width_interface'
        ellipse_width: Int = Int(10)
        interface.ellipse_width = ellipse_width
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.radius({ellipse_width.variable_name}'
            ', 0);'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        ellipse_height: Int = Int(20)
        setattr(interface, '_ellipse_height', ellipse_height)
        interface.ellipse_width = ellipse_width
        expression = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.radius({ellipse_width.variable_name}'
            f', {ellipse_height.variable_name});'
        )
        assert expected in expression
