from apysc._testing import testing_helper
from apysc._validation import size_validation


def test_validate_size_is_int() -> None:
    size_validation.validate_size_is_int(
        size=100, err_msg='Specified width is not integer value.')

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=size_validation.validate_size_is_int,
        kwargs={
            'size': '100px',
            'err_msg': 'Specified width is not integer value.'})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=size_validation.validate_size_is_int,
        kwargs={'size': '100px'})


def test_validate_size_is_gt_zero() -> None:
    size_validation.validate_size_is_gt_zero(
        size=1,
        err_msg='Specified width is less than or equal to zero.')

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=size_validation.validate_size_is_gt_zero,
        kwargs={'size': 0})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=size_validation.validate_size_is_gt_zero,
        kwargs={
            'size': 0,
            'err_msg': 'Specified width is less than or equal to zero.'})


def test_validate_size_is_gte_zero() -> None:
    size_validation.validate_size_is_gte_zero(size=0)
    size_validation.validate_size_is_gte_zero(size=100)

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=size_validation.validate_size_is_gte_zero,
        kwargs={'size': -1})

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=size_validation.validate_size_is_gte_zero,
        kwargs={'size': -1, 'err_msg': 'Size is invalid.'})
