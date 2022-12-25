from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import expression_data_util



class TestTruncMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_trunc(self) -> None:
        expression_data_util.empty_expression()
        value: ap.Int = ap.Int(10)
        result: ap.Int = ap.Math.trunc(value=value)
        assert isinstance(result, ap.Int)
        assert result == 10
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{result.variable_name} = Math.trunc({value.variable_name});"
        )
        assert expected in expression

        result = ap.Math.trunc(value=ap.Number(10.5))
        assert result._value == 10

        result = ap.Math.trunc(value=ap.String("10.5"))
        assert result._value == 10

        result = ap.Math.trunc(value=ap.String("a"))
        assert result._value == 0
