"""Common testing helper implementations.
"""

import os
from typing import Any, Dict


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
        If expected attribute value not exists.
    """
    for attr_name, expected_value in expected_attrs.items():
        msg: str = (
            'Expected attribute not exists.'
            f'\nAttribute name: {attr_name}'
        )
        assert hasattr(any_obj, attr_name), msg

        attr_val: Any = getattr(any_obj, attr_name)
        msg = (
            'Attribute value is different from expected value.'
            f'\nAttribute name: {attr_name}'
            f'\nAttribute value: {attr_val}'
            f'\nExpected value: {expected_value}'
        )
