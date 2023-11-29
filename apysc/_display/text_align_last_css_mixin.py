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

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=350,
        ...     stage_height=170,
        ...     stage_elem_id="stage",
        ... )
        >>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        ...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        ...     "Ut enim ad minim veniam",
        ...     width=300,
        ...     font_size=16,
        ...     fill_color=ap.Color("#00aaff"),
        ...     x=25,
        ...     y=25,
        ... )
        >>> multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
        >>> multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT
        >>> assert multi_line_text.text_align_last == ap.CssTextAlignLast.RIGHT
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

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=350,
        ...     stage_height=170,
        ...     stage_elem_id="stage",
        ... )
        >>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        ...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        ...     "Ut enim ad minim veniam",
        ...     width=300,
        ...     font_size=16,
        ...     fill_color=ap.Color("#00aaff"),
        ...     x=25,
        ...     y=25,
        ... )
        >>> multi_line_text.text_align = ap.CssTextAlign.JUSTIFY
        >>> multi_line_text.text_align_last = ap.CssTextAlignLast.RIGHT
        >>> assert multi_line_text.text_align_last == ap.CssTextAlignLast.RIGHT
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._css_text_align_last = value
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        interface.set_css(name="text-align-last", value=value.value)
