from random import randint
from typing import List, Type

from retrying import retry

from apyscript.validation import expression_arg_validation
from tests import testing_helper
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__validate_args() -> None:
    acceptable_arg_types: List[Type] = [Stage, Sprite]
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=expression_arg_validation._validate_args,
        kwargs={
            'args': [100],
            'acceptable_arg_types': acceptable_arg_types,
        })

    stage: Stage = Stage()
    expression_arg_validation._validate_args(
        args=[stage], acceptable_arg_types=acceptable_arg_types)


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__is_acceptable_arg() -> None:
    acceptable_arg_types: List[Type] = [Stage, Sprite]
    result: bool = expression_arg_validation._is_acceptable_arg(
        arg=100, acceptable_types=acceptable_arg_types)
    assert not result

    stage: Stage = Stage()
    result = expression_arg_validation._is_acceptable_arg(
        arg=stage, acceptable_types=acceptable_arg_types)
    assert result


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test__validate_kwargs() -> None:
    acceptable_arg_types: List[Type] = [Stage, Sprite]
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=expression_arg_validation._validate_kwargs,
        kwargs={
            'kwargs': {'a': 100},
            'acceptable_arg_types': acceptable_arg_types,
        })

    stage: Stage = Stage()
    expression_arg_validation._validate_kwargs(
        kwargs={'a': stage}, acceptable_arg_types=acceptable_arg_types)


@retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
def test_validate_acceptable_arg_types() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=expression_arg_validation.
        validate_acceptable_arg_types,
        kwargs={
            'args': [100],
            'kwargs': {},
        }
    )

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=expression_arg_validation.
        validate_acceptable_arg_types,
        kwargs={
            'args': [],
            'kwargs': {'a': 100},
        }
    )

    stage: Stage = Stage()
    expression_arg_validation.validate_acceptable_arg_types(
        args=[stage], kwargs={'a': stage})


def test_validate_default_values_not_exist() -> None:

    def _test_func_1(a: int, b: str) -> None:
        ...

    expression_arg_validation.validate_default_values_not_exist(
        func=_test_func_1)

    def _test_func_2(a: int, b: str = '') -> None:
        ...

    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=expression_arg_validation.
        validate_default_values_not_exist,
        kwargs={'func': _test_func_2},
    )
