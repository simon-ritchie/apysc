import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._validation import matrix_data_validation


@apply_test_settings()
def test_validate_matrix_list_data() -> None:
    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_list_data,
        match="A specified data type is not a list: ",
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
        match="A specified dict value type is not int, float, or str: ",
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
            },
        ],
    )


@apply_test_settings()
def test_validate_matrix_array_data() -> None:
    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_array_data,
        match="A specified data type is not `ap.Array`: ",
        matrix_array_data=100,
        additional_err_msg="test message",
    )

    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_array_data,
        match="A specified `ap.Array` value's type is not the `ap.Dictionary`: ",
        matrix_array_data=ap.Array([10, 20]),
        additional_err_msg="test message",
    )

    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_array_data,
        match="A specified dictionary key type is not the `ap.String`: ",
        matrix_array_data=ap.Array([ap.Dictionary({0: ap.Int(10)})]),
        additional_err_msg="test message",
    )

    assert_raises(
        expected_error_class=TypeError,
        callable_=matrix_data_validation.validate_matrix_array_data,
        match="A specified dictionary value type is not `ap.Int`, ",
        matrix_array_data=ap.Array([ap.Dictionary({ap.String("a"): 10})]),
        additional_err_msg="test message",
    )

    matrix_data_validation.validate_matrix_array_data(
        matrix_array_data=ap.Array([ap.Dictionary({ap.String("a"): ap.Int(10)})]),
        additional_err_msg="test message",
    )
