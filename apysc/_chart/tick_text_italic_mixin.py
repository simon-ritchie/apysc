"""The mix-in class implementation for the `tick_text_italic` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class TickTextItalicMixIn:
    _tick_text_italic: Boolean

    @final
    @arg_validation_decos.is_boolean(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_text_italic(
        self,
        *,
        tick_text_italic: Union[bool, Boolean],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial boolean value, whether a tick text is
        an italic style or not (normal).

        Parameters
        ----------
        tick_text_italic : Union[bool, Boolean]
            A boolean, whether a tick text is an italic style or not (normal).
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(tick_text_italic, Boolean):
            tick_text_italic_: Boolean = Boolean(
                tick_text_italic,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            tick_text_italic_ = tick_text_italic
        self._tick_text_italic = tick_text_italic_
