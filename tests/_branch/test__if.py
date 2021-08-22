from random import randint
from typing import Any
from typing import Dict

import pytest
from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression import indent_num
from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope
from tests import testing_helper


class TestIf:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(True)
        locals_: Dict[str, Any] = locals()
        globals_: Dict[str, Any] = globals()
        if_: ap.If = ap.If(
            condition=boolean_1, locals_=locals_, globals_=globals_)
        assert if_._condition
        testing_helper.assert_attrs(
            expected_attrs={
                '_condition': boolean_1,
                '_locals': locals_,
                '_globals': globals_,
            },
            any_obj=if_)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___enter__(self) -> None:
        indent_num.reset()
        int_1: ap.Int = ap.Int(10)
        int_2: ap.Int = ap.Int(20)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': int_2}
        boolean_1: ap.Boolean = ap.Boolean(True)
        with ap.If(condition=boolean_1, locals_=locals_, globals_=globals_):
            current_indent_num: int = indent_num.get_current_indent_num()
            assert current_indent_num == 1
        snapshot_name: str = list(int_1._value_snapshots.keys())[0]
        assert int_1._value_snapshots[snapshot_name] == 10
        assert int_2._value_snapshots[snapshot_name] == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___exit__(self) -> None:
        indent_num.reset()
        int_1: ap.Int = ap.Int(10)
        int_2: ap.Int = ap.Int(20)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': int_2}
        boolean_1: ap.Boolean = ap.Boolean(True)
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.NORMAL
        with ap.If(condition=boolean_1, locals_=locals_, globals_=globals_):
            int_1.value = 100
            int_2.value = 200
            last_scope_ = last_scope.get_last_scope()
            assert last_scope_ == LastScope.NORMAL
        last_scope_ = last_scope.get_last_scope()
        assert last_scope_ == LastScope.IF
        assert int_1 == 10
        assert int_2 == 20
        current_indent_num: int = indent_num.get_current_indent_num()
        assert current_indent_num == 0
        int_1.value = 100
        last_scope_ = last_scope.get_last_scope()
        assert last_scope_ == LastScope.NORMAL

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_enter_expression(self) -> None:
        expression_file_util.empty_expression()
        indent_num.reset()
        int_1: ap.Int = ap.Int(10)
        boolean_1: ap.Boolean = ap.Boolean(True)
        with ap.If(condition=boolean_1, locals_=locals(), globals_=globals()):
            int_1.value = 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            f'\n  {int_1.variable_name} = 20;'
        )
        assert expected in expression

        with pytest.raises(ValueError):  # type: ignore
            with ap.If(None, locals(), globals()):
                pass

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_exit_expression(self) -> None:
        expression_file_util.empty_expression()
        indent_num.reset()
        boolean_1: ap.Boolean = ap.Boolean(True)
        int_1: ap.Int = ap.Int(10)
        with ap.If(condition=boolean_1, locals_=locals(), globals_=globals()):
            int_1.value = 20
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            f'\n  {int_1.variable_name} = 20;'
            '\n}'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_last_scope(self) -> None:
        with ap.If(ap.Boolean(True), locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.IF
