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
    import apysc as ap

    if isinstance(point, ap.Point2D):
        return
    if additional_err_msg != "":
        additional_err_msg = f"\n{additional_err_msg}"
    raise ValueError(
        f"Specified value's type is not Point2D: {type(point)}" f"{additional_err_msg}"
    )
