"""Class implementation for the path labels enum.
"""

from enum import Enum


class PathLabel(Enum):
    """
    Enum class for the path labels
    """

    MOVE_TO = "M"
    LINE_TO = "L"
    HORIZONTAL = "H"
    VERTICAL = "V"
    CLOSE = "Z"
    BEZIER_2D = "Q"
    BEZIER_2D_CONTINUAL = "T"
    BEZIER_3D = "C"
    BEZIER_3D_CONTINUAL = "S"
