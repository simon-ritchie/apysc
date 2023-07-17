"""The mix-in class implementation for the `axis_label_italic` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class AxisLabelItalicMixIn:
    _axis_label_italic: Boolean

    @final
    @arg_validation_decos.is_boolean(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_italic(
        self,
        *,
        axis_label_italic: Union[bool, Boolean],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial boolean, whether an axis label is
        an italic style or not (normal).

        Parameters
        ----------
        axis_label_italic : Union[bool, Boolean]
            A boolean, whether an axis label is an italic style or not (normal).
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(axis_label_italic, Boolean):
            axis_label_italic_: Boolean = Boolean(
                axis_label_italic, variable_name_suffix=variable_name_suffix
            )
        else:
            axis_label_italic_ = axis_label_italic
        self._axis_label_italic = axis_label_italic_
