"""Implementations of the Path class.
"""

from typing import Any, List

from apysc._display.line_base import LineBase
from apysc._geom.path_data_base import PathDataBase

_Graphics = Any


class Path(LineBase):
    """
    The path vector graphics class.
    """

    _path_data_list: List[PathDataBase]

    def __init__(
            self,
            parent: _Graphics,
            path_data_list: List[PathDataBase]) -> None:
        """
        Create a path vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        path_data_list : list of PathDataBase
            Target path data settings, such as the ap.PathData.MoveTo.
        """
        from apysc._display.graphics import Graphics
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        parent_graphics: Graphics = parent
        variable_name: str = expression_variables_util.get_next_variable_name(
            type_name=var_names.PATH)
        super(Path, self).__init__(
            parent=parent, x=0, y=0, variable_name=variable_name)
        self._path_data_list = path_data_list
        self._set_initial_basic_values(parent=parent)
        self._set_line_setting_if_not_none_value_exists(
            parent_graphics=parent_graphics)
        self._set_overflow_visible_setting()

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Path('<variable_name>')`).
        """
