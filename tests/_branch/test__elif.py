from random import randint

import pytest
from pytest import raises
from retrying import retry

from apysc import Boolean
from apysc import Elif
from apysc import If
from apysc._expression import expression_file_util
from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope


class TestElif:

    @retry(stop_max_attempt_number=15, wait_fixed=1500)
    def test__append_enter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(True)
        with raises(
                ValueError,
                match=r'Elif interface can only use right '
                      r'after If or Elif'):  # type: ignore
            with Elif(boolean_1, locals(), globals()):
                pass

        with If(boolean_1, locals(), globals()):
            pass
        with Elif(boolean_1, locals(), globals()):
            pass
        with Elif(boolean_1, locals(), globals()):
            pass
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            '\n}'
            f'\nelse if ({boolean_1.variable_name}) {{'
            '\n}'
        )
        assert expected in expression

        with If(boolean_1, locals(), globals()):
            pass
        with pytest.raises(
                ValueError,
                match=r'Elif expression\'s condition argument '
                      r'can\'t be set None.'):  # type: ignore
            with Elif(None, locals(), globals()):
                pass

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_last_scope(self) -> None:
        boolean_1: Boolean = Boolean(True)
        with If(boolean_1, locals(), globals()):
            pass
        with Elif(boolean_1, locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELIF
