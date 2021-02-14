from random import randint

from retrying import retry

from apyscript.display.height_interface import HeightInterface
from apyscript.expression import expression_file_util
from apyscript.html import html_util


class TestHeightInterface:

    def test_height(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        height_interface.height = 200
        assert height_interface.height == 200

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_height_update_expression(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        height_interface.variable_name = 'test_height_interface'
        expression_file_util.remove_current_scope_expression_file()
        height_interface.height = 300
        expression: str = expression_file_util.get_current_scope_expression()
        expected: str = (
            f'test_height_interface.height(300);'
        )
        expected = html_util.wrap_expression_by_script_tag(
            expression=expected)
        assert expected in expression

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_update_height_and_skip_appending_exp(self) -> None:
        height_interface: HeightInterface = HeightInterface()
        expression_file_util.remove_current_scope_expression_file()
        height_interface.update_height_and_skip_appending_exp(value=300)
        assert height_interface.height == 300

        expression: str = expression_file_util.get_current_scope_expression()
        assert expression == ''
