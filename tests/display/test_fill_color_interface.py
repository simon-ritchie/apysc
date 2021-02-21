from random import randint

from retrying import retry

from apyscript.display.fill_color_interface import FillColorInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class TestFillColorInterface:

    def test_fill_color(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface.fill_color = '#333'
        assert fill_color_interface.fill_color == '#333333'

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_fill_color_update_expression(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        expression_file_util.remove_expression_file()
        fill_color_interface.fill_color = '#666'
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_fill_color_interface.fill("#666666");'
        expected = html_util.wrap_expression_by_script_tag(
            expression=expected)
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_update_fill_color_and_skip_appending_exp(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        expression_file_util.remove_expression_file()
        fill_color_interface.update_fill_color_and_skip_appending_exp(
            value='#333')
        assert fill_color_interface.fill_color == '#333333'
        expression: str = expression_file_util.get_current_expression()
        assert expression == ''
