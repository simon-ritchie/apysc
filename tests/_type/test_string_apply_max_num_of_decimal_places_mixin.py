import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import string_apply_max_num_of_decimal_places_mixin


@apply_test_settings()
def test__get_py_str() -> None:
    max_num_of_decimal_places: ap.Int = ap.Int(3)
    py_str: str = string_apply_max_num_of_decimal_places_mixin._get_py_str(
        max_num_of_decimal_places=max_num_of_decimal_places,
        self_str="10.12345",
    )
    assert py_str == ""

    py_str = string_apply_max_num_of_decimal_places_mixin._get_py_str(
        max_num_of_decimal_places=max_num_of_decimal_places,
        self_str=ap.String("10.12345"),
    )
    assert py_str == "10.123"


class TestStringApplyMaxNumOfDecimalPlacesMixIn:
    @apply_test_settings()
    def test_apply_max_num_of_decimal_places(self) -> None:
        string: ap.String = ap.String("10.123.456")
        result_string: ap.String = string.apply_max_num_of_decimal_places(
            max_num_of_decimal_places=2,
            variable_name_suffix="test_suffix",
        )
        assert result_string == ap.String("10.123.456")
        assert "test_suffix" in result_string.variable_name
        expression: str = expression_data_util.get_current_expression()
        assert (
            f' = {string.variable_name}.match(new RegExp("^(\\\\d+\\\\.\\\\d{{"'
            in expression
        )

        ap.Stage()
        max_num_of_decimal_places: ap.Int = ap.Int(3)
        string = ap.String("10.123456")
        result_string = string.apply_max_num_of_decimal_places(
            max_num_of_decimal_places=max_num_of_decimal_places,
            variable_name_suffix="test_suffix",
        )
        assert result_string == ap.String("10.123")
        expression = expression_data_util.get_current_expression()
        assert (
            f' = {string.variable_name}.match(new RegExp("^(\\\\d+\\\\.\\\\d'
            f'{{" + {max_num_of_decimal_places.variable_name} + "}})\\\\d*$"));'
            in expression
        )
        assert "\nif (" in expression
        assert f"\n  {result_string.variable_name} = "
        assert "[1];" in expression
        assert "\n} else {" in expression
        assert (
            f"\n  {result_string.variable_name} = {string.variable_name};\n}}"
            in expression
        )
