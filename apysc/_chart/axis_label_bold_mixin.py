"""The mix-in class implementation for the `axis_label_bold` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class AxisLabelBoldMixIn:
    _axis_label_bold: Boolean

    @final
    @arg_validation_decos.is_boolean(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_bold(
        self,
        *,
        axis_label_bold: Union[bool, Boolean],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial boolean, whether an axis label is a bold style or not.

        Parameters
        ----------
        axis_label_bold : Union[bool, Boolean]
            A boolean, whether an axis label is a bold style or not.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(axis_label_bold, Boolean):
            axis_label_bold_: Boolean = Boolean(
                axis_label_bold,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            axis_label_bold_ = axis_label_bold
        self._axis_label_bold = axis_label_bold_
