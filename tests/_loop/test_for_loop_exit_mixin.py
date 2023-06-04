from apysc._expression import expression_data_util
from apysc._expression import last_scope
from apysc._expression.get_last_scope_interface import GetLastScopeInterface
from apysc._expression.indent_num import Indent
from apysc._expression.last_scope import LastScope
from apysc._loop import loop_count
from apysc._loop.for_loop_exit_mixin import ForLoopExitMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class _TestMixIn(ForLoopExitMixIn, GetLastScopeInterface):
    def _get_last_scope(self) -> LastScope:
        """
        Get a target last scope value.

        Returns
        -------
        last_scope : LastScope
            A target last scope.
        """
        return LastScope.FOR_ARRAY_INDICES


class TestForLoopExitMixIn:
    @apply_test_settings()
    def test___exit__(self) -> None:
        expression_data_util.empty_expression()
        mixin_1: _TestMixIn = _TestMixIn()
        mixin_1._locals = {}
        mixin_1._globals = {}
        mixin_1._snapshot_name = "test_snapshot"
        mixin_1._indent = Indent()
        mixin_1._indent.__enter__()
        loop_count.increment_current_loop_count()
        mixin_1.__exit__()
        expression: str = expression_data_util.get_current_expression()
        assert "}" in expression
        last_scope_: LastScope = last_scope.get_last_scope()
        assert last_scope_ == LastScope.FOR_ARRAY_INDICES
        assert loop_count.get_current_loop_count() == 0

        mixin_2: ForLoopExitMixIn = ForLoopExitMixIn()
        mixin_2._locals = {}
        mixin_2._globals = {}
        mixin_2._snapshot_name = "test_snapshot"
        mixin_2._indent = Indent()
        mixin_2._indent.__enter__()
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin_2.__exit__,
        )
