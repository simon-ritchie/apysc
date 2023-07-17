"""The mix-in class implementation for the `tick_text_bold` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class TickTextBoldMixIn:
    _tick_text_bold: Boolean

    @final
    @arg_validation_decos.is_boolean(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_text_bold(
        self,
        *,
        tick_text_bold: Union[bool, Boolean],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial boolean value, whether a tick text is a bold style or not.

        Parameters
        ----------
        tick_text_bold : Union[bool, Boolean]
            A boolean, whether a tick text is a bold style or not.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(tick_text_bold, Boolean):
            tick_text_bold_: Boolean = Boolean(
                tick_text_bold,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            tick_text_bold_ = tick_text_bold
        self._tick_text_bold = tick_text_bold_
