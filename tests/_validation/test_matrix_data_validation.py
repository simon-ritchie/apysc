import apysc as ap
from apysc._validation import matrix_data_validation
from apysc._testing.testing_helper import apply_test_settings, assert_raises


@apply_test_settings()
def test_validate_matrix_list_data() -> None:
    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_list_data,
        match="A specified data type is not the list: ",
        matrix_list_data=10,
        additional_err_msg="test message",
    )

    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_list_data,
        match="A specified list value's type is not the dict: ",
        matrix_list_data=[10, 20, 30],
        additional_err_msg="test message",
    )

    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_list_data,
        match="A specified dict key type is not the str: ",
        matrix_list_data=[{10: 20}],
        additional_err_msg="test message",
    )

    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_list_data,
        match="A specified dict value type is not the int, float, or str: ",
        matrix_list_data=[{"price": [10, 20]}],
        additional_err_msg="test message",
    )

    matrix_data_validation.validate_matrix_list_data(
        matrix_list_data=[
            {
                "price": 100,
                "percentage": 10.5,
                "date": "1970-01-01",
            },
            {
                "price": 200,
                "percentage": 20.5,
                "date": "1970-01-02",
            }
        ],
    )
