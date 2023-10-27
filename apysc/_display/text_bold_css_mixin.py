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
