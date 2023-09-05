import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from typing import Any
import inspect


def _assert_all_constants_are_uppercase(*, object: Any) -> None:
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
                f"The specified object's constant name '{name}' "
                "is not uppercase."
            )


@apply_test_settings()
def test_check_Colors_constsnts_are_uppercase() -> None:
    _assert_all_constants_are_uppercase(object=ap.Colors)
