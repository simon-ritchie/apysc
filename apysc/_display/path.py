"""Implementations of the Path class.
"""

from typing import List

from apysc._display import graphics
from apysc._display.line_base import LineBase
from apysc._geom.path_data_base import PathDataBase


class Path(LineBase):
    """
    The path vector graphics class.

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.line_style(color='#fff', thickness=3)
    >>> path: ap.Path = sprite.graphics.draw_path(
    ...     path_data_list=[
    ...         ap.PathMoveTo(x=0, y=50),
    ...         ap.PathBezier2D(
    ...             control_x=50, control_y=0,
    ...             dest_x=100, dest_y=50),
    ...     ])
    """

    _path_data_list: List[PathDataBase]

    def __init__(
            self,
            *,
            parent: 'graphics.Graphics',
            path_data_list: List[PathDataBase]) -> None:
        """
        Create a path vector graphics.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        path_data_list : list of PathDataBase
            Target path data settings, such as the ap.PathData.MoveTo.

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.line_style(color='#fff', thickness=3)
        >>> path: ap.Path = sprite.graphics.draw_path(
        ...     path_data_list=[
        ...         ap.PathMoveTo(x=0, y=50),
        ...         ap.PathBezier2D(
        ...             control_x=50, control_y=0,
        ...             dest_x=100, dest_y=50),
        ...     ])
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Path):
            from apysc._display.graphics import Graphics
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._validation import path_validation
            path_validation.validate_path_data_list(
                path_data_list=path_data_list)
            parent_graphics: Graphics = parent
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.PATH)
            super(Path, self).__init__(
                parent=parent, x=0, y=0, variable_name=variable_name)
            self._path_data_list = path_data_list
            self._set_initial_basic_values(parent=parent)
            self._append_constructor_expression()
            self._set_line_setting_if_not_none_value_exists(
                parent_graphics=parent_graphics)
            self._set_overflow_visible_setting()

    def _append_constructor_expression(self) -> None:
        """
        Append a constructor expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Path):
            from apysc._display.stage import get_stage_variable_name
            from apysc._geom.path_data_util import \
                make_paths_expression_from_list
            from apysc._string import indent_util
            stage_variable_name: str = get_stage_variable_name()
            path_data_expression: str = make_paths_expression_from_list(
                path_data_list=self._path_data_list)
            INDENT_NUM: int = 2
            expression: str = (
                f'var {self.variable_name} = {stage_variable_name}'
                f'\n  .path({path_data_expression})'
                '\n  .attr({'
            )
            expression = self._append_basic_vals_expression(
                expression=expression,
                indent_num=INDENT_NUM)
            spaces: str = indent_util.make_spaces_for_html(
                indent_num=INDENT_NUM)
            if self._fill_color._value == '':
                expression += f'\n{spaces}fill: "transparent",'
            expression += '\n  });'
            ap.append_js_expression(expression=expression)

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
        repr_str: str = f"Path('{self.variable_name}')"
        return repr_str
