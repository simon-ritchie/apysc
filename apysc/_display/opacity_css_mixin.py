"""The mix-in class implementation for the CSS fill-alpha (`opacity`) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.number import Number


class OpacityCssMixIn(AttrLinkingMixIn):
    _fill_alpha: Number

    def _initialize_fill_alpha(self) -> None:
        """
        Initialize the `_fill_alpha` attribute.
        """
        if hasattr(self, "_fill_alpha"):
            return
        self._fill_alpha = Number(1.0)

    @property
    def fill_alpha(self) -> Number:
        """
        Get a fill-alpha (opacity) value.

        Returns
        -------
        alpha : Number
            A fill-alpha (opacity) value.

        References
        ----------
        - Text fill_alpha property
            - https://simon-ritchie.github.io/apysc/en/text_fill_alpha.html

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
        >>> multi_line_text.fill_alpha = ap.Number(0.5)
        >>> multi_line_text.fill_alpha
        Number(0.5)
        """
        self._initialize_fill_alpha()
        return self._fill_alpha._copy()

    @fill_alpha.setter
    def fill_alpha(self, value: Number) -> None:
        """
        Set a fill-alpha (opacity) value.

        Parameters
        ----------
        value : Number
            A fill-alpha (opacity) value.

        References
        ----------
        - Text fill_alpha property
            - https://simon-ritchie.github.io/apysc/en/text_fill_alpha.html

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
        >>> multi_line_text.fill_alpha = ap.Number(0.5)
        >>> multi_line_text.fill_alpha
        Number(0.5)
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        self._initialize_fill_alpha()
        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._fill_alpha = value
        interface.set_css(
            name="opacity",
            value=self._fill_alpha.to_string(),
        )

        self._append_applying_new_attr_val_exp(
            new_attr=self._fill_alpha, attr_name="fill_alpha"
        )
        self._append_attr_to_linking_stack(
            attr=self._fill_alpha, attr_name="fill_alpha"
        )
