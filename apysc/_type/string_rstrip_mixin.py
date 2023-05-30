"""The mix-in class implementation for the `rstrip` method.
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


class StringRstripMixIn:
    @final
    @arg_validation_decos.is_apysc_string(arg_position_index=0)
    @arg_validation_decos.is_string(arg_position_index=1, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    def rstrip(
        self,
        *,
        string: Optional[Union[str, "String"]] = None,
        variable_name_suffix: str = "",
    ) -> "String":
        """
        Remove a specified character or string from the end of this value.

        Parameters
        ----------
        string : Optional[Union[str, "String"]], optional
            A character or string to remove from the end of this value.
            If this argument is `None` (default), this method removes
            spaces and line breaks.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.

        Returns
        -------
        result : String
            A stripped result string.
        """
        import apysc as ap
        from apysc._type.variable_name_mixin import VariableNameMixIn

        result: ap.String = ap.String("", variable_name_suffix=variable_name_suffix)
        self_variable_name: str = ""
        if isinstance(self, VariableNameMixIn):
            self_variable_name = self.variable_name
        if string is None:
            expression: str = _create_string_none_case_expression(
                result_string=result,
                self_variable_name=self_variable_name,
            )
        pass


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
    expression: str = (
        f"{result_string.variable_name} = {self_variable_name}.trimEnd();"
    )
    return expression
