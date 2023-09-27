"""The mix-in class for the String's `zfill` method.
"""

from typing import TYPE_CHECKING
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._type.int import Int
    from apysc._type.string import String


class StringZfillMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    def zfill(self, *, width: Union[int, "Int"]) -> "String":
        """
        Return a copy of the string left filled with 0.

        Parameters
        ----------
        width : Union[int, "Int"]
            A width (length) of the string.

        Returns
        -------
        result : String
            A result string.

        References
        ----------
        - String class zfill method
            - https://simon-ritchie.github.io/apysc/en/string_zfill.html

        Examples
        --------
        >>> import apysc as ap
        >>> _: ap.Stage = ap.Stage()
        >>> string: ap.String = ap.String("1")
        >>> string = string.zfill(width=1)
        >>> string
        String("1")

        >>> string = string.zfill(width=3)
        >>> string
        String("001")

        >>> string = string.zfill(width=5)
        >>> string
        String("00001")
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )
        from apysc._expression.expression_data_util import append_js_expression
        from apysc._type.int import Int
        from apysc._type.string import String
        from apysc._validation import string_validation

        self_string: String = string_validation.validate_apysc_string_type(
            string=self,
        )
        result: String = self_string._copy()
        width_: Int = get_copied_int_from_builtin_val(integer=width)
        result._value = result._value.zfill(width_._value)

        expression: str = (
            f"{result.variable_name} = {self_string.variable_name}"
            f'.padStart({width_.variable_name}, "0");'
        )
        append_js_expression(expression=expression)

        return result
