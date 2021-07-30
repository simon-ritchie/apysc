from random import randint
from typing import Any
from typing import Dict

import pytest
from pytest import raises
from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope
from tests.testing_helper import assert_attrs


class TestElif:

    @retry(stop_max_attempt_number=15, wait_fixed=1500)
    def test__append_enter_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        boolean_1: ap.Boolean = ap.Boolean(True)
        with raises(
                ValueError,
                match=r'Elif interface can only use right '
                      r'after If or Elif'):  # type: ignore
            with ap.Elif(boolean_1, locals(), globals()):
                pass

        with ap.If(boolean_1, locals(), globals()):
            pass
        with ap.Elif(boolean_1, locals(), globals()):
            pass
        with ap.Elif(boolean_1, locals(), globals()):
            pass
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            '\n}'
            f'\nelse if ({boolean_1.variable_name}) {{'
            '\n}'
        )
        assert expected in expression

        with ap.If(boolean_1, locals(), globals()):
            pass
        with pytest.raises(
                ValueError,
                match=r'Elif expression\'s condition argument '
                      r'can\'t be set None.'):  # type: ignore
            with ap.Elif(None, locals(), globals()):
                pass

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_last_scope(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(True)
        with ap.If(boolean_1, locals(), globals()):
            pass
        with ap.Elif(boolean_1, locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELIF

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        boolean_1: ap.Boolean = ap.Boolean(True)
        locals_: Dict[str, Any] = locals()
        globals_: Dict[str, Any] = globals()
        elif_: ap.Elif = ap.Elif(
            condition=boolean_1, locals_=locals_, globals_=globals_)
        assert_attrs(
            expected_attrs={
                '_condition': boolean_1,
                '_locals': locals_,
                '_globals': globals_,
            },
            any_obj=elif_)
