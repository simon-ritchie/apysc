"""The mix-in class implementation for the `SvgText`'s `_set_delta_y` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class SvgTextSetDeltaYMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_delta_y(self, *, delta_y: Union[float, Number]) -> None:
        """
        Set a coordinate delta-y value.

        Parameters
        ----------
        delta_y : Union[float, Number]
            A delta-y value.
        """
        from apysc._display.svg_text_delta_y_mixin import SvgTextDeltaYMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if not isinstance(self, SvgTextDeltaYMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextDeltaYMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if not isinstance(delta_y, Number):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="delta_y"
            )
            delta_y_: Number = Number(delta_y, variable_name_suffix=suffix)
        else:
            delta_y_ = delta_y
        self.delta_y = delta_y_
