"""The mix-in class implementation for the `to_fixed` method.
"""

from typing import TYPE_CHECKING
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._type.int import Int


class ToFixedMixIn:
    @final
    @arg_validation_decos.is_apysc_int_or_number(arg_position_index=0)
    @arg_validation_decos.num_is_between(
        arg_position_index=1, min_value=0, max_value=100
    )
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def to_fixed(
        self,
        *,
        digits: Union[int, "Int"],
        variable_name_suffix: str = "",
    ) -> String:
        """
        Convert value to fixed floating point string notation.

        Parameters
        ----------
        digits : int or Int
            A floating point digit number (0 to 100 value is acceptable).
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        result_str : String
            A converted string.

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage()
        >>> num: ap.Number = ap.Number(10.789)
        >>> fixed_float_str: ap.String = num.to_fixed(digits=2)
        >>> fixed_float_str
        String("10.79")

        >>> fixed_float_str = num.to_fixed(digits=5)
        >>> fixed_float_str
        String("10.78900")

        >>> fixed_float_str = num.to_fixed(digits=0)
        >>> fixed_float_str
        String("11")
        """
        from apysc._expression import expression_data_util
        from apysc._type.int import Int
        from apysc._type.number import Number
        from apysc._type.variable_name_mixin import VariableNameMixIn

        result_str: String = String("", variable_name_suffix=variable_name_suffix)
        if isinstance(digits, int):
            digits_: Int = Int(digits, variable_name_suffix=variable_name_suffix)
        else:
            digits_ = digits
        variable_name: str = ""
        if isinstance(self, VariableNameMixIn):
            variable_name = self.variable_name
        expression: str = (
            f"{result_str.variable_name} = "
            f"{variable_name}.toFixed({digits_.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

        value: float = 0.0
        if isinstance(self, (Int, Number)):
            value = self._value
        value = round(value, digits_._value)
        py_fixed_floating_point_value: str = f"{value:.{digits_._value}f}"
        result_str._value = py_fixed_floating_point_value
        return result_str
