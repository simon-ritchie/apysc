"""Class implementation for the truncate-related mix-in.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String
from apysc._type.variable_name_suffix_mixin import VariableNameSuffixMixIn


class TruncMixIn:
    @classmethod
    @final
    @add_debug_info_setting(module_name=__name__)
    def trunc(cls, value: Union[Int, Number, String, Boolean]) -> Int:
        """
        Truncate a fraction value from a specified value.

        Parameters
        ----------
        value : Union[Int, Number, String, Boolean]
            A value to truncate a fraction value.
            If a specified value is the `Number`'s, `String`'s, or `Boolean`'s type,
            the return value becomes an `Int`'s value.

        Returns
        -------
        result : Int
            Truncated and converted to `Int`'s value.
        """
        import apysc as ap

        suffix: str = ""
        if isinstance(value, VariableNameSuffixMixIn):
            suffix = value._variable_name_suffix

        result: Int = Int(0, variable_name_suffix=suffix)
        if isinstance(value, (Int, Number, Boolean)):
            result._value = int(value._value)
        try:
            result._value = int(float(value._value))
        except Exception:
            pass
        expression: str = f"{result.variable_name} = Math.trunc({value.variable_name});"
        ap.append_js_expression(expression=expression)
        return result
