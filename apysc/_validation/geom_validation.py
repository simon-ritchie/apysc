"""This module is for the geometry-related values' validation
helper interfaces.
"""

from typing import Any


def validate_point_2d_type(*, point: Any, additional_err_msg: str = "") -> None:
    """
    Validate specified value's type is Point2D.

    Parameters
    ----------
    point : Point2D
        Point2D instance to be checked.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value's type is not Point2D.
    """
    from apysc._geom.point2d import Point2D
    from apysc._validation import validation_common_utils

    if isinstance(point, Point2D):
        return
    err_msg: str = f"Specified value's type is not Point2D: {type(point)}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)
