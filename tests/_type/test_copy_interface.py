import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._type.copy_interface import CopyInterface


class TestCopyInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__copy(self) -> None:
        interface: CopyInterface = CopyInterface()
        interface.variable_name = 'test_copy_interface'
        interface._type_name = 'test_copy_interface'
        result: CopyInterface = interface._copy()
        assert result.variable_name.startswith('test_copy_interface_')
        assert result.variable_name != interface.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_copy_expression(self) -> None:
        expression_file_util.empty_expression()
        interface: CopyInterface = CopyInterface()
        interface.variable_name = 'test_copy_interface'
        interface._type_name = 'test_copy_interface'
        result: CopyInterface = interface._copy()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'cpy({interface.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_updating_cpy_exp_to_handler_scope(self) -> None:
        expression_file_util.empty_expression()
        int_1: ap.Int = ap.Int(10)
        with HandlerScope():
            int_2: ap.Int = int_1._copy()
        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        pattern: str = (
            rf'^{int_2.variable_name} = cpy\({int_1.variable_name}\);')
        match: Optional[Match] = re.search(
            pattern=pattern,
            string=expression, flags=re.MULTILINE)
        assert match is not None
