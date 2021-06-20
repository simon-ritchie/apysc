"""Validation helper interfaces for geometry related values.
"""


from typing import Any


def validate_point_2d_type(point: Any) -> None:
    """
    Validate specified value's type is Point2D.

    Parameters
    ----------
    point : Point2D
        Point2D instance to be checked.

    Raises
    ------
    ValueError
        If scpecified value's type is not Point2D.
    """
    from apysc import Point2D
    if isinstance(point, Point2D):
        return
    raise ValueError(
        f'Specified value\'s type is not Point2D: {type(point)}')
