"""The mix-in class implementation for the `SvgText`'s
`_skip_fill_alpha_expression_appending` attribute.
"""

from typing import Optional
from typing import Union

from typing_extensions import final

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number


class SvgTextSkipFillAlphaExpAppendingMixIn:
    _skip_fill_alpha_expression_appending: bool = False

    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_fill_alpha_expression_skipping_attr(
        self,
        *,
        fill_alpha: Optional[Union[float, Number]],
    ) -> None:
        """
        Set a boolean attribute, whether to skip a fill-alpha expression's appending
        or not.

        Parameters
        ----------
        fill_alpha : Optional[Union[float, Number]]
            A fill-alpha setting.
        """
        if fill_alpha is None:
            self._skip_fill_alpha_expression_appending = True
            return
        self._skip_fill_alpha_expression_appending = False
