"""The mix-in class for the `to_hex` method.
"""

from typing import Union
from apysc._type.string import String
from typing_extensions import final
from apysc._validation import arg_validation_decos
from apysc._html.debug_mode import add_debug_info_setting


class ToHexMixIn:

    @final
    @arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def to_hex(self, *, variable_name_suffix: str = "") -> String:
        """
        Get a hexadecimal string (e.g., "1f").

        Notes
        -----
        This method ignores floating point numbers.

        Parameters
        ----------
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        hex_str : String
            A hexadecimal string (e.g., "1f").
        """
        from apysc._type.int import Int
        from apysc._type.number import Number
        from apysc._validation import number_validation
        from apysc._math.math import Math
        from apysc._expression import expression_data_util

        int_or_num: Union[
            Int, Number
        ] = number_validation.validate_apysc_int_or_number(value=self)
        hex_py_str: str = hex(int(int_or_num._value)).replace("0x", "", 1)
        truncated_int: Int = Math.trunc(int_or_num)
        hex_str: String = String("", variable_name_suffix=variable_name_suffix)
        hex_str._value = hex_py_str
        expression: str = (
            f"{hex_str.variable_name} = {truncated_int.variable_name}.toString(16);"
        )
        expression_data_util.append_js_expression(expression=expression)
        return hex_str
