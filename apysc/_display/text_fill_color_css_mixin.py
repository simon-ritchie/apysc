"""The mix-in class implementation for the CSS color setting.
"""

from apysc._color.color import Color
from apysc._type.attr_linking_mixin import AttrLinkingMixIn


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
        """
        self._initialize_fill_color()
        return self._fill_color._copy()

    @fill_color.setter
    def fill_color(self, value: Color) -> None:
        """
        Set a text's fill color.

        Parameters
        ----------
        value : Color
            A text color.
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
