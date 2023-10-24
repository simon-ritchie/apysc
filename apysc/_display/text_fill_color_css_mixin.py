"""The mix-in class implementation for the CSS color setting.
"""

from apysc._color.color import Color


class TextFillColorCSSMixIn:
    _fill_color: Color

    def _initialize_fill_color(self) -> None:
        """
        Initialize a `_fill_color` attribute.
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
        return self._fill_color

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

        if not isinstance(self, CssInterface):
            raise TypeError(
                "This method can only be called on an instance of CssInterface class."
            )
        self._fill_color = value
        self.set_css(
            name="color",
            value=self._fill_color._value,
        )
