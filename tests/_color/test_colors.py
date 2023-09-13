import inspect
from typing import Any
from typing import List
from typing import Type

import apysc as ap
from apysc._color import colors
from apysc._testing.testing_helper import apply_test_settings


def _assert_constants_names_are_uppercase(*, object: Any) -> None:
    """
    Assert the specified object's all constants are uppercase.

    Parameters
    ----------
    object : Any
        The target object to check constants.
    """
    for name, value in inspect.getmembers(object):
        if not isinstance(value, ap.Color):
            continue
        if not name.isupper():
            raise AssertionError(
                f"The specified object's constant name '{name}' " "is not uppercase."
            )


@apply_test_settings()
def test_assert_Colors_constsnts_are_uppercase() -> None:
    _assert_constants_names_are_uppercase(object=ap.Colors)


@apply_test_settings()
def test_all_module_constants_names_and_values_are_same() -> None:
    module_members: list[tuple[str, ap.Color]] = inspect.getmembers(
        colors,
        lambda x: isinstance(x, ap.Color),
    )
    member_value: ap.Color
    for member_name, member_value in module_members:
        expected_color_code_value: str = f"#{member_name.replace('_', '', 1).lower()}"
        assert member_value._value._value == expected_color_code_value


def _assert_constants_are_instances_of_color(*, object: Any) -> None:
    """
    Assert the specified object's all constants are instances of `Color`.

    Parameters
    ----------
    object : Any
        The target object to check constants.
    """
    members: list[tuple[str, Any]] = inspect.getmembers(object)
    for member_name, member_value in members:
        if member_name.startswith("_"):
            continue
        if callable(member_value):
            continue
        if isinstance(member_value, ap.Color):
            continue
        raise AssertionError(
            "The specified object's constant value is not an instance of "
            f"`Color`: `{type(member_value)}`"
        )


@apply_test_settings()
def test_assert_Colors_constsnts_are_instances_of_Color() -> None:
    _assert_constants_are_instances_of_color(object=ap.Colors)


def _assert_constants_suffixes_and_values_are_same(*, object: Any) -> None:
    """
    Assert the specified object's all constants suffixes
    and values' colors are same.

    Parameters
    ----------
    object : Any
        The target object to check constants.
    """
    for name, value in inspect.getmembers(object):
        if not isinstance(value, ap.Color):
            continue
        SUFFIX: str = name.split("_")[-1]
        assert f"#{SUFFIX.lower()}" == value._value._value


@apply_test_settings()
def test_assert_Colors_constsnts_suffixes_and_values_are_same() -> None:
    _assert_constants_suffixes_and_values_are_same(object=ap.Colors)


@apply_test_settings()
def test_assert_MaterialDesignColors_constants_are_uppercase() -> None:
    _assert_constants_names_are_uppercase(object=ap.MaterialDesignColors)


@apply_test_settings()
def test_assert_MaterialDesignColors_constants_are_instances_of_Color() -> None:
    _assert_constants_are_instances_of_color(object=ap.MaterialDesignColors)


@apply_test_settings()
def test_assert_MaterialDesignColors_constants_suffixes_and_values_are_same() -> None:
    _assert_constants_suffixes_and_values_are_same(object=ap.MaterialDesignColors)


_EXPECTED_MATERIAL_DESIGN_COLORS_NUMBERS: List[str] = [
    "50",
    "100",
    "200",
    "300",
    "400",
    "500",
    "600",
    "700",
    "800",
    "900",
    "A100",
    "A200",
    "A400",
    "A700",
]


def _assert_material_design_colors_numbers(*, class_: Type) -> None:
    """
    Assert the specified object's material design colors numbers
    are in expected string list (`_EXPECTED_MATERIAL_DESIGN_COLORS_NUMBERS`).

    Parameters
    ----------
    class_ : Type
        The target class to check constants.
    """
    for name, value in inspect.getmembers(object):
        if not isinstance(value, ap.Color):
            continue
        number_str: str = name.split("_")[-2]
        assert number_str in _EXPECTED_MATERIAL_DESIGN_COLORS_NUMBERS


@apply_test_settings()
def test_assert_MaterialDesignColors_numbers() -> None:
    _assert_material_design_colors_numbers(class_=ap.MaterialDesignColors)
