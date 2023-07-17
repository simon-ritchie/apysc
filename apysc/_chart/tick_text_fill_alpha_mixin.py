"""The mix-in class implementation for the `tick_text_fill_alpha` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class TickTextFillAlphaMixIn:
    _tick_text_fill_alpha: Number

    @final
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_text_fill_alpha(
        self,
        *,
        tick_text_fill_alpha: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial tick text fill alpha setting.

        Parameters
        ----------
        tick_text_fill_alpha : Union[float, Number]
            A tick text fill-alpha setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(tick_text_fill_alpha, Number):
            tick_text_fill_alpha_: Number = Number(
                tick_text_fill_alpha,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            tick_text_fill_alpha_ = tick_text_fill_alpha
        self._tick_text_fill_alpha = tick_text_fill_alpha_
