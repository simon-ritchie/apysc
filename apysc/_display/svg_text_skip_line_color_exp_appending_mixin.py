"""The mix-in class implementation for the `SVGText`'s
`_skip_line_color_expression_appending` attribute.
"""

from typing import Union, Optional

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String


class SVGTextSkipLineColorExpAppendingMixIn:

    _skip_line_color_expression_appending: bool = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_line_color_expression_skipping_attr(
        self,
        *,
        line_color: Optional[Union[str, String]],
    ) -> None:
        """
        Set a boolean attribute, whether to skip a line-color expression's appending
        or not.

        Parameters
        ----------
        line_color : Optional[Union[str, String]]
            A line-color setting.
        """
        if line_color is None:
            self._skip_line_color_expression_appending = True
            return
        self._skip_line_color_expression_appending = False
