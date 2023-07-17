"""The mix-in class implementation for the `y_max` value.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class YMaxMixIn:
    _y_max: Optional[Number]

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_y_max(
        self,
        *,
        y_max: Optional[Union[float, Number]],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial maximum y-axis value.

        Parameters
        ----------
        y_max : Optional[Union[float, Number]]
            A maximum y-axis value.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if y_max is None:
            self._y_max = None
            return
        if not isinstance(y_max, Number):
            y_max_: Number = Number(y_max, variable_name_suffix=variable_name_suffix)
        else:
            y_max_ = y_max
        self._y_max = y_max_
