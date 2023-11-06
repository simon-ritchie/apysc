"""The mix-in class implementation for the `SvgText`'s `_set_align` method.
"""


from typing_extensions import final

from apysc._display.svg_text_align_mixin import SVGTextAlign
from apysc._html.debug_mode import add_debug_info_setting


class SVGTextSetAlignMixIn:
    @final
    @add_debug_info_setting(module_name=__name__)
    def _set_align(self, *, align: SVGTextAlign) -> None:
        """
        Set a text-align setting.

        Parameters
        ----------
        align : SVGTextAlign
            A text-align setting.
        """
        from apysc._display.svg_text_align_mixin import SvgTextAlignMixIn

        if not isinstance(self, SvgTextAlignMixIn):
            raise TypeError(
                f"This method is only supported an {SvgTextAlignMixIn.__name__} "
                f"instance: {type(self).__name__}"
            )

        self.align = align
