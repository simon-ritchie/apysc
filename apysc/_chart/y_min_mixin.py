"""The mix-in class implementation for the `y_min` value.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class YMinMixIn:
    _y_min: Optional[Number]

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=True)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_y_min(
        self,
        *,
        y_min: Optional[Union[float, Number]],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial minimum y-axis value.

        Parameters
        ----------
        y_min : Optional[Union[float, Number]]
            A minimum y-axis value.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if y_min is None:
            self._y_min = None
            return
        if not isinstance(y_min, Number):
            y_min_: Number = Number(y_min, variable_name_suffix=variable_name_suffix)
        else:
            y_min_ = y_min
        self._y_min = y_min_
