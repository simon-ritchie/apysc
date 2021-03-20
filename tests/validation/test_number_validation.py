from apyscript.type import Int
from apyscript.validation import number_validation
from tests import testing_helper


def test_validate_num() -> None:
    number_validation.validate_num(num=100)
    number_validation.validate_num(num=100.5)
    number_validation.validate_num(num=Int(value=100))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_num,
        kwargs={'num': 'Hello!'})


def test_validate_integer() -> None:
    number_validation.validate_integer(integer=10)
    number_validation.validate_integer(integer=Int(10))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_integer,
        kwargs={'integer': 10.5})


def test_validate_num_is_gt_zero() -> None:
    number_validation.validate_num_is_gt_zero(num=1)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_num_is_gt_zero,
        kwargs={'num': 0})


def test_validate_num_is_gte_zero() -> None:
    number_validation.validate_num_is_gte_zero(num=0)
    number_validation.validate_num_is_gte_zero(num=1)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_num_is_gte_zero,
        kwargs={'num': -0.1})


def test_validate_int_is_zero_or_one() -> None:
    number_validation.validate_int_is_zero_or_one(
        integer='Hello!')  # type: ignore
    number_validation.validate_int_is_zero_or_one(integer=1)
    number_validation.validate_int_is_zero_or_one(integer=0)
    number_validation.validate_int_is_zero_or_one(integer=Int(0))
    number_validation.validate_int_is_zero_or_one(integer=Int(1))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_int_is_zero_or_one,
        kwargs={'integer': 2})
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_int_is_zero_or_one,
        kwargs={'integer': Int(2)})
