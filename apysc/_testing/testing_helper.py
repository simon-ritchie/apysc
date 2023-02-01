# mypy: disable-error-code=type-var

"""Common testing helper implementations.
"""

import functools
import time
from random import randint
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type
from typing import TypeVar
from typing import cast

import pytest


def make_blank_file(*, file_path: str) -> None:
    """
    Make a blank file. If there is no directory, also create
    a parent directory.

    Parameters
    ----------
    file_path : str
        File path to make.
    """
    from apysc._file import file_util

    file_util.save_plain_txt(txt="", file_path=file_path)


def _assert_has_attr(*, any_obj: Any, attr_name: str) -> None:
    """
    Check object has a specified attribute.

    Parameters
    ----------
    any_obj : *
        Any object to check.
    attr_name : str
        Expected attribute name.
    """
    msg: str = "Expected attribute does not exists." f"\nAttribute name: {attr_name}"
    assert hasattr(any_obj, attr_name), msg


def assert_attrs(*, expected_attrs: Dict[str, Any], any_obj: Any) -> None:
    """
    Check a specified object's attributes.

    Parameters
    ----------
    expected_attrs : dict
        A dict that has attribute names in key and expected values in value.
    any_obj : *
        Any object to check.

    Raises
    ------
    AssertionError
        If an expected attribute value does not exist or differ.
    """
    for attr_name, expected_value in expected_attrs.items():
        _assert_has_attr(any_obj=any_obj, attr_name=attr_name)

        attr_val: Any = getattr(any_obj, attr_name)
        msg: str = (
            "Attribute value is different from expected value."
            f"\nAttribute name: {attr_name}"
            f"\nAttribute value: {attr_val}"
            f"\nExpected value: {expected_value}"
        )
        assert attr_val == expected_value, msg


def assert_attrs_type(*, expected_types: Dict[str, Type], any_obj: Any) -> None:
    """
    Check a specified object's attribute types.

    Parameters
    ----------
    expected_types : dict
        A dict that has attribute names in key and expected types in value.
    any_obj : *
        Any object to check.

    Raises
    ------
    AssertionError
        If any attribute type differs from an expected type.
    """
    for attr_name, expected_type in expected_types.items():
        _assert_has_attr(any_obj=any_obj, attr_name=attr_name)

        attr_val: Any = getattr(any_obj, attr_name)
        msg: str = (
            "Attribute type is different from expected type."
            f"\nAttribute name: {attr_name}"
            f"\nAttribute type: {type(attr_val)}"
            f"\nExpected type: {expected_type}"
        )
        assert isinstance(attr_val, expected_type), msg


def assert_raises(
    *,
    expected_error_class: type,
    callable_: Callable,
    match: Optional[str] = None,
    **kwargs: Any,
) -> None:
    """
    Check that a specified callable raises an exception.

    Parameters
    ----------
    expected_error_class : type
        Expected error class, for instance, ValueError, Exception, etc.
    callable_ : callable
        Target function or method.
    match : str or None, default None
        Error message's regular expression match pattern.
    **kwargs : dict, optional
        Keyword arguments to pass to the function or method.

    Raises
    ------
    AssertionError
        If a specified interface does not raise an error.
    """
    _kwargs: Dict[str, Any] = {}
    if match is not None:
        _kwargs["match"] = match
    with pytest.raises(expected_error_class, **_kwargs):  # type: ignore
        callable_(**kwargs)


# pyright: reportInvalidTypeVarUse=false
_Callable = TypeVar("_Callable", bound=Callable)


def apply_test_settings(
    *,
    retrying_max_attempts_num: int = 15,
    retrying_sleep_seconds: Optional[float] = None,
) -> _Callable:
    """
    Apply each test setting to a test function.
    This function is a decorator function.

    Parameters
    ----------
    retrying_max_attempts_num : int, optional
        A maximum number of retry attempts.
    retrying_sleep_seconds : Optional[float], optional
        A Sleep seconds of retrying (Maximum seconds is 10).

    Returns
    -------
    wrapped : Callable
        Wrapped callable object.

    Raises
    ------
    ValueError
        If a specified `retrying_sleep_seconds` is greater than 10.
    """
    if retrying_sleep_seconds is None:
        retrying_sleep_seconds = randint(10, 3000) / 1000
    _validate_retrying_sleep_seconds(retrying_sleep_seconds=retrying_sleep_seconds)
    retrying_sleep_seconds_: float = cast(float, retrying_sleep_seconds)

    def wrapped(callable_: _Callable) -> _Callable:
        @functools.wraps(callable_)
        def inner_wrapped(*args: Any, **kwargs: Any) -> Any:

            result: Any = None
            for i in range(retrying_max_attempts_num + 1):

                if i < retrying_max_attempts_num:
                    try:
                        result = callable_(*args, **kwargs)
                        break
                    except Exception:
                        time.sleep(retrying_sleep_seconds_)
                        continue
                result = callable_(*args, **kwargs)
                break
            return result

        return inner_wrapped  # type: ignore

    return wrapped  # type: ignore


def _validate_retrying_sleep_seconds(*, retrying_sleep_seconds: float) -> None:
    """
    Validate whether specified retrying sleep seconds is not greater than 10.

    Parameters
    ----------
    retrying_sleep_seconds : float
        Sleep seconds of retrying.

    Raises
    ------
    ValueError
        If a specified `retrying_sleep_seconds` is greater than 10.
    """
    if retrying_sleep_seconds <= 10:
        return
    raise ValueError(
        "A specified `retrying_sleep_seconds` argument is greater than 10: "
        f"{retrying_sleep_seconds}"
    )
