"""The mix-in class implementation for the CSS line-height property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number
from apysc._validation import arg_validation_decos


class TextLineHeightCssMixIn(
    AttrLinkingMixIn,
):
    _line_height: Number

    def _initialize_line_height(self) -> None:
        """
        Initialize the `_line_height` attribute.
        """
        if hasattr(self, "_line_height"):
            return
        self._line_height = Number(1.5)

    @property
    def line_height(self) -> Number:
        """
        Get a line-height value.

        Returns
        -------
        line_height : Number
            A line-height value.

        References
        ----------
        - Text line_height property
            - https://simon-ritchie.github.io/apysc/en/text_line_height.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=300,
        ...     stage_height=250,
        ...     stage_elem_id="stage",
        ... )

        >>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        ...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        ...     "Ut enim ad minim veniam",
        ...     width=250,
        ...     fill_color=ap.Colors.GRAY_AAAAAA,
        ...     x=25,
        ...     y=25,
        ... )
        >>> multi_line_text.line_height = ap.Number(2.0)
        >>> multi_line_text.line_height
        Number(2.0)
        """
        self._initialize_line_height()
        return self._line_height

    @line_height.setter
    @arg_validation_decos.is_apysc_num(arg_position_index=1)
    def line_height(self, value: Number) -> None:
        """
        Update a line-height value.

        Parameters
        ----------
        value : Number
            A line-height value.

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=300,
        ...     stage_height=250,
        ...     stage_elem_id="stage",
        ... )

        >>> multi_line_text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        ...     "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        ...     "Ut enim ad minim veniam",
        ...     width=250,
        ...     fill_color=ap.Colors.GRAY_AAAAAA,
        ...     x=25,
        ...     y=25,
        ... )
        >>> multi_line_text.line_height = ap.Number(2.0)
        >>> multi_line_text.line_height
        Number(2.0)
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._initialize_line_height()
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._line_height = value
        interface.set_css(
            name="line-height",
            value=self._line_height.to_string(),
        )

        self._append_applying_new_attr_val_exp(
            new_attr=self._line_height, attr_name="line_height"
        )
        self._append_attr_to_linking_stack(
            attr=self._line_height, attr_name="line_height"
        )
