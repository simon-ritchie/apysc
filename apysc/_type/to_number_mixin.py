"""The mix-in class implementation for the `to_number` method.
"""

from typing import TYPE_CHECKING

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting

if TYPE_CHECKING:
    from apysc._type.number import Number


class ToNumberMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def to_number(self, *, variable_name_suffix: str = "") -> "Number":
        """
        Convert this value to an `ap.Number` value.

        Parameters
        ----------
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        number : Number
            A converted number.
        """
        import apysc as ap
        from apysc._validation.variable_name_validation import (
            validate_variable_name_mixin_type,
        )

        self_variable_name: str = validate_variable_name_mixin_type(
            instance=self
        ).variable_name
        number: ap.Number = ap.Number(0.0, variable_name_suffix=variable_name_suffix)
        py_value: float = 0
        if isinstance(self, (ap.Int, ap.String, ap.Boolean)):
            py_value = float(self._value)
        number._value = py_value
        expression: str = f"{number.variable_name} = Number({self_variable_name});"
        ap.append_js_expression(expression=expression)

        return number
