from apysc.expression import expression_file_util
from random import randint

from retrying import retry
from pytest import raises

from apysc.branch import Elif, If
from apysc.type import Int, Boolean
from apysc.expression.last_scope import LastScope
from apysc.expression import last_scope


class TestElif:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_enter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        boolean_1: Boolean = Boolean(True)
        with raises(ValueError):  # type: ignore
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

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__set_last_scope(self) -> None:
        boolean_1: Boolean = Boolean(True)
        with If(boolean_1, locals(), globals()):
            pass
        with Elif(boolean_1, locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELIF
