import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestClampMixIn:
    @apply_test_settings()
    def test_clamp(self) -> None:
        result_1: ap.Number = ap.Math.clamp(
            value=ap.Number(3),
            min_=ap.Number(5),
            max_=ap.Number(10),
        )
        assert result_1._value == 5
        expression: str = expression_data_util.get_current_expression()
        assert "Math.max" in expression
        assert "Math.min" in expression
        assert isinstance(result_1, ap.Number)

        result_1 = ap.Math.clamp(
            value=ap.Number(11),
            min_=ap.Number(5),
            max_=ap.Number(10),
        )
        assert result_1._value == 10

        result_2: ap.Int = ap.Math.clamp(
            value=ap.Int(5),
            min_=ap.Int(3),
            max_=ap.Int(10),
        )
        assert result_2._value == 5
        assert isinstance(result_2, ap.Int)
