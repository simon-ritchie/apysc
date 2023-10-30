"""The mix-in class implementation for the CSS bold (font-weight) property.
"""

from apysc._type.attr_linking_mixin import AttrLinkingMixIn
from apysc._type.boolean import Boolean


class TextBoldCssMixIn(AttrLinkingMixIn):
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
        """
        self._initialize_bold()
        return self._bold._copy()

    @bold.setter
    def bold(self, value: Boolean) -> None:
        """
        Set a bold (font-weight) value.

        Parameters
        ----------
        value : Boolean
            A bold (font-weight) value.
        """
        pass
