"""The mix-in class implementation for the `_set_initial_horizontal_padding` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class SetInitialHorizontalPaddingMixIn:
    _horizontal_padding: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_horizontal_padding(
        self,
        *,
        horizontal_padding: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set a chart's initial horizontal padding.

        Parameters
        ----------
        horizontal_padding : Union[int, Int]
            A chart's horizontal padding between borders and contents.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(horizontal_padding, Int):
            horizontal_padding_: Int = Int(
                horizontal_padding, variable_name_suffix=variable_name_suffix
            )
        else:
            horizontal_padding_ = horizontal_padding
        self._horizontal_padding = horizontal_padding_
