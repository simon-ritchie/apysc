"""Mix-in class implementation for the `_set_initial_y` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class SetInitialYMixIn:
    _y: Number

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_y(
        self,
        *,
        y: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial y value.

        Parameters
        ----------
        y : Union[float, Number]
            A chart's initial y-coordinate value.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(y, Number):
            y_: Number = Number(y, variable_name_suffix=variable_name_suffix)
        else:
            y_ = y
        self._y = y_
