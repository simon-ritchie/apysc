"""Mix-in class implementation for the `_set_initial_border_alpha` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class SetInitialBorderAlphaMixIn:

    _border_alpha: Number

    @final
    @arg_validation_decos.is_num(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_0_to_1_range(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_border_alpha(
        self,
        *,
        border_alpha: Union[float, Number],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial border alpha.

        Parameters
        ----------
        border_alpha : Union[float, Number]
            A chart's border alpha.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(border_alpha, Number):
            border_alpha_: Number = Number(
                border_alpha, variable_name_suffix=variable_name_suffix
            )
        else:
            border_alpha_ = border_alpha
        self._border_alpha = border_alpha_
