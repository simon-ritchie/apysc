from random import randint
from typing import Any

from retrying import retry
from typing_extensions import TypedDict

import apysc as ap
from apysc._testing.testing_helper import assert_raises
from apysc._validation import handler_validation


class _TestTypedDict(TypedDict):
    a: int


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_options_type() -> None:
    handler_validation.validate_options_type(options=None)

    handler_validation.validate_options_type(
        options={'a': 10})

    test_typed_dict: _TestTypedDict = {'a': 20}
    handler_validation.validate_options_type(options=test_typed_dict)

    assert_raises(
        expected_error_class=TypeError,
        func_or_method=handler_validation.validate_options_type,
        kwargs={'options': [10]},
        match="Handler's options argument must be a dictionary")


def _test_handler_1(*, e: ap.Event) -> None:
    ...


def _test_handler_2(*, e: ap.Event, options: dict) -> None:
    ...


def _test_handler_3(self: Any, *, e: ap.Event, options: dict) -> None:
    ...


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_handler_args_num() -> None:
    assert_raises(
        expected_error_class=ValueError,
        func_or_method=handler_validation.validate_handler_args_num,
        kwargs={'handler': _test_handler_1},
        match=r'A specified handler\'s arguments number '
        r'must be 2 \(actual: 1\)')

    handler_validation.validate_handler_args_num(handler=_test_handler_2)
    handler_validation.validate_handler_args_num(handler=_test_handler_3)
