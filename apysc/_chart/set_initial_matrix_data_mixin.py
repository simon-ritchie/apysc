"""The mix-in class implementation for the `_set_initial_matrix_data` method.
"""

from typing import Dict
from typing import List
from typing import Union
from typing import cast

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.dictionary import Dictionary
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._validation import arg_validation_decos

_DataType = Union[
    Array[Dictionary[String, Union[Int, Number, String]]],
    List[Dict[str, Union[int, float, str]]],
]


class SetInitialMatrixDataMixIn:
    _matrix_data: Array[Dictionary[String, Union[Int, Number, String]]]

    @final
    @arg_validation_decos.is_list_or_array_matrix_data(arg_position_index=1)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_matrix_data(
        self,
        *,
        data: _DataType,
        variable_name_suffix: str,
    ) -> None:
        """
        Set an initial matrix data.

        Parameters
        ----------
        data : _DataType
            A data array, which contains a 1-dimensional string key dictionary.
            A list of dictionaries or an `ap.Array` of `ap.Dictionary` values
            are acceptable.
            E.g., `[{"column_name_1": 10, "column_name_2"}]`
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(data, Array):
            data_: Array[Dictionary[String, Union[Int, Number, String]]] = (
                _convert_list_to_array(
                    data=cast(List[Dict[str, Union[int, float, str]]], data),
                    variable_name_suffix=variable_name_suffix,
                )
            )
        else:
            data_ = data
        self._matrix_data = data_


def _convert_list_to_array(
    *,
    data: List[Dict[str, Union[int, float, str]]],
    variable_name_suffix: str,
) -> Array[Dictionary[String, Union[Int, Number, String]]]:
    """
    Convert a specified matrix list to an array.

    Parameters
    ----------
    data : List[Dict[str, Union[int, float, str]]]
        A matrix list.
    variable_name_suffix : str, optional
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    data__ : Array[Dictionary[String, Union[Int, Number, String]]]:
        A converted array.
    """
    data_: List[Dictionary[String, Union[Int, Number, String]]] = []
    for dict_data in data:
        dict_data_: Dict[String, Union[Int, Number, String]] = {}
        for key, value in dict_data.items():
            key_: String = String(key, variable_name_suffix=variable_name_suffix)
            if isinstance(value, int):
                dict_data_[key_] = Int(value, variable_name_suffix=variable_name_suffix)
                continue
            if isinstance(value, float):
                dict_data_[key_] = Number(
                    value, variable_name_suffix=variable_name_suffix
                )
                continue
            if isinstance(value, str):
                dict_data_[key_] = String(
                    value, variable_name_suffix=variable_name_suffix
                )
                continue
        data_.append(Dictionary(dict_data_, variable_name_suffix=variable_name_suffix))
    data__: Array[Dictionary[String, Union[Int, Number, String]]] = Array(
        data_, variable_name_suffix=variable_name_suffix
    )
    return data__
