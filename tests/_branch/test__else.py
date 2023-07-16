import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope
from apysc._testing.testing_helper import apply_test_settings


class TestElse:
    @apply_test_settings(retrying_sleep_seconds=1)
    def test__append_enter_expression(self) -> None:
        ap.Stage()
        last_scope.reset()

        with pytest.raises(ValueError):  # type: ignore
            with ap.Else(locals_=locals(), globals_=globals()):
                pass

        boolean_1: ap.Boolean = ap.Boolean(True)
        int_1: ap.Int = ap.Int(10)
        with ap.If(boolean_1, locals_=locals(), globals_=globals()):
            pass
        with ap.Else(locals_=locals(), globals_=globals()):
            int_1.value = 20

        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"if ({boolean_1.variable_name}) {{"
            "\n}"
            "\nelse {"
            f"\n  {int_1.variable_name} = 20;"
            "\n}"
        )
        assert expected in expression
        assert int_1 == 10

    @apply_test_settings()
    def test__set_last_scope(self) -> None:
        ap.Stage()
        last_scope.reset()
        boolean_1: ap.Boolean = ap.Boolean(True)
        with ap.If(boolean_1, locals_=locals(), globals_=globals()):
            pass
        with ap.Else(locals_=locals(), globals_=globals()):
            pass
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.ELSE
