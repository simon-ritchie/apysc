"""Line caps enum definitions.
"""

from enum import Enum


class LineCaps(Enum):
    """
    Line caps style type definitions.

    Attributes
    ----------
    BUTT
        Default style type. No line cap will be set.
    ROUND
        This style type will change line cap to round.
    SQUARE
        This style type will change line cap to square.
        This is similar to BUTT type, but the length of the line
        will be increased by the stroke-width (thickness) value.
    """
    BUTT = 'butt'
    ROUND = 'round'
    SQUARE = 'square'
