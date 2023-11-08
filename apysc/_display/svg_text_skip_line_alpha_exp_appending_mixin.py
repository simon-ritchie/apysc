"""The mix-in class implementation for the `SvgText`'s
`_skip_line_alpha_expression_appending` attribute.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class SvgTextSkipLineAlphaExpAppendingMixIn:
    _skip_line_alpha_expression_appending: bool = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_line_alpha_expression_skipping_attr(
        self,
        *,
        line_alpha: Optional[Union[float, Number]],
    ) -> None:
        """
        Set a boolean attribute, whether to skip a line-alpha expression's appending
        or not.

        Parameters
        ----------
        line_alpha : Optional[Union[float, Number]]
            A line-alpha setting.
        """
        if line_alpha is None:
            self._skip_line_alpha_expression_appending = True
            return
        self._skip_line_alpha_expression_appending = False
