from random import randint

import pytest
from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util
from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope


class TestElse:

    @retry(stop_max_attempt_number=15, wait_fixed=1000)
    def test__append_enter_expression(self) -> None:
        expression_file_util.empty_expression()
        last_scope.reset()

        with pytest.raises(ValueError):  # type: ignore
            with ap.Else(locals(), globals()):
                pass

        boolean_1: ap.Boolean = ap.Boolean(True)
        int_1: ap.Int = ap.Int(10)
        with ap.If(boolean_1, locals(), globals()):
            pass
        with ap.Else(locals(), globals()):
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_last_scope(self) -> None:
        expression_file_util.empty_expression()
        last_scope.reset()
        boolean_1: ap.Boolean = ap.Boolean(True)
        with ap.If(boolean_1, locals(), globals()):
            pass
        with ap.Else(locals(), globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELSE
