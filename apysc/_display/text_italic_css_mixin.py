"""The mix-in class implementation for the CSS italic (font-style) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean


class TextItalicCssMixIn(
    AttrLinkingMixIn,
):
    _italic: Boolean

    def _initialize_italic(self) -> None:
        """
        Initialize the `_italic` attribute.
        """
        if hasattr(self, '_italic'):
            return
        self._italic = Boolean(False)

    @property
    def italic(self) -> Boolean:
        """
        Get a italic (font-style) value.

        Returns
        -------
        italic : Boolean
            A italic (font-style) value.
        """
        self._initialize_italic()
        return self._italic._copy()
