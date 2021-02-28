from random import randint

from retrying import retry

from apyscript.expression import expression_file_util
from apyscript.type.copy_interface import CopyInterface


class TestCopyInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__copy(self) -> None:
        interface: CopyInterface = CopyInterface()
        interface.variable_name = 'test_copy_interface'
        interface._type_name = 'test_copy_interface'
        result: CopyInterface = interface._copy()
        assert result.variable_name.startswith('test_copy_interface_')
        assert result.variable_name != interface.variable_name

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test__append_copy_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: CopyInterface = CopyInterface()
        interface.variable_name = 'test_copy_interface'
        interface._type_name = 'test_copy_interface'
        result: CopyInterface = interface._copy()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = {interface.variable_name};'
        )
        assert expected in expression
