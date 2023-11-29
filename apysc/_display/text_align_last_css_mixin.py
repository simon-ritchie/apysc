"""The mix-in class implementation for the CSS text-align-last property.
"""

from apysc._display.css_text_align_last import CssTextAlignLast
from apysc._validation import arg_validation_decos


class TextAlignLastCssMixIn:
    _css_text_align_last: CssTextAlignLast

    @property
    def text_align_last(self) -> CssTextAlignLast:
        """
        Get a text-align-last value.

        Returns
        -------
        text_align_last : CssTextAlignLast
            A text-align-last value.

        References
        ----------
        - text_align_last property
            - https://simon-ritchie.github.io/apysc/en/text_align_last.html
        """
        return self._css_text_align_last

    @text_align_last.setter
    @arg_validation_decos.is_css_text_align_last(arg_position_index=1)
    def text_align_last(self, value: CssTextAlignLast) -> None:
        """
        Set a text-align-last value.

        Parameters
        ----------
        value : CssTextAlignLast
            A text-align-last value.

        References
        ----------
        - text_align_last property
            - https://simon-ritchie.github.io/apysc/en/text_align_last.html
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._css_text_align_last = value
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        interface.set_css(name="text-align-last", value=value.value)
