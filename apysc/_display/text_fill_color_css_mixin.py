"""The mix-in class implementation for the CSS color setting.
"""

from apysc._color.color import Color
from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._validation import arg_validation_decos


class TextFillColorCssMixIn(
    AttrLinkingMixIn,
):
    _fill_color: Color

    def _initialize_fill_color(self) -> None:
        """
        Initialize the `_fill_color` attribute.
        """
        if hasattr(self, "_fill_color"):
            return
        self._fill_color = Color("")

    @property
    def fill_color(self) -> Color:
        """
        Get a text's fill color.

        Returns
        -------
        color : Color
            A text color.

        References
        ----------
        - MultiLineText class
            - https://simon-ritchie.github.io/apysc/en/multi_line_text.html
        - Text fill_color property
            - https://simon-ritchie.github.io/apysc/en/text_fill_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=300,
        ...     stage_height=100,
        ...     stage_elem_id="stage",
        ... )
        >>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        ...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        ...     "Ut enim ad minim veniam",
        ...     width=300,
        ...     font_size=16,
        ...     x=20,
        ...     y=20,
        ... )
        >>> multi_line_text.fill_color = ap.Colors.CYAN_00AAFF
        >>> assert multi_line_text.fill_color == ap.Colors.CYAN_00AAFF
        """
        self._initialize_fill_color()
        return self._fill_color._copy()

    @fill_color.setter
    @arg_validation_decos.is_color(arg_position_index=1, optional=False)
    def fill_color(self, value: Color) -> None:
        """
        Set a text's fill color.

        Parameters
        ----------
        value : Color
            A text color.

        References
        ----------
        - MultiLineText class
            - https://simon-ritchie.github.io/apysc/en/multi_line_text.html
        - Text fill_color property
            - https://simon-ritchie.github.io/apysc/en/text_fill_color.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=300,
        ...     stage_height=100,
        ...     stage_elem_id="stage",
        ... )
        >>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        ...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        ...     "Ut enim ad minim veniam",
        ...     width=300,
        ...     font_size=16,
        ...     x=20,
        ...     y=20,
        ... )
        >>> multi_line_text.fill_color = ap.Colors.CYAN_00AAFF
        >>> assert multi_line_text.fill_color == ap.Colors.CYAN_00AAFF
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._fill_color = value
        interface.set_css(
            name="color",
            value=self._fill_color._value,
        )

        self._append_applying_new_attr_val_exp(
            new_attr=self._fill_color, attr_name="fill_color"
        )
        self._append_attr_to_linking_stack(
            attr=self._fill_color, attr_name="fill_color"
        )
