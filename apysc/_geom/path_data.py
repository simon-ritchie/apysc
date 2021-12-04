"""Class definitions of each path data class.
"""

from apysc._geom.path_bezier_2d import PathBezier2D
from apysc._geom.path_bezier_2d_continual import PathBezier2DContinual
from apysc._geom.path_bezier_3d import PathBezier3D
from apysc._geom.path_bezier_3d_continual import PathBezier3DContinual
from apysc._geom.path_close import PathClose
from apysc._geom.path_horizontal import PathHorizontal
from apysc._geom.path_line_to import PathLineTo
from apysc._geom.path_move_to import PathMoveTo
from apysc._geom.path_vertical import PathVertical


class PathData:
    """
    Class definitions of each path data class.
    """
    MoveTo = PathMoveTo
    LineTo = PathLineTo
    Horizontal = PathHorizontal
    Vertical = PathVertical
    Close = PathClose
    Bezier2D = PathBezier2D
    Bezier2DContinual = PathBezier2DContinual
    Bezier3D = PathBezier3D
    Bezier3DContinual = PathBezier3DContinual
