"""The mix-in class implementation for the `String`'s
`apply_max_num_of_decimal_places` method.
"""

import re
from typing import TYPE_CHECKING
from typing import Any
from typing import Match
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._type.int import Int
    from apysc._type.string import String


class StringApplyMaxNumOfDecimalPlacesMixIn:
    @final
    @arg_validation_decos.is_string(arg_position_index=0, optional=False)
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def apply_max_num_of_decimal_places(
        self,
        *,
        max_num_of_decimal_places: Union[int, "Int"],
        variable_name_suffix: str = "",
    ) -> "String":
        """
        Apply a maximum number of decimal places limit to this string.

        Parameters
        ----------
        max_num_of_decimal_places : Union[int, Int]
            A maximum number of decimal places.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        string : String
            An applied string.

        References
        ----------
        - String class apply_max_num_of_decimal_places interface
            - https://simon-ritchie.github.io/apysc/en/string_apply_max_num_of_decimal_places.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> string = ap.String("123.456")
        >>> string = string.apply_max_num_of_decimal_places(max_num_of_decimal_places=1)
        >>> ap.assert_equal(string, "123.4")
        """
        from apysc._expression import expression_data_util
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._type.int import Int
        from apysc._type.string import String
        from apysc._validation import variable_name_validation

        if not isinstance(max_num_of_decimal_places, Int):
            max_num_of_decimal_places_: Int = Int(
                max_num_of_decimal_places, variable_name_suffix=variable_name_suffix
            )
        else:
            max_num_of_decimal_places_ = max_num_of_decimal_places
        string: String = String("", variable_name_suffix=variable_name_suffix)
        string._value = _get_py_str(
            max_num_of_decimal_places=max_num_of_decimal_places_,
            self_str=self,
        )

        self_variable_name: str = (
            variable_name_validation.validate_variable_name_mixin_type(
                instance=self
            ).variable_name
        )
        matched_variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.MATCHED,
        )
        expression: str = (
            f"var {matched_variable_name} = {self_variable_name}"
            f'.match(new RegExp("^(\\\\d+\\\\.\\\\d{{"'
            f' + {max_num_of_decimal_places_.variable_name} + "}})\\\\d*$"));'
            f"\nif ({matched_variable_name}) {{"
            f"\n  {string.variable_name} = {matched_variable_name}[1];"
            "\n} else {"
            f"\n  {string.variable_name} = {self_variable_name};"
            "\n}"
        )
        expression_data_util.append_js_expression(expression=expression)

        return string


@add_debug_info_setting(module_name=__name__)
@arg_validation_decos.is_apysc_integer(arg_position_index=0)
def _get_py_str(
    *,
    max_num_of_decimal_places: "Int",
    self_str: Any,
) -> str:
    """
    Get a Python value string.

    Parameters
    ----------
    max_num_of_decimal_places : Int
        A maximum number of decimal places.
    self_str : Any
        A self `String` instance.

    Returns
    -------
    py_str : str
        A Python value string.
    """
    from apysc._type.string import String

    py_str: str = ""
    if isinstance(self_str, String):
        py_str = self_str._value
    match_: Optional[Match] = re.match(
        pattern=rf"^(\d+\.\d{{{max_num_of_decimal_places._value}}})\d*$",
        string=py_str,
    )
    if match_ is not None:
        py_str = match_.group(1)
    return py_str
