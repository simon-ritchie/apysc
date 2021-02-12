"""Common testing helper implementations.
"""

import os
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type

import pytest


def make_blank_file(file_path: str) -> None:
    """
    Make a blank file. If there is no directory of file, also create
    parent directory.

    Parameters
    ----------
    file_path : str
        File path to make.
    """
    dir_path: str = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(file_path)


def _assert_has_attr(any_obj: Any, attr_name: str) -> None:
    """
    Check object has specified attribute.

    Parameters
    ----------
    any_obj : *
        Any object to check.
    attr_name : str
        Expected attribute name.
    """
    msg: str = (
        'Expected attribute not exists.'
        f'\nAttribute name: {attr_name}'
    )
    assert hasattr(any_obj, attr_name), msg


def assert_attrs(expected_attrs: Dict[str, Any], any_obj: Any) -> None:
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
        If expected attribute value not exists or different.
    """
    for attr_name, expected_value in expected_attrs.items():
        _assert_has_attr(any_obj=any_obj, attr_name=attr_name)

        attr_val: Any = getattr(any_obj, attr_name)
        msg: str = (
            'Attribute value is different from expected value.'
            f'\nAttribute name: {attr_name}'
            f'\nAttribute value: {attr_val}'
            f'\nExpected value: {expected_value}'
        )
        assert attr_val == expected_value, msg


def assert_attrs_type(
        expected_types: Dict[str, Type], any_obj: Any) -> None:
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
        If any attribute type different from expected type.
    """
    for attr_name, expected_type in expected_types.items():
        _assert_has_attr(any_obj=any_obj, attr_name=attr_name)

        attr_val: Any = getattr(any_obj, attr_name)
        msg: str = (
            'Attribute type is different from expected type.'
            f'\nAttribute name: {attr_name}'
            f'\nAttribute type: {type(attr_val)}'
            f'\nExpected type: {expected_type}'
        )
        assert isinstance(attr_val, expected_type), msg


def assert_raises(
        expected_error_class: type, func_or_method: Callable,
        kwargs: Optional[Dict[str, Any]] = None) -> None:
    """
    Check that specified callable will raise exception.

    Parameters
    ----------
    expected_error_class : type
        Expected error class, for instance, ValueError, Exception, etc.
    func_or_method : callable
        Target function or method.
    kwargs : dict, optional
        Keyword arguments to pass to the function or method.

    Raises
    ------
    AssertionError
        If specified error not be raised.
    """
    if kwargs is None:
        kwargs = {}
    with pytest.raises(expected_error_class):  # type: ignore
        func_or_method(**kwargs)
