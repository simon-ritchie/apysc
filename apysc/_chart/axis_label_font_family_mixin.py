"""The mix-in class implementation for the `axis_label_font_family` value.
"""

from typing import List
from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.array import Array
from apysc._type.string import String
from apysc._validation import arg_validation_decos


class AxisLabelFontFamilyMixIn:
    _axis_label_font_family: Optional[Array[String]]

    @final
    @arg_validation_decos.is_builtin_str_list_or_apysc_str_arr(
        arg_position_index=1, optional=True
    )
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_axis_label_font_family(
        self,
        *,
        axis_label_font_family: Optional[Union[Array[String], List[str]]],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial axis label font family setting.

        Parameters
        ----------
        axis_label_font_family : Optional[Union[Array[String], List[str]]]
            An axis label font family setting.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if axis_label_font_family is not None and not isinstance(
            axis_label_font_family, Array
        ):
            axis_label_font_family_: Optional[Array[String]] = Array(
                [String(font_name) for font_name in axis_label_font_family],  # type: ignore[union-attr] # noqa
                variable_name_suffix=variable_name_suffix,
            )
        else:
            axis_label_font_family_ = axis_label_font_family
        self._axis_label_font_family = axis_label_font_family_
