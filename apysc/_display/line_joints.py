"""Line joints enum's definitions.
"""

from enum import Enum


class LineJoints(Enum):
    """
    The class for the line joints' style type definitions.

    Attributes
    ----------
    MITER
        Default style type. Line vertices will be miter joint.
    ROUND
        Line vertices will be rounded.
    BEVEL
        Line vertices will be bevel joint (bevel vertices).

    References
    ----------
    - Graphics line_style interface
        - https://simon-ritchie.github.io/apysc/en/graphics_line_style.html
    """

    MITER = "miter"
    ROUND = "round"
    BEVEL = "bevel"
