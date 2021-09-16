from random import randint

from retrying import retry
from typing_extensions import TypedDict

from apysc._validation import options_validation
from tests.testing_helper import assert_raises


class _TestTypedDict1(TypedDict):
    a: int
    b: str


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_dict_type() -> None:
    options_validation._validate_dict_type(options={'a': 10})

    test_typed_dict: _TestTypedDict1 = {
        'a': 10,
        'b': 'Hello',
    }
    options_validation._validate_dict_type(options=test_typed_dict)

    assert_raises(
        expected_error_class=TypeError,
        func_or_method=options_validation._validate_dict_type,
        kwargs={'options': [1, 2]},
    )
