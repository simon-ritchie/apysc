"""Each interfaces to get apysc values from Python built-in ones.
"""

from typing import Union

import apysc as ap


def get_copied_int_from_builtin_val(
        integer: Union[int, ap.Int]) -> ap.Int:
    """
    Get a copied Int value from Python built-in int.

    Parameters
    ----------
    integer : int or Int
        Target integer value.

    Returns
    -------
    copied : Int
        Copied Int value.
    """
    if isinstance(integer, int):
        copied: ap.Int = ap.Int(integer)
    else:
        copied = integer._copy()
    return copied
