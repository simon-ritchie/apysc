from random import randint
import inspect
from typing import Any, Dict, List

from retrying import retry
from typing_extensions import TypedDict

import apysc as ap
from apysc._validation import options_validation
from apysc._validation.options_validation import _ArgData, _HandlerArgumentsLengthError, _HandlerFirstArgumentNameError, _HandlerSecondArgumentNameError, _TypedDictOptionsTypeMismatchError
from tests.testing_helper import assert_raises


class _TestTypedDict1(TypedDict):
    a: int
    b: str
    c: Any


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_dict_type() -> None:
    options_validation._validate_dict_type(options={'a': 10})

    test_typed_dict: _TestTypedDict1 = {
        'a': 10,
        'b': 'Hello',
        'c': 20,
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


def _test_handler_2(
        e: ap.Event, options: Dict[str, Any], third_arg: int) -> None:
    """
    The handler function for the testing.

    Parameters
    ----------
    e : Event
        Event instance.
    options : dict
        Optional arguments dictionary.
    third_arg : int
        Third argument.
    """


def _test_handler_3(evt: ap.Event, options: Dict[str, Any]) -> None:
    """
    The handler function for the testing.

    Parameters
    ----------
    evt : Event
        Event instance.
    options : dict
        Optional arguments dictionary.
    """


def _test_handler_4(e: ap.Event, opt: Dict[str, Any]) -> None:
    """
    The handler function for the testing.

    Parameters
    ----------
    e : Event
        Event instance.
    opt : dict
        Optional arguments dictionary.
    """


def _test_handler_5(e: ap.Event, options: _TestTypedDict1) -> None:
    """
    The handler function for the testing.

    Parameters
    ----------
    e : Event
        Event instance.
    options : _TestTypedDict1
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


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_arg_names() -> None:
    handler_arg_data_list: List[_ArgData] = options_validation.\
        _get_handler_arg_data_list(handler=_test_handler_2)  # type: ignore
    assert_raises(
        expected_error_class=_HandlerArgumentsLengthError,
        func_or_method=options_validation._validate_arg_names,
        kwargs={'handler_arg_data_list': handler_arg_data_list},
        match='Passed handler arguments length is invalid.')

    handler_arg_data_list = options_validation._get_handler_arg_data_list(
        handler=_test_handler_3)  # type: ignore
    assert_raises(
        expected_error_class=_HandlerFirstArgumentNameError,
        func_or_method=options_validation._validate_arg_names,
        kwargs={'handler_arg_data_list': handler_arg_data_list},
        match="Passed handler's first argument name is invalid.")

    handler_arg_data_list = options_validation._get_handler_arg_data_list(
        handler=_test_handler_4)  # type: ignore
    assert_raises(
        expected_error_class=_HandlerSecondArgumentNameError,
        func_or_method=options_validation._validate_arg_names,
        kwargs={'handler_arg_data_list': handler_arg_data_list},
        match="Passed handler's second argument name is invalid.")

    handler_arg_data_list = options_validation._get_handler_arg_data_list(
        handler=_test_handler_1)
    options_validation._validate_arg_names(
        handler_arg_data_list=handler_arg_data_list)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__is_typed_dict_options_arg() -> None:
    handler_arg_data_list: List[_ArgData] = options_validation.\
        _get_handler_arg_data_list(handler=_test_handler_1)
    result: bool = options_validation._is_typed_dict_options_arg(
        handler_arg_data_list=handler_arg_data_list)
    assert not result

    handler_arg_data_list = options_validation._get_handler_arg_data_list(
        handler=_test_handler_5)  # type: ignore
    result = options_validation._is_typed_dict_options_arg(
        handler_arg_data_list=handler_arg_data_list)
    assert result


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__get_options_annotation_from_handler_arg_data_list() -> None:
    handler_arg_data_list: List[_ArgData] = options_validation.\
        _get_handler_arg_data_list(handler=_test_handler_1)
    annotation: Any = options_validation.\
        _get_options_annotation_from_handler_arg_data_list(
            handler_arg_data_list=handler_arg_data_list)
    assert annotation == Dict[str, Any]


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__validate_typed_dict() -> None:
    handler_arg_data_list: List[_ArgData] = options_validation.\
        _get_handler_arg_data_list(handler=_test_handler_1)
    options_validation._validate_typed_dict(
        handler_arg_data_list=handler_arg_data_list,
        options={'a': 10})

    handler_arg_data_list = options_validation._get_handler_arg_data_list(
        handler=_test_handler_5)  # type: ignore
    options: Dict[str, Any] = {'a': 10, 'c': 20}
    assert_raises(
        expected_error_class=_TypedDictOptionsTypeMismatchError,
        func_or_method=options_validation._validate_typed_dict,
        kwargs={
            'handler_arg_data_list': handler_arg_data_list,
            'options': options,
        },
        match='There is no options dictionary key: b',
    )

    options = {'a': 10, 'b': 20, 'c': 30}
    assert_raises(
        expected_error_class=_TypedDictOptionsTypeMismatchError,
        func_or_method=options_validation._validate_typed_dict,
        kwargs={
            'handler_arg_data_list': handler_arg_data_list,
            'options': options,
        },
        match='There is a options value type mismatch.',
    )

    options = {'a': 10, 'b': 'Hello', 'c': 30}
    options_validation._validate_typed_dict(
        handler_arg_data_list=handler_arg_data_list, options=options)
