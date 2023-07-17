"""The mix-in class implementation for the `tick_text_max_num_of_decimal_places`
value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class TickTextMaxNumOfDecimalPlacesMixIn:
    _tick_text_max_num_of_decimal_places: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_tick_text_max_num_of_decimal_places(
        self,
        *,
        tick_text_max_num_of_decimal_places: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial tick text maximum number of decimal places.

        Parameters
        ----------
        tick_text_max_num_of_decimal_places : Union[int, Int]
            A tick text maximum number of decimal places.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(tick_text_max_num_of_decimal_places, Int):
            tick_text_max_num_of_decimal_places_: Int = Int(
                tick_text_max_num_of_decimal_places,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            tick_text_max_num_of_decimal_places_ = tick_text_max_num_of_decimal_places
        self._tick_text_max_num_of_decimal_places = tick_text_max_num_of_decimal_places_
