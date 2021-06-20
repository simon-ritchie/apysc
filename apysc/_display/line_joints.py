"""Line joints enum definitions.
"""

from enum import Enum


class LineJoints(Enum):
    """
    Line joints style type definitions.

    Attributes
    ----------
    MITER
        Default style type. Line vertices will be miter joint.
    ROUND
        Line vertices will be rounded.
    BEVEL
        Line vertices will be bevel joint (bevel vertices).
    """
    MITER = 'miter'
    ROUND = 'round'
    BEVEL = 'bevel'
