"""The mix-in class implementation for the `left_margin` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class LeftMarginMixIn:

    _left_margin: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_left_margin(
        self,
        *,
        left_margin: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial left margin.

        Parameters
        ----------
        left_margin : Union[int, Int]
            A left margin.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(left_margin, Int):
            left_margin_: Int = Int(
                left_margin,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            left_margin_ = left_margin
        self._left_margin = left_margin_
