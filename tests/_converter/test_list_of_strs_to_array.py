from typing import Optional
from apysc._converter import list_of_strs_to_array
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap


@apply_test_settings()
def test_list_of_strs_to_array_of_string() -> None:
    converted_value: Optional[ap.Array] = (
        list_of_strs_to_array.list_of_strs_to_array_of_string(
            optional_list_or_arr=None,
        )
    )
    assert converted_value is None

    converted_value = list_of_strs_to_array.list_of_strs_to_array_of_string(
        optional_list_or_arr=["Hello", "World"],
    )
    assert isinstance(converted_value, ap.Array)
    assert converted_value._value == ["Hello", "World"]

    arr: ap.Array[ap.String] = ap.Array([ap.String("Hello"), ap.String("World")])
    converted_value = list_of_strs_to_array.list_of_strs_to_array_of_string(
        optional_list_or_arr=arr,
    )
    assert converted_value is not None
    assert isinstance(converted_value, ap.Array)
    assert arr.variable_name == converted_value.variable_name
