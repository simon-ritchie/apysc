"""Mix-in class implementation for the `_set_initial_border_thickness`
method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class SetInitialBorderThicknessMixIn:
    _border_thickness: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_border_thickness(
        self,
        *,
        border_thickness: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial border thickness.

        Parameters
        ----------
        border_thickness : Union[int, Int]
            A chart's border thickness.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(border_thickness, Int):
            border_thickness_: Int = Int(
                border_thickness, variable_name_suffix=variable_name_suffix
            )
        else:
            border_thickness_ = border_thickness
        self._border_thickness = border_thickness_
