"""The enum definitions for the text-align CSS property.
"""

from enum import Enum


class CssTextAlign(Enum):
    """
    The enum definitions for the text-align CSS property.

    References
    ----------
    - text_align property
        - https://simon-ritchie.github.io/apysc/en/text_align.html
    """

    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFY = "justify"
