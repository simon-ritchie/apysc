"""Class implementation for the path labels enum.
"""

from enum import Enum


class PathLabel(Enum):
    """
    Enum class for the path labels
    """
    MoveTo = 'M'
    LineTo = 'L'
    Horizontal = 'H'
    Vertical = 'V'
    Close = 'Z'
    Bezier2D = 'Q'
    Bezier2DContinual = 'T'
    Bezier3D = 'C'
    Bezier3DContinual = 'S'
