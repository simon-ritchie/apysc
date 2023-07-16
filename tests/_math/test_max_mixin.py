import apysc as ap
from apysc._expression import expression_data_util
from apysc._math import max_mixin
from apysc._math.max_mixin import MaxMixIn
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__get_max_float_value() -> None:
    ap.Stage()
    max_value: float = max_mixin._get_max_float_value(
        values=ap.Array([10, 10.5, ap.Int(11), ap.Number(10.9)]),
    )
    assert max_value == 11.0


@apply_test_settings()
def test__get_max_value_variable_name_suffix_from_arr() -> None:
    ap.Stage()
    suffix: str = max_mixin._get_max_value_variable_name_suffix_from_arr(
        arr=ap.Array(
            [
                10,
                9.5,
                ap.Int(11, variable_name_suffix="test_int"),
                ap.Number(10.5, variable_name_suffix="test_number"),
            ]
        ),
    )
    assert suffix == "test_int"


class TestMaxMixIn:
    @apply_test_settings()
    def test_max(self) -> None:
        ap.Stage()
        values: ap.Array = ap.Array([10, 10.5, ap.Int(11), ap.Number(10.9)])
        max_value: ap.Number = MaxMixIn.max(values=values)
        assert max_value == ap.Number(11.0)

        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{max_value.variable_name} = {values.variable_name}.reduce("
            "function (a, b) {return Math.max(a, b)});"
        )
        assert expected in expression
