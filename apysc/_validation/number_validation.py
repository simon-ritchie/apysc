"""Number validation implementations.

Mainly following interfaces are defined:

- validate_num
    - Validate a specified value as an integer or float type.
- validate_integer
    - Validate whether a specified value is an integer or not.
- validate_builtin_integer
    - Validate whether a specified value is a built-in integer or not.
- validate_int_is_zero_or_one
    - Validate specified integer value is zero or one.
- validate_num_is_gt_zero
    - Validate specified value is greater than zero.
- validate_num_is_gte_zero
    - Validate whether a specified value is greater than or
    equal to zero.
- validate_num_is_0_to_1_range
    - Validate whether a specified number is from 0.0 to 1.0.
- validate_apysc_int_or_number
    - Validate whether a specified value is an apysc's `Int` or `Number`.
"""

from typing import Any
from typing import Union

from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.number_value_mixin import NumberValueMixIn


def validate_num(
    *, num: Union[int, float, Int, Number], additional_err_msg: str = ""
) -> None:
    """
    Validate a specified value as an integer or float type.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is not an integer and float value.
    """
    from apysc._validation import validation_common_utils

    if isinstance(num, (int, float, NumberValueMixIn)):
        return
    err_msg: str = (
        f"Specified value is not iteger or float type: {num}" f"({type(num)})"
    )
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_integer(*, integer: Union[int, Int], additional_err_msg: str = "") -> None:
    """
    Validate whether a specified value is an integer or not.

    Parameters
    ----------
    integer : Int or int
        Integer value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is not an integer.
    """
    from apysc._validation import validation_common_utils

    if isinstance(integer, (int, Int)):
        return
    err_msg: str = f"A specified value is not an integer: {integer}({type(integer)})"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_builtin_integer(*, integer: int, additional_err_msg: str = "") -> None:
    """
    Validate whether a specified value is a built-in integer or not.

    Parameters
    ----------
    integer : int
        A target integer to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is not a built-in integer.
    """
    from apysc._validation import validation_common_utils

    if isinstance(integer, int):
        return
    err_msg: str = (
        "A specified value is not a built-in integer: " f"{integer}({type(integer)})"
    )
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_int_is_zero_or_one(*, integer: Union[int, Int]) -> None:
    """
    Validate specified integer value is zero or one.

    Notes
    -----
    This interface skips validation if an argument
    value is not an Int or int instance.

    Parameters
    ----------
    integer : Int or int
        Integer value to check.

    Raises
    ------
    ValueError
        If a specified integer is not zero and one.
    """
    if not isinstance(integer, (int, Int)):
        return
    if isinstance(integer, int):
        if integer == 0 or integer == 1:
            return
    elif isinstance(integer, Int):
        if integer._value == 0 or integer._value == 1:
            return
    raise ValueError(f"Specified integer value is not zero and one: {integer}")


def validate_num_is_gt_zero(
    *, num: Union[int, float, Int, Number], additional_err_msg: str = ""
) -> None:
    """
    Validate specified value is greater than zero.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is less than or equal to zero.
    """
    from apysc._validation import validation_common_utils

    if isinstance(num, NumberValueMixIn):
        if num._value > 0:
            return
    elif num > 0:
        return
    err_msg: str = f"Specified values is less than or equal to zero: {num}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_num_is_gte_zero(
    *, num: Union[int, float, Int, Number], additional_err_msg: str = ""
) -> None:
    """
    Validate whether a specified value is greater than or equal to zero.

    Parameters
    ----------
    num : int or float or Int or Number
        Number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified value is less than zero.
    """
    from apysc._validation import validation_common_utils

    if isinstance(num, NumberValueMixIn):
        if num._value >= 0:
            return
    elif num >= 0:
        return
    err_msg: str = f"Specified values is less than zero: {num}"
    err_msg = validation_common_utils.append_additional_err_msg(
        err_msg=err_msg, additional_err_msg=additional_err_msg
    )
    raise ValueError(err_msg)


def validate_num_is_0_to_1_range(
    *, num: Union[float, NumberValueMixIn], additional_err_msg: str = ""
) -> None:
    """
    Validate whether a specified number is from 0.0 to 1.0.

    Parameters
    ----------
    num : float or Number
        A number value to check.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    ValueError
        If a specified opacity is out of the 0.0 to 1.0 range.
    """
    from apysc._validation import validation_common_utils

    lt_err_msg: str = "Can't specify number value less than 0.0: "
    gt_err_msg: str = "Can't specify number value greater than 1.0: "
    if isinstance(num, NumberValueMixIn):
        if num._value < 0.0:
            err_msg: str = f"{lt_err_msg}{num}"
            err_msg = validation_common_utils.append_additional_err_msg(
                err_msg=err_msg, additional_err_msg=additional_err_msg
            )
            raise ValueError(err_msg)
        if num._value > 1.0:
            err_msg = f"{gt_err_msg}{num}"
            err_msg = validation_common_utils.append_additional_err_msg(
                err_msg=err_msg, additional_err_msg=additional_err_msg
            )
            raise ValueError(err_msg)
    else:
        if num < 0.0:
            err_msg = f"{lt_err_msg}{num}"
            err_msg = validation_common_utils.append_additional_err_msg(
                err_msg=err_msg, additional_err_msg=additional_err_msg
            )
            raise ValueError(err_msg)
        if num > 1.0:
            err_msg = f"{gt_err_msg}{num}"
            err_msg = validation_common_utils.append_additional_err_msg(
                err_msg=err_msg, additional_err_msg=additional_err_msg
            )
            raise ValueError(err_msg)


def validate_apysc_int_or_number(*, value: Any) -> Union[Int, Number]:
    """
    Validate whether a specified value is an apysc's `Int` or `Number`.

    Parameters
    ----------
    value : Any
        A value to check.

    Returns
    -------
    value : Union[Int, Number]
        An apysc's `Int` or `Number` value.
    """
    if not isinstance(value, (Int, Number)):
        raise TypeError(
            "A specified value type is not an apysc's `Int` or `Number`: "
            f"{type(value)}"
        )
    return value
