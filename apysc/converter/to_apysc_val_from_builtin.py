"""Each interfaces to get apysc values from Python built-in ones.
"""

from typing import Union

from apysc import Int


def get_copied_int_from_builtin_val(integer: Union[int, Int]) -> Int:
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
        copied: Int = Int(integer)
    else:
        copied = integer._copy()
    return copied
