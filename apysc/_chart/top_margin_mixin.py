"""The mix-in class implementation for the `top_margin` value.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class TopMarginMixIn:

    _top_margin: Int

    @final
    @arg_validation_decos.is_integer(arg_position_index=1, optional=False)
    @arg_validation_decos.is_builtin_string(arg_position_index=2, optional=False)
    @add_debug_info_setting(module_name=__name__)
    def _set_initial_top_margin(
        self,
        top_margin: Union[int, Int],
        variable_name_suffix: str = "",
    ) -> None:
        """
        Set an initial top margin.

        Parameters
        ----------
        top_margin : Union[int, Int]
            A top margin.
        variable_name_suffix : str, optional
            A JavaScript variable name suffix string.
            This setting is sometimes useful for JavaScript debugging.
        """
        if not isinstance(top_margin, Int):
            top_margin_: Int = Int(
                top_margin,
                variable_name_suffix=variable_name_suffix,
            )
        else:
            top_margin_ = top_margin
        self._top_margin = top_margin_
