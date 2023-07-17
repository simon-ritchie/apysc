"""The mix-in class implementation for the `is_display_axis_label` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class IsDisplayAxisLabelMixIn:
    _is_display_axis_label: Boolean

    @final
    @arg_validation_decos.is_boolean(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_is_display_axis_label(
        self,
        *,
        is_display_axis_label: Union[bool, Boolean],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial boolean, whether an axis label is visible or not.

        Parameters
        ----------
        is_display_axis_label : Union[bool, Boolean]
            A boolean, whether an axis label is visible or not.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(is_display_axis_label, Boolean):
            is_display_axis_label_: Boolean = Boolean(
                is_display_axis_label,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            is_display_axis_label_ = is_display_axis_label
        self._is_display_axis_label = is_display_axis_label_
