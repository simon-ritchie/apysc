from random import randint

from retrying import retry

from typing import Any, Dict
from apysc.branch import If
from apysc.type import Boolean, Int
from apysc.expression import indent_num
from apysc.expression import expression_file_util
from tests import testing_helper


class TestIf:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        boolean_1: Boolean = Boolean(True)
        locals_: Dict[str, Any] = locals()
        globals_: Dict[str, Any] = globals()
        if_: If = If(
            condition=boolean_1, locals_=locals_, globals_=globals_)
        assert if_._condition
        testing_helper.assert_attrs(
            expected_attrs={
                '_condition': boolean_1,
                '_locals': locals_,
                '_globals': globals_,
            },
            any_obj=if_)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___enter__(self) -> None:
        indent_num.reset()
        int_1: Int = Int(10)
        int_2: Int = Int(20)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': int_2}
        boolean_1: Boolean = Boolean(True)
        with If(condition=boolean_1, locals_=locals_, globals_=globals_):
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
        snapshot_name: str = list(int_1._value_snapshots.keys())[0]
        assert int_1._value_snapshots[snapshot_name] == 10
        assert int_2._value_snapshots[snapshot_name] == 20

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___exit__(self) -> None:
        indent_num.reset()
        int_1: Int = Int(10)
        int_2: Int = Int(20)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': int_2}
        boolean_1: Boolean = Boolean(True)
        with If(condition=boolean_1, locals_=locals_, globals_=globals_):
            int_1.value = 100
            int_2.value = 200
        assert int_1 == 10
        assert int_2 == 20
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_enter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        indent_num.reset()
        int_1: Int = Int(10)
        boolean_1: Boolean = Boolean(True)
        with If (condition=boolean_1, locals_=locals(), globals_=globals()):
            int_1.value = 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            f'\n  {int_1.variable_name} = 20;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_exit_expression(self) -> None:
        expression_file_util.remove_expression_file()
        indent_num.reset()
        boolean_1: Boolean = Boolean(True)
        int_1: Int = Int(10)
        with If (condition=boolean_1, locals_=locals(), globals_=globals()):
            int_1.value = 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            f'\n  {int_1.variable_name} = 20;'
            '\n}'
        )
        assert expected in expression
