"""The mix-in class implementation for the `slice` method.
"""

from typing import TYPE_CHECKING
from typing import Optional
from typing import Union
from typing import cast

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._type.int import Int
    from apysc._type.string import String


class StringSliceMixIn:
    @final
    @arg_validation_decos.is_apysc_string(arg_position_index=0)
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=2, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def slice(
        self,
        *,
        start: Union[int, "Int"],
        end: Optional[Union[int, "Int"]] = None,
        variable_name_suffix: str = "",
    ) -> "String":
        """
        Get a sliced string based on the specified arguments range.

        Parameters
        ----------
        start : Union[int, "Int"]
            A start index of the slice range.
        end : Optional[Union[int, "Int"]], optional
            An end index of the slice range. If this argument is
            not specified, this method skips the end position's slicing.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        result : String
            A sliced result string.

        References
        ----------
        - String class slice method
            - https://simon-ritchie.github.io/apysc/en/string_slice.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     stage_width=0,
        ...     stage_height=0,
        ...     background_color=ap.Color("#333"),
        ...     stage_elem_id="stage",
        ... )

        >>> string: ap.String = ap.String("012345")
        >>> result_string: ap.String = string.slice(start=0)
        >>> result_string
        String("012345")

        >>> result_string = string.slice(start=1)
        >>> result_string
        String("12345")

        >>> result_string = string.slice(start=0, end=2)
        >>> result_string
        String("01")

        >>> result_string = string.slice(start=2, end=4)
        >>> result_string
        String("23")

        >>> result_string = string.slice(start=-2)
        >>> result_string
        String("45")

        >>> result_string = string.slice(start=-3, end=-1)
        >>> result_string
        String("34")
        """
        from apysc._converter.to_apysc_val_from_builtin import (
            get_copied_int_from_builtin_val,
        )
        from apysc._expression import expression_data_util
        from apysc._type.int import Int
        from apysc._type.string import String
        from apysc._validation.string_validation import validate_apysc_string_type

        result: String = String("", variable_name_suffix=variable_name_suffix)
        self_string: String = validate_apysc_string_type(string=self)
        start_ap_int: Int = get_copied_int_from_builtin_val(integer=start)
        end_ap_int: Optional[Int] = None
        if end is not None:
            end_ap_int = get_copied_int_from_builtin_val(integer=end)
            result._value = self_string._value[
                start_ap_int._value : cast(Int, end_ap_int)._value
            ]
        else:
            result._value = self_string._value[start_ap_int._value :]

        expression: str = f"{result.variable_name} = {self_string.variable_name}.slice("
        if end_ap_int is not None:
            expression += f"{start_ap_int.variable_name}, {end_ap_int.variable_name}"
        else:
            expression += f"{start_ap_int.variable_name}"
        expression += ");"
        expression_data_util.append_js_expression(expression=expression)

        return result
