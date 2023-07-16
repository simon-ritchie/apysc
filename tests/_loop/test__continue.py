import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


class TestContinue:
    @apply_test_settings()
    def test___init__(self) -> None:
        ap.Stage()
        assert_raises(
            expected_error_class=Exception,
            callable_=ap.Continue,
        )

        arr: ap.Array = ap.Array([1, 2, 3])
        with ap.ForArrayIndices(arr):
            ap.Continue()
        expression: str = expression_data_util.get_current_expression()
        assert "continue;" in expression
