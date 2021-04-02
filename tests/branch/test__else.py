from random import randint

from retrying import retry

import pytest

from apysc.branch import If, Elif, Else
from apysc.expression import expression_file_util, last_scope
from apysc.expression.last_scope import LastScope
from apysc.type import Boolean, Int


class TestElse:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_enter_expression(self) -> None:
        expression_file_util.remove_expression_file()
        last_scope.reset()

        with pytest.raises(ValueError):  # type: ignore
            with Else(locals(), globals()):
                pass
            pass

        boolean_1: Boolean = Boolean(True)
        int_1: Int = Int(10)
        with If(boolean_1, locals(), globals()):
            pass
        with Else(locals(), globals()):
            int_1.value = 20

        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if ({boolean_1.variable_name}) {{'
            '\n}'
            '\nelse {'
            f'\n  {int_1.variable_name} = 20;'
            '\n}'
        )
        assert expected in expression
        assert int_1 == 10

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__set_last_scope(self) -> None:
        expression_file_util.remove_expression_file()
        last_scope.reset()
        boolean_1: Boolean = Boolean(True)
        with If(boolean_1, locals(), globals()):
            pass
        with Else(locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELSE
