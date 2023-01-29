from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises
from apysc._testing.testing_helper import apply_test_settings


class TestContinue:
    @apply_test_settings()
    def test___init__(self) -> None:
        expression_data_util.empty_expression()
        assert_raises(
            expected_error_class=Exception,
            callable_=ap.Continue,
        )

        arr: ap.Array = ap.Array([1, 2, 3])
        with ap.For(arr):
            ap.Continue()
        expression: str = expression_data_util.get_current_expression()
        assert "continue;" in expression
