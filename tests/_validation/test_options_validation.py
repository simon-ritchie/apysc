from random import randint
import inspect
from typing import Any, Dict, List

from retrying import retry
from typing_extensions import TypedDict

import apysc as ap
from apysc._validation import options_validation
from apysc._validation.options_validation import _ArgData
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


def _test_handler_1(e: ap.Event, options: Dict[str, Any]) -> None:
    """
    The handler function for the testing.

    Parameters
    ----------
    e : Event
        Event instance.
    options : dict
        Optional arguments dictionary.
    """


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_handler_arg_data_list() -> None:
    handler_arg_data_list: List[_ArgData] = options_validation.\
        _get_handler_arg_data_list(handler=_test_handler_1)
    arg_names: List[str] = [
        arg_data['arg_name'] for arg_data in handler_arg_data_list]
    assert arg_names == ['e', 'options']

    annotations: List[Any] = [
        arg_data['annotation'] for arg_data in handler_arg_data_list]
    assert annotations == [ap.Event, Dict[str, Any]]
