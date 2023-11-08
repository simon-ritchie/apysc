"""The mix-in class implementation for the `SvgText`'s
`_skip_line_thickness_expression_appending` attribute.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int


class SvgTextSkipLineThicknessExpAppendingMixIn:
    _skip_line_thickness_expression_appending: bool = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_line_thickness_expression_skipping_attr(
        self,
        *,
        line_thickness: Optional[Union[int, Int]],
    ) -> None:
        """
        Set a boolean attribute, whether to skip a line-thickness expression's
        appending or not.

        Parameters
        ----------
        line_thickness : Optional[Union[int, Int]]
            A line-thickness setting.
        """
        if line_thickness is None:
            self._skip_line_thickness_expression_appending = True
            return
        self._skip_line_thickness_expression_appending = False
