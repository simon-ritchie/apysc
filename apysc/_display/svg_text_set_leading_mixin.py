"""The mix-in class implementation for the `SvgText`'s `_set_leading` method.
"""

from typing import Union
from typing import cast

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class SvgTextSetLeadingMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_leading(self, *, leading: Union[float, Number]) -> None:
        """
        Set a leading value.

        Parameters
        ----------
        leading : Union[float, Number]
            A text-leading value.
        """
        from apysc._display.svg_text_leading_mixin import SvgTextLeadingMixIn
        from apysc._type.variable_name_suffix_utils import (
            get_attr_or_variable_name_suffix,
        )

        if not isinstance(self, SvgTextLeadingMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextLeadingMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        if isinstance(leading, float):
            suffix: str = get_attr_or_variable_name_suffix(
                instance=self, value_identifier="leading"
            )
            leading_: Number = Number(leading, variable_name_suffix=suffix)
        else:
            leading_ = cast(Number, leading)
        self.leading = leading_
