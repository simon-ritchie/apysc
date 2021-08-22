from random import randint

from retrying import retry

from apysc._expression import expression_file_util
from apysc._expression import var_names
from apysc._type.blank_object_interface import BlankObjectInterface


class TestBlankObjectInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_blank_object_if_not_initialized(self) -> None:
        expression_file_util.empty_expression()
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_blank_object_variable_name(self) -> None:
        interface: BlankObjectInterface = BlankObjectInterface()
        blank_object_variable_name: str = interface.blank_object_variable_name
        assert blank_object_variable_name.startswith(
            f'{var_names.BLANK_OBJECT}_'
        )
