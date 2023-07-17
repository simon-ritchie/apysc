"""Mix-in class implementation for the `_set_initial_height` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class SetInitialHeightMixIn:
    _height: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_height(
        self,
        *,
        height: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial height.

        Parameters
        ----------
        height : Union[int, Int]
            A chart's initial height.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(height, Int):
            height_: Int = Int(height, variable_name_suffix=variable_name_suffix)
        else:
            height_ = height
        self._height = height_
