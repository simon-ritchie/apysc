"""The mix-in class implementation for the CSS color setting.
"""

from apysc._color.color import Color


class TextColorCSSMixIn:
    _color: Color

    def _initialize_color(self) -> None:
        """
        Initialize text color attribute.
        """
        if hasattr(self, "_color"):
            return
        self._color = Color("")

    @property
    def color(self) -> Color:
        """
        Get a text color.

        Returns
        -------
        color : Color
            A text color.
        """
        self._initialize_color()
        return self._color

    @color.setter
    def color(self, value: Color) -> None:
        """
        Set a text color.

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
        self._color = value
        self.set_css(
            name="color",
            value=self._color._value,
        )
