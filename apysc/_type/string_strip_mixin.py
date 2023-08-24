"""The mix-in class implementation for the `strip` method.
"""

from typing import TYPE_CHECKING
from typing import Any
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._type.string import String


class StringStripMixIn:
    @final
    @arg_validation_decos.is_apysc_string(arg_position_index=0)
    @arg_validation_decos.is_string(arg_position_index=1, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def strip(
        self,
        *,
        string: Optional[Union[str, "String"]] = None,
        variable_name_suffix: str = "",
    ) -> "String":
        """
        Remove a specified character or string from left- and right-edges.

        Parameters
        ----------
        string : Optional[Union[str, "String"]], optional
            A character or string to remove from the beginning and end of the
            this value. If this argument is `None` (default), this method
            removes spaces and line breaks.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        result : String
            A stripped result string.

        References
        ----------
        - String class strip interface
            - https://simon-ritchie.github.io/apysc/en/string_strip.html

        Examples
        --------
        >>> import apysc as ap

        >>> _ = ap.Stage()
        >>> string: ap.String = ap.String("   aabbcc   ")
        >>> string = string.strip()
        >>> string
        String("aabbcc")

        >>> string = ap.String("aabbccaa")
        >>> string = string.strip(string="a")
        >>> string
        String("bbcc")
        """
        from apysc._expression import expression_data_util
        from apysc._type.string import String
        from apysc._type.variable_name_mixin import VariableNameMixIn

        result: String = String("", variable_name_suffix=variable_name_suffix)
        self_variable_name: str = ""
        if isinstance(self, VariableNameMixIn):
            self_variable_name = self.variable_name
        if string is None:
            expression: str = _create_string_none_case_expression(
                result_string=result,
                self_variable_name=self_variable_name,
            )
        else:
            expression = _create_string_not_none_case_expression(
                result_string=result,
                removing_string=string,
                self_variable_name=self_variable_name,
                variable_name_suffix=variable_name_suffix,
            )
        expression_data_util.append_js_expression(expression=expression)
        py_str: str = _get_py_str_from_current_value(
            self_str=self,
            removing_string=string,
        )
        result._value = py_str
        return result


@arg_validation_decos.is_apysc_string(arg_position_index=0)
@arg_validation_decos.is_string(arg_position_index=1, optional=True)
def _get_py_str_from_current_value(
    *,
    self_str: Any,
    removing_string: Optional[Union[str, "String"]],
) -> str:
    """
    Get a Python string from a current string value.

    Parameters
    ----------
    self_str : Any
        A self-string.
    removing_string : Optional[Union[str, "String"]]
        A removing target string.

    Returns
    -------
    py_str : str
        A Python string.
    """
    from apysc._type.string import String

    py_str: str = ""
    if isinstance(self_str, String):
        py_str = self_str._value
    if removing_string is None:
        py_str = (
            py_str.strip()
            .strip("\\r\\n")
            .strip("\\n")
            .strip("\\r")
            .strip("\\t")
            .strip()
        )
        return py_str
    if isinstance(removing_string, String):
        py_str = py_str.strip(removing_string._value)
        return py_str
    if isinstance(removing_string, str):
        py_str = py_str.strip(removing_string)
    return py_str


@arg_validation_decos.is_apysc_string(arg_position_index=0)
@arg_validation_decos.is_string(arg_position_index=1, optional=False)
@arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
@arg_validation_decos.is_builtin_string(arg_position_index=3, optional=False)
def _create_string_not_none_case_expression(
    *,
    result_string: "String",
    removing_string: Union[str, "String"],
    self_variable_name: str,
    variable_name_suffix: str,
) -> str:
    """
    Create an expression for the string's not `None` case.

    Parameters
    ----------
    result_string : String
        A result string.
    removing_string : Union[str, "String"]
        A removing target string.
    self_variable_name : str
        An instance's self-variable name.
    variable_name_suffix : str
        A JavaScript variable name suffix string.
        This setting is sometimes useful for JavaScript debugging.

    Returns
    -------
    expression : str
        A created expression.
    """
    from apysc._type.string import String

    if not isinstance(removing_string, String):
        removing_string_: String = String(
            removing_string, variable_name_suffix=variable_name_suffix
        )
    else:
        removing_string_ = removing_string
    expression: str = (
        f"{result_string.variable_name} = {self_variable_name}"
        f'.replace(new RegExp(`^(${{{removing_string_.variable_name}}})+`), "");'
        f"\n{result_string.variable_name} = {result_string.variable_name}"
        f'.replace(new RegExp(`(${{{removing_string_.variable_name}}})+$`), "");'
    )
    return expression


@arg_validation_decos.is_apysc_string(arg_position_index=0)
@arg_validation_decos.is_builtin_string(arg_position_index=1, optional=False)
def _create_string_none_case_expression(
    *,
    result_string: "String",
    self_variable_name: str,
) -> str:
    """
    Create an expression for the string's `None` case.

    Parameters
    ----------
    result_string : String
        A result string.
    self_variable_name : str
        An instance's self-variable name.

    Returns
    -------
    expression : str
        A created expression.
    """
    expresion: str = f"{result_string.variable_name} = {self_variable_name}.trim();"
    return expresion
