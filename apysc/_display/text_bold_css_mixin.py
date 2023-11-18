"""The mix-in class implementation for the CSS bold (font-weight) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class TextBoldCssMixIn(
    AttrLinkingMixIn,
):
    _bold: Boolean

    def _initialize_bold(self) -> None:
        """
        Initialize the `_bold` attribute.
        """
        if hasattr(self, "_bold"):
            return
        self._bold = Boolean(False)

    @property
    def bold(self) -> Boolean:
        """
        Get a bold (font-weight) value.

        Returns
        -------
        bold : Boolean
            A bold (font-weight) value.

        References
        ----------
        - Text bold property
            - https://simon-ritchie.github.io/apysc/en/text_bold.html

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
        >>> multi_line_text.bold = ap.True_
        >>> multi_line_text.bold
        Boolean(True)
        """
        self._initialize_bold()
        return self._bold._copy()

    @bold.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    def bold(self, value: Boolean) -> None:
        """
        Set a bold (font-weight) value.

        Parameters
        ----------
        value : Boolean
            A bold (font-weight) value.

        References
        ----------
        - Text bold property
            - https://simon-ritchie.github.io/apysc/en/text_bold.html

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
        >>> multi_line_text.bold = ap.True_
        >>> multi_line_text.bold
        Boolean(True)
        """
        from apysc._branch._else import Else
        from apysc._branch._if import If
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._bold = value

        with If(self._bold):
            interface.set_css(
                name="font-weight",
                value="bold",
            )
        with Else():
            interface.set_css(
                name="font-weight",
                value="normal",
            )

        self._append_applying_new_attr_val_exp(new_attr=self._bold, attr_name="bold")
        self._append_attr_to_linking_stack(attr=self._bold, attr_name="bold")
