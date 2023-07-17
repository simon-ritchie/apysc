import apysc as ap
from apysc._expression import expression_data_util
from apysc._math import min_mixin
from apysc._math.min_mixin import MinMixIn
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_min_float_value() -> None:
    ap.Stage()
    min_value: float = min_mixin._get_min_float_value(
        values=ap.Array([10, 10.5, ap.Int(9), ap.Number(8.5)])
    )
    assert min_value == 8.5


@apply_test_settings()
def test__get_min_value_variable_name_suffix_from_arr() -> None:
    ap.Stage()
    suffix: str = min_mixin._get_min_value_variable_name_suffix_from_arr(
        arr=ap.Array(
            [
                10,
                ap.Int(9, variable_name_suffix="test_int_1"),
                10.5,
                ap.Number(9.5, variable_name_suffix="test_number_1"),
            ]
        )
    )
    assert suffix == "test_int_1"

    suffix = min_mixin._get_min_value_variable_name_suffix_from_arr(
        arr=ap.Array(
            [
                8.5,
                ap.Int(9, variable_name_suffix="test_int_1"),
                10,
                ap.Number(9.5, variable_name_suffix="test_number_1"),
            ]
        )
    )
    assert suffix == ""


class TestMinMixIn:
    @apply_test_settings()
    def test_min(self) -> None:
        values: ap.Array = ap.Array([10, 9.5, ap.Int(9), ap.Number(9.5)])
        min_value: ap.Number = MinMixIn.min(
            values=values,
        )
        assert min_value == ap.Number(9)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{min_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.min(a, b)});"
        )
        assert expected in expression
