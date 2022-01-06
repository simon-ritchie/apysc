import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression.event_handler_scope import HandlerScope
from apysc._type.copy_interface import CopyInterface
from apysc._type.variable_name_interface import VariableNameInterface


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
        expression_data_util.empty_expression()
        interface: CopyInterface = CopyInterface()
        interface.variable_name = 'test_copy_interface'
        interface._type_name = 'test_copy_interface'
        result: CopyInterface = interface._copy()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{result.variable_name} = '
            f'cpy({interface.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_value_updating_cpy_exp_to_handler_scope(self) -> None:
        expression_data_util.empty_expression()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_instance'
        int_1: ap.Int = ap.Int(10)
        with HandlerScope(handler_name='test_handler_1', instance=instance):
            int_2: ap.Int = int_1._copy()
        expression: str = \
            expression_data_util.get_current_event_handler_scope_expression()
        pattern: str = (
            rf'^{int_2.variable_name} = {int_1.variable_name};')
        match: Optional[Match] = re.search(
            pattern=pattern,
            string=expression, flags=re.MULTILINE)
        assert match is not None

        expression_data_util.empty_expression()
        arr_1: ap.Array = ap.Array([1, 2, 3])
        with HandlerScope(handler_name='test_handler_1', instance=instance):
            arr_2: ap.Array = arr_1._copy()
        expression = \
            expression_data_util.get_current_event_handler_scope_expression()
        pattern = (
            rf'^{arr_2.variable_name} = cpy\({arr_1.variable_name}\);'
        )
        match = re.search(
            pattern=pattern,
            string=expression, flags=re.MULTILINE)
        assert match is not None
