from random import randint

from pytest import raises
from retrying import retry

from apysc.branch import Elif
from apysc.branch import If
from apysc.expression import expression_file_util
from apysc.expression import last_scope
from apysc.expression.last_scope import LastScope
from apysc.type import Boolean
from tests import testing_helper


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

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=If,
            kwargs={
                'condition': None,
                'locals_': locals(),
                'globals_': globals(),
            })

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__set_last_scope(self) -> None:
        boolean_1: Boolean = Boolean(True)
        with If(boolean_1, locals(), globals()):
            pass
        with Elif(boolean_1, locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELIF
