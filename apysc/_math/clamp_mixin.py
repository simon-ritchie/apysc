"""Class implementation for the clamp-related mix-in.
"""

from typing import Any, cast
from typing import List
from typing import Union
from typing import Generic, TypeVar

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._validation import arg_validation_decos

_ValueType = TypeVar('_ValueType', Int, Number)


class ClampMixIn:
    @classmethod
    @final
    @arg_validation_decos.is_apysc_int_or_number(arg_position_index=1)
    @arg_validation_decos.is_apysc_int_or_number(arg_position_index=2)
    @arg_validation_decos.is_apysc_int_or_number(arg_position_index=3)
    @add_debug_info_setting(module_name=__name__)
    def clamp(
        cls, *, value: _ValueType, min_: _ValueType, max_: _ValueType) -> _ValueType:
        """
        Sets the value within a specified minimum and maximum range.
        If the value is less than the minumum, this method returns the minimum value.
        If the value is greater than the maximum, this method returns the
        maximum value.

        Parameters
        ----------
        value : _ValueType
            Target `Int` or `Number` value.
        min_ : _ValueType
            Minimum value.
        max_ : _ValueType
            Maximum value.

        Returns
        -------
        result : _ValueType
            Clamped value.
        """
        from apysc._math.math import Math
        from apysc._type.array import Array

        py_value: Union[int, float] = value._value
        py_value = min(py_value, max_._value)
        py_value = max(py_value, min_._value)

        result: _ValueType = cast(_ValueType, Math.min(values=Array([value, max_])))
        result = cast(_ValueType, Math.max(values=Array([result, min_])))
        result._value = py_value  # type: ignore
        return result
