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
