"""The validation utilities for a matrix data.
"""

from typing import Dict, List, Union


def validate_matrix_list_data(
    *,
    matrix_list_data: List[Dict[str, Union[int, float, str]]],
    additional_err_msg: str = "",
) -> None:
    """
    Validate whether a specified matrix list data is valid type or not.

    Parameters
    ----------
    matrix_list_data : List[Dict[str, Union[int, float, str]]]
        A matrix list data.
    additional_err_msg : str, optional
        An additional error message to display.

    Raises
    ------
    TypeError
        - If a specified data type is not the list.
        - If values are not type of dict.
        - If a dictionary key's type is not the str.
        - If a dictionary value's type is not the int, float, or str.
    """
    from apysc._validation import validation_common_utils

    if not isinstance(matrix_list_data, list):
        err_msg: str = (
            f"A specified data type is not the list: {type(matrix_list_data).__name__} "
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
                    "A specified dict value type is not the int, float, or str: "
                    f"{type(value).__name__}\n{value}"
                )
                err_msg = validation_common_utils.append_additional_err_msg(
                    err_msg=err_msg,
                    additional_err_msg=additional_err_msg,
                )
                raise TypeError(err_msg)
