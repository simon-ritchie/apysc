"""Mix-in Class implementation for the `_set_initial_width` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class SetInitialWidthMixIn:
    _width: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_width(
        self,
        *,
        width: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial width.

        Parameters
        ----------
        width : Union[int, Int]
            A chart's initial width.
        variable_name_suffix : str, default ""
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(width, Int):
            width_: Int = Int(width, variable_name_suffix=variable_name_suffix)
        else:
            width_ = width
        self._width = width_
