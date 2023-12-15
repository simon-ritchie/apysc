"""The mix-in implementation for the text's CSS underline setting.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean
from apysc._validation import arg_validation_decos


class TextDecorationUnderlineCssMixIn(
    AttrLinkingMixIn,
):
    _underline: Boolean

    def _initialize_underline(self) -> None:
        """
        Initialize the `_underline` attribute.
        """
        if hasattr(self, "_underline"):
            return
        self._underline = Boolean(False)

    @property
    def underline(self) -> Boolean:
        """
        Get a text underline (`text-decoration: underline`) setting.

        Returns
        -------
        underline : Boolean
            A text underline setting.

        References
        ----------
        - Text underline property
            - https://simon-ritchie.github.io/apysc/en/text_underline.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=300,
        ...     stage_height=195,
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
        >>> multi_line_text.underline = ap.True_
        >>> multi_line_text.underline
        Boolean(True)
        """
        self._initialize_underline()
        return self._underline._copy()

    @underline.setter
    @arg_validation_decos.is_apysc_boolean(arg_position_index=1)
    def underline(self, value: Boolean) -> None:
        """
        Set a text underline (`text-decoration: underline`) setting.

        Parameters
        ----------
        value : Boolean
            A text underline setting.

        References
        ----------
        - Text underline property
            - https://simon-ritchie.github.io/apysc/en/text_underline.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=300,
        ...     stage_height=195,
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
        >>> multi_line_text.underline = ap.True_
        >>> multi_line_text.underline
        Boolean(True)
        """
        from apysc._branch._else import Else
        from apysc._branch._if import If
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._underline = value

        with If(self._underline):
            interface.set_css(name="text-decoration", value="underline")
        with Else():
            interface.set_css(name="text-decoration", value="none")

        self._append_applying_new_attr_val_exp(
            new_attr=self._underline, attr_name="underline"
        )
        self._append_attr_to_linking_stack(attr=self._underline, attr_name="underline")
