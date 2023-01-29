from apysc._expression import last_scope
from apysc._expression.last_scope import LastScope
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_reset() -> None:
    last_scope.set_last_scope(value=LastScope.FOR)
    last_scope.reset()
    last_scope_: LastScope = last_scope.get_last_scope()
    assert last_scope_ == LastScope.NORMAL


@apply_test_settings()
def test_get_last_scope() -> None:
    last_scope.reset()
    last_scope_: LastScope = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.NORMAL

    last_scope.set_last_scope(value=last_scope.LastScope.IF)
    last_scope_ = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.IF


@apply_test_settings()
def test_set_last_scope() -> None:
    last_scope.reset()
    last_scope.set_last_scope(value=last_scope.LastScope.IF)
    last_scope_: LastScope = last_scope.get_last_scope()
    assert last_scope_ == last_scope.LastScope.IF
