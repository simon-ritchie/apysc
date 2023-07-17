"""Mix-in class implementation for the `_set_initial_x` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class SetInitialXMixIn:
    _x: Number

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_x(
        self,
        *,
        x: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial x value.

        Parameters
        ----------
        x : Union[float, Number]
            A chart's initial x-coordinate value.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(x, Number):
            x_: Number = Number(x, variable_name_suffix=variable_name_suffix)
        else:
            x_ = x
        self._x = x_
