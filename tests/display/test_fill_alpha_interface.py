from random import randint

from retrying import retry

from apyscript.display.fill_alpha_interface import FillAlphaInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class TestFillAlphaInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_fill_alpha(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        fill_alpha_interface.fill_alpha = 0.5
        assert fill_alpha_interface.fill_alpha == 0.5

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_fill_alpha_update_expression(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        expression_file_util.remove_expression_file()
        fill_alpha_interface.fill_alpha = 0.3
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_fill_alpha_interface.fill({opacity: 0.3});'
        expected = html_util.wrap_expression_by_script_tag(
            expression=expected)
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_update_fill_alpha_and_skip_appending_exp(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        expression_file_util.remove_expression_file()
        fill_alpha_interface.update_fill_alpha_and_skip_appending_exp(
            value=0.25)
        assert fill_alpha_interface.fill_alpha == 0.25
        expression: str = expression_file_util.get_current_expression()
        assert expression == ''
