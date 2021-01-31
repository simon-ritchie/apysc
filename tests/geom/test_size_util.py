from apyscript.geom import size_util
from tests import testing_helper


def test_validate_size_is_int() -> None:
    size_util.validate_size_is_int(
        size=100, err_msg='Specified width is not integer value.')

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=size_util.validate_size_is_int,
        kwargs={
            'size': '100px',
            'err_msg': 'Specified width is not integer value.'})


def test_validate_size_is_greater_than_zero() -> None:
    size_util.validate_size_is_greater_than_zero(
        size=1,
        err_msg='Specified width is less than or equal to zero.')

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=size_util.validate_size_is_greater_than_zero,
        kwargs={
            'size': 0 ,
            'err_msg': 'Specified width is less than or equal to zero.'})
