"""The mix-in class implementation for the CSS text-align property.
"""

from apysc._display.css_text_align import CssTextAlign
from apysc._validation import arg_validation_decos


class TextAlignCssMixIn:
    _css_text_align: CssTextAlign = CssTextAlign.LEFT

    @property
    def text_align(self) -> CssTextAlign:
        """
        Get a text-align value.

        Returns
        -------
        text_align : CssTextAlign
            A text-align value.
        """
        return self._css_text_align

    @text_align.setter
    @arg_validation_decos.is_css_text_align(arg_position_index=1)
    def text_align(self, value: CssTextAlign) -> None:
        """
        Set a text-align value.

        Parameters
        ----------
        value : CssTextAlign
            A text-align value.
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._css_text_align = value
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        interface.set_css(name="text-align", value=value.value)
