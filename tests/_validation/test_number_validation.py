from random import randint

from retrying import retry

import apysc as ap
from apysc._validation import number_validation
from tests import testing_helper


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_num() -> None:
    number_validation.validate_num(num=100)
    number_validation.validate_num(num=100.5)
    number_validation.validate_num(num=ap.Int(value=100))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_num,
        kwargs={'num': 'Hello!'})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_integer() -> None:
    number_validation.validate_integer(integer=10)
    number_validation.validate_integer(integer=ap.Int(10))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_integer,
        kwargs={'integer': 10.5})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_num_is_gt_zero() -> None:
    number_validation.validate_num_is_gt_zero(num=1)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_num_is_gt_zero,
        kwargs={'num': 0})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_num_is_gte_zero() -> None:
    number_validation.validate_num_is_gte_zero(num=0)
    number_validation.validate_num_is_gte_zero(num=1)
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_num_is_gte_zero,
        kwargs={'num': -0.1})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_int_is_zero_or_one() -> None:
    number_validation.validate_int_is_zero_or_one(
        integer='Hello!')  # type: ignore
    number_validation.validate_int_is_zero_or_one(integer=1)
    number_validation.validate_int_is_zero_or_one(integer=0)
    number_validation.validate_int_is_zero_or_one(integer=ap.Int(0))
    number_validation.validate_int_is_zero_or_one(integer=ap.Int(1))
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_int_is_zero_or_one,
        kwargs={'integer': 2})
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_int_is_zero_or_one,
        kwargs={'integer': ap.Int(2)})


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_nums_are_int_and_gt_zero() -> None:
    number_validation.validate_nums_are_int_and_gt_zero(
        nums=[1, ap.Int(1)])
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_nums_are_int_and_gt_zero,
        kwargs={'nums': [10.5]})
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=number_validation.validate_nums_are_int_and_gt_zero,
        kwargs={'nums': [0]})
