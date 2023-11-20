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

        References
        ----------
        - text_align property
            - https://simon-ritchie.github.io/apysc/en/text_align.html

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
        >>> multi_line_text.text_align = ap.CssTextAlign.RIGHT
        >>> assert multi_line_text.text_align == ap.CssTextAlign.RIGHT
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

        References
        ----------
        - text_align property
            - https://simon-ritchie.github.io/apysc/en/text_align.html

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
        >>> multi_line_text.text_align = ap.CssTextAlign.RIGHT
        >>> assert multi_line_text.text_align == ap.CssTextAlign.RIGHT
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._css_text_align = value
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        interface.set_css(name="text-align", value=value.value)
