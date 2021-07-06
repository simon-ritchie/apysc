from random import randint

from retrying import retry

from apysc._type.blank_object_interface import BlankObjectInterface
from apysc._expression import var_names, expression_file_util


class TestBlankObjectInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_blank_object_if_not_initialized(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: BlankObjectInterface = BlankObjectInterface()
        interface._initialize_blank_object_if_not_initialized()
        assert interface._initialize_blank_object_if_not_initialized
        assert interface._blank_object_variable_name.startswith(
            f'{var_names.BLANK_OBJECT}_')
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {interface._blank_object_variable_name} = {{}};'
        )
        assert expected in expression
