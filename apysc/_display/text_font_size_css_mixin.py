"""The mix-in class implementation for the font-size setting.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.int import Int
from apysc._validation import arg_validation_decos


class TextFontSizeCssMixIn(
    AttrLinkingMixIn,
):
    _font_size: Int

    def _initialize_font_size(self) -> None:
        """
        Initialize the `_font_size` attribute.
        """
        if hasattr(self, "_font_size"):
            return
        self._font_size = Int(16)

    @property
    def font_size(self) -> Int:
        """
        Get a text's font size.

        Returns
        -------
        font_size : Int
            A text font size.

        References
        ----------
        - Text font_size property
            - https://simon-ritchie.github.io/apysc/en/text_font_size.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=350,
        ...     stage_height=250,
        ...     stage_elem_id="stage",
        ... )
        >>> text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Example of font-size = 32. Lorem ipsum dolor sit amet, "
        ...     "consectetur adipiscing elit, sed do eiusmod tempor incididunt.",
        ...     width=300,
        ...     fill_color=ap.Color("#00aaff"),
        ...     x=25,
        ...     y=25,
        ... )
        >>> text.font_size = ap.Int(32)
        >>> text.font_size
        Int(32)
        """
        self._initialize_font_size()
        return self._font_size._copy()

    @font_size.setter
    @arg_validation_decos.is_apysc_integer(arg_position_index=1)
    def font_size(self, value: Int) -> None:
        """
        Set a text's font size.

        Parameters
        ----------
        value : Int
            A text font size.

        References
        ----------
        - Text font_size property
            - https://simon-ritchie.github.io/apysc/en/text_font_size.html

        Examples
        --------
        >>> import apysc as ap

        >>> stage: ap.Stage = ap.Stage(
        ...     background_color=ap.Color("#333"),
        ...     stage_width=350,
        ...     stage_height=250,
        ...     stage_elem_id="stage",
        ... )
        >>> text: ap.MultiLineText = ap.MultiLineText(
        ...     text="Example of font-size = 32. Lorem ipsum dolor sit amet, "
        ...     "consectetur adipiscing elit, sed do eiusmod tempor incididunt.",
        ...     width=300,
        ...     fill_color=ap.Color("#00aaff"),
        ...     x=25,
        ...     y=25,
        ... )
        >>> text.font_size = ap.Int(32)
        >>> text.font_size
        Int(32)
        """
        from apysc._display.css_interface import CssInterface
        from apysc._validation import display_validation

        interface: CssInterface = display_validation.validate_css_interface(
            instance=self
        )
        self._font_size = value
        interface.set_css(
            name="font-size",
            value=self._font_size.to_string() + "px",
        )

        self._append_applying_new_attr_val_exp(
            new_attr=self._font_size, attr_name="font_size"
        )
        self._append_attr_to_linking_stack(attr=self._font_size, attr_name="font_size")
