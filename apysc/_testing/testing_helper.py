"""Common testing helper implementations.
"""

from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type

import pytest

from apysc._file import file_util


def make_blank_file(*, file_path: str) -> None:
    """
    Make a blank file. If there is no directory, also create
    a parent directory.

    Parameters
    ----------
    file_path : str
        File path to make.
    """
    file_util.save_plain_txt(txt="", file_path=file_path)


def _assert_has_attr(*, any_obj: Any, attr_name: str) -> None:
    """
    Check object has specified attribute.

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
