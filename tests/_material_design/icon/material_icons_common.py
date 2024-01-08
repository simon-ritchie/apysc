"""
The common constants and utilities for the material icons' testing.
"""

from typing import Type

import apysc as ap


def assert_constructor(
    *,
    icon_class: Type,
    expected_variable_name: str,
) -> None:
    """
    Assert the specified icon class's constructor.

    Parameters
    ----------
    icon_class : Type[ap.MaterialIconBase]
        A target icon class to assert.
    expected_variable_name : str
        An expected variable name.
    """
    icon: ap.MaterialIconBase = icon_class(
        fill_color=ap.Colors.WHITE_FFFFFF,
        fill_alpha=0.5,
        x=100,
        y=150,
        width=40,
        height=50,
        variable_name_suffix="test_suffix",
    )
    assert icon._fill_color == ap.Colors.WHITE_FFFFFF
    assert icon._fill_alpha._value == 0.5
    assert icon._x._value == 100
    assert icon._y._value == 150
    assert icon._width._value == 40
    assert icon._height._value == 50
    assert expected_variable_name in icon.variable_name
    assert "test_suffix" in icon._variable_name_suffix
