"""The color class implementation.
"""

from typing import Union, TypeVar
from typing_extensions import final

from apysc._type.copy_mixin import CopyMixIn
from apysc._type.revert_mixin import RevertMixIn
from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._type.string import String
from apysc._validation import arg_validation_decos
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.initial_substitution_exp_mixin import InitialSubstitutionExpMixIn

_StrOrString = TypeVar("_StrOrString", str, String)


class Color(
    CopyMixIn,
    RevertMixIn,
    CustomEventMixIn,
    InitialSubstitutionExpMixIn,
):
    _value: String

    @arg_validation_decos.is_hex_color_code_format(arg_position_index=1, optional=False)
    def __init__(
        self,
        value: _StrOrString,
        *,
        variable_name_suffix: str = "",
        skip_init_substitution_expression_appending: bool = False,
    ) -> None:
        """
        The color class implementation.

        Parameters
        ----------
        value : str or String
            A hexadecimal color code string (e.g., '#000000').
        variable_name_suffix : str, default ''
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        skip_init_substitution_expression_appending : bool, default False
            A boolean indicates whether to skip an initial substitution
            expression or not. This class uses this option internally.
        """
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope
        from apysc._color import color_util

        with TemporaryNotHandlerScope():
            value = color_util.complement_hex_color(hex_color_code=value)
            self._value = String(
                value=value,
                variable_name_suffix=variable_name_suffix,
            )

        self._append_initial_substitution_expression_if_in_handler_scope(
            skip_appending=skip_init_substitution_expression_appending,
        )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_constructor_expression(self) -> None:
        pass

    @final
    def _create_initial_substitution_expression(self) -> str:
        """
        Create an initial value's substitution expression string.

        Returns
        -------
        expression : str
            Created expression string.
        """
        return ""
