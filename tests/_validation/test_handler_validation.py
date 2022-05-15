from random import randint

from retrying import retry
from typing_extensions import TypedDict

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
