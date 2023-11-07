"""The mix-in class implementation for the `SvgText`'s `_set_delta_x` method.
"""

from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class SvgTextSetDeltaXMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_delta_x(self, *, delta_x: Union[float, Number]) -> None:
        """
        Set a coordinate delta-x value.

        Parameters
        ----------
        delta_x : Union[float, Number]
            A delta-x value.
        """
        from apysc._display.svg_text_delta_x_mixin import SvgTextDeltaXMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if not isinstance(self, SvgTextDeltaXMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextDeltaXMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if not isinstance(delta_x, Number):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="delta_x"
            )
            delta_x_: Number = Number(delta_x, variable_name_suffix=suffix)
        else:
            delta_x_ = delta_x
        self.delta_x = delta_x_
