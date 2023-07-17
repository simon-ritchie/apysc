"""The mix-in class implementation for the `SVGText`'s
`_skip_fill_color_expression_appending` attribute.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.string import String


class SVGTextSkipFillColorExpAppendingMixIn:
    _skip_fill_color_expression_appending: bool = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_fill_color_expression_skipping_attr(
        self,
        *,
        fill_color: Optional[Union[str, String]],
    ) -> None:
        """
        Set a boolean attribute, whether to skip a fill-color expression's appending
        or not.

        Parameters
        ----------
        fill_color : Optional[Union[str, String]]
            A fill-color setting.
        """
        if fill_color is None:
            self._skip_fill_color_expression_appending = True
            return
        self._skip_fill_color_expression_appending = False
