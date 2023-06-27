"""The validation utilities for matrix data.
"""

from typing import Dict
from typing import List
from typing import Union

from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


def validate_matrix_list_data(
    *,
    matrix_list_data: List[Dict[str, Union[int, float, str]]],
    additional_err_msg: str = "",
) -> None:
    """
    Validate whether a specified matrix list data is a valid type or not.

    Parameters
    ----------
    matrix_list_data : List[Dict[str, Union[int, float, str]]]
        A matrix list data.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    TypeError
        - If a specified data type is not a list.
        - If values are not type of dict.
        - If a dictionary key's type is not str.
        - If a dictionary value's type is not int, float, or str.
    """
    from apysc._validation import validation_common_utils

    if not isinstance(matrix_list_data, list):
        err_msg: str = (
            f"A specified data type is not a list: {type(matrix_list_data).__name__} "
            f"\n{matrix_list_data}"
        )
        err_msg = validation_common_utils.append_additional_err_msg(
            err_msg=err_msg,
            additional_err_msg=additional_err_msg,
        )
        raise TypeError(err_msg)

    for data in matrix_list_data:
        if not isinstance(data, dict):
            err_msg = (
                "A specified list value's type is not the dict: "
                f"{type(data).__name__}\n{data}"
            )
            err_msg = validation_common_utils.append_additional_err_msg(
                err_msg=err_msg,
                additional_err_msg=additional_err_msg,
            )
            raise TypeError(err_msg)
        for key, value in data.items():
            if not isinstance(key, str):
                err_msg = (
                    "A specified dict key type is not the str: "
                    f"{type(key).__name__}\n{key}"
                )
                err_msg = validation_common_utils.append_additional_err_msg(
                    err_msg=err_msg,
                    additional_err_msg=additional_err_msg,
                )
                raise TypeError(err_msg)
            if not isinstance(value, (int, float, str)):
                err_msg = (
                    "A specified dict value type is not int, float, or str: "
                    f"{type(value).__name__}\n{value}"
                )
                err_msg = validation_common_utils.append_additional_err_msg(
                    err_msg=err_msg,
                    additional_err_msg=additional_err_msg,
                )
                raise TypeError(err_msg)


def validate_matrix_array_data(
    *,
    matrix_array_data: Array[Dictionary[String, Union[Int, Number, String]]],
    additional_err_msg: str,
) -> None:
    """
    Validate whether a specified matrix array data is a valid type or not.

    Parameters
    ----------
    matrix_array_data : Array[Dictionary[String, Union[Int, Number, String]]]
        A matrix array data.
    additional_err_msg : str
        An additional error message to display.

    Raises
    ------
    TypeError
        - If a specified data type is not `ap.Array`.
        - If values are not the type of the `ap.Dictionary`.
        - If a dictionary key's type is not `ap.String`.
        - If a dictionary value's type is not `ap.Int`, `ap.Number`, or `ap.String`.
    """
    from apysc._validation import validation_common_utils

    if not isinstance(matrix_array_data, Array):
        err_msg: str = (
            "A specified data type is not `ap.Array`: "
            f"{type(matrix_array_data).__name__}\n{matrix_array_data}"
        )
        err_msg = validation_common_utils.append_additional_err_msg(
            err_msg=err_msg,
            additional_err_msg=additional_err_msg,
        )
        raise TypeError(err_msg)

    for data in matrix_array_data._value:
        if not isinstance(data, Dictionary):
            err_msg = (
                "A specified `ap.Array` value's type is not the `ap.Dictionary`: "
                f"{type(data).__name__}\n{data}"
            )
            err_msg = validation_common_utils.append_additional_err_msg(
                err_msg=err_msg,
                additional_err_msg=additional_err_msg,
            )
            raise TypeError(err_msg)
        for key, value in data._value.items():
            if not isinstance(key, String):
                err_msg = (
                    "A specified dictionary key type is not the `ap.String`: "
                    f"{type(key).__name__}\n{key}"
                )
                err_msg = validation_common_utils.append_additional_err_msg(
                    err_msg=err_msg,
                    additional_err_msg=additional_err_msg,
                )
                raise TypeError(err_msg)
            if not isinstance(value, (Int, Number, String)):
                err_msg = (
                    "A specified dictionary value type is not `ap.Int`, "
                    f"`ap.Number`, or `ap.String`: {type(value).__name__}\n{value}"
                )
                err_msg = validation_common_utils.append_additional_err_msg(
                    err_msg=err_msg,
                    additional_err_msg=additional_err_msg,
                )
                raise TypeError(err_msg)
