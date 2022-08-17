import inspect
from random import randint
from typing import Any

from retrying import retry
from typing_extensions import TypedDict

import apysc as ap
from apysc._testing.testing_helper import assert_raises
from apysc._validation import handler_validation
from apysc._validation.handler_validation import InvalidAssignmentInHandler


class _TestTypedDict(TypedDict):
    a: int


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_options_type() -> None:
    handler_validation.validate_options_type(options=None)

    handler_validation.validate_options_type(options={"a": 10})

    test_typed_dict: _TestTypedDict = {"a": 20}
    handler_validation.validate_options_type(options=test_typed_dict)

    assert_raises(
        expected_error_class=TypeError,
        callable_=handler_validation.validate_options_type,
        match="Handler's options argument must be a dictionary",
        options=[10],
    )
    assert_raises(
        expected_error_class=TypeError,
        callable_=handler_validation.validate_options_type,
        match="\nTest error!",
        options=[10],
        additional_err_msg="Test error!",
    )


def _test_handler_1(*, e: ap.Event) -> None:
    ...


def _test_handler_2(*, e: ap.Event, options: dict) -> None:
    ...


def _test_handler_3(self: Any, *, e: ap.Event, options: dict) -> None:
    ...


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_handler_args_num() -> None:
    assert_raises(
        expected_error_class=TypeError,
        callable_=handler_validation.validate_handler_args_num,
        match="A specified handler's argument is not callable:",
        handler=100,
    )

    assert_raises(
        expected_error_class=ValueError,
        callable_=handler_validation.validate_handler_args_num,
        match=r"A specified handler\'s arguments number " r"must be 2 \(actual: 1\)",
        handler=_test_handler_1,
    )
    assert_raises(
        expected_error_class=ValueError,
        callable_=handler_validation.validate_handler_args_num,
        match="\nTest error!",
        handler=_test_handler_1,
        additional_err_msg="Test error!",
    )

    handler_validation.validate_handler_args_num(handler=_test_handler_2)
    handler_validation.validate_handler_args_num(handler=_test_handler_3)


_HANDLER_SOURCE_1: str = """
def on_timer(e: ap.TimerEvent, options: dict) -> None:
    print(100)
""".strip()

_HANDLER_SOURCE_2: str = """
def on_timer(e, options):
    print(200)
""".strip()

_HANDLER_SOURCE_3: str = """
def on_timer(
        e, options):
    print(300)
""".strip()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_handlers_name_and_args_from_source() -> None:
    source: str = handler_validation._remove_handlers_name_and_args_from_source(
        source=_HANDLER_SOURCE_1
    )
    assert source == "    print(100)"

    source = handler_validation._remove_handlers_name_and_args_from_source(
        source=_HANDLER_SOURCE_2
    )
    assert source == "    print(200)"

    source = handler_validation._remove_handlers_name_and_args_from_source(
        source=_HANDLER_SOURCE_3
    )
    assert source == "    print(300)"


def _test_handler_4(e: ap.TimerEvent, options: dict) -> None:
    """
    Lorem ipsum dolor.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    print(400)


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_docstring_from_source() -> None:
    source: str = handler_validation._remove_docstring_from_source(
        docstring=None, source="    print(600)"
    )
    assert source == "    print(600)"

    source = inspect.getsource(_test_handler_4)
    source = handler_validation._remove_handlers_name_and_args_from_source(
        source=source
    )
    source = handler_validation._remove_docstring_from_source(
        docstring=_test_handler_4.__doc__, source=source
    )
    assert source == "    print(400)"


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_validate_in_handler_assignment() -> None:
    def _test_handler_1(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        """
        Lorem ipsum dolor sit amet, consect et.

        Parameters
        ----------
        e : ap.MouseEvent[ap.Rectangle]
            Event instance.
        options : dict
            Optional arguments dictionary.
        """
        test_int: int = 10 + 20
        ap.trace(test_int)

    handler_validation.validate_in_handler_assignment(handler=_test_handler_1)

    def _test_handler_2(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        """
        Lorem ipsum dolor sit amet, consect et.

        Parameters
        ----------
        e : ap.MouseEvent[ap.Rectangle]
            Event instance.
        options : dict
            Optional arguments dictionary.
        """
        test_int: ap.Int = ap.Int(10)
        ap.trace(test_int)

    assert_raises(
        expected_error_class=InvalidAssignmentInHandler,
        callable_=handler_validation.validate_in_handler_assignment,
        handler=_test_handler_2,
        match="test_int.value = ap.Int(...)",
    )

    def _test_handler_3(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        """
        Lorem ipsum dolor sit amet, consect et.

        Parameters
        ----------
        e : ap.MouseEvent[ap.Rectangle]
            Event instance.
        options : dict
            Optional arguments dictionary.
        """
        e.this.x = ap.Int(50)

    handler_validation.validate_in_handler_assignment(handler=_test_handler_3)


_TEST_SOURCE_1: str = """
    test_int_1: int = 10 + 20
    test_int_2: ap.Int = ap.Int(30)
    test_int_3 = 40
""".strip()

_EXPECTED_SOURCE_1: str = """
    test_int_1 = 10 + 20
    test_int_2 = ap.Int(30)
    test_int_3 = 40
""".strip()


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test__remove_type_annotation_from_source_variable() -> None:
    source: str = handler_validation._remove_type_annotation_from_source_variable(
        source=_TEST_SOURCE_1
    )
    assert source == _EXPECTED_SOURCE_1
