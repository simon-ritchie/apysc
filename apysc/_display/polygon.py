"""Implementations of Polygon class.
"""


from apysc._display import graphics
from apysc._display.append_line_point_interface import AppendLinePointInterface
from apysc._display.line_base import LineBase
from apysc._geom.point2d import Point2D
from apysc._type.array import Array


class Polygon(LineBase, AppendLinePointInterface):
    """
    The polygon vector graphics class.

    References
    ----------
    - Graphics draw_polygon interface document
        - https://bit.ly/3wHVZUk

    Examples
    --------
    >>> import apysc as ap
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
    ...     points=[
    ...         ap.Point2D(x=50, y=50),
    ...         ap.Point2D(x=50, y=100),
    ...         ap.Point2D(x=100, y=75),
    ...     ])
    >>> polygon.fill_color
    String('#00aaff')
    """

    def __init__(
            self, *, parent: 'graphics.Graphics',
            points: Array[Point2D]) -> None:
        """
        Create a polygon vector graphic. This is similar to Polyline
        class, but unlike that, end point and start point will be
        connected.

        Parameters
        ----------
        parent : Graphics
            Graphics instance to link this graphic.
        points : Array of Point2D
            List of polygon vertex points.

        References
        ----------
        - Graphics draw_polygon interface document
            - https://bit.ly/3wHVZUk

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
        ...     points=[
        ...         ap.Point2D(x=50, y=50),
        ...         ap.Point2D(x=50, y=100),
        ...         ap.Point2D(x=100, y=75),
        ...     ])
        >>> polygon.fill_color
        String('#00aaff')
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Polygon):
            from apysc._display.graphics import Graphics
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            parent_graphics: Graphics = parent
            variable_name: str = expression_variables_util.\
                get_next_variable_name(type_name=var_names.POLYGON)
            super(Polygon, self).__init__(
                parent=parent, x=0, y=0, variable_name=variable_name)
            self.points = points
            self._set_initial_basic_values(parent=parent)
            self._append_constructor_expression()
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
            (e.g., `Polygon('<variable_name>')`).
        """
        repr_str: str = f"Polygon('{self.variable_name}')"
        return repr_str

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Polygon):
            from apysc._display.stage import get_stage_variable_name
            stage_variable_name: str = get_stage_variable_name()
            points_var_name: str
            points_expression: str
            points_var_name, points_expression = \
                self._make_2dim_points_expression()
            expression: str = (
                f'{points_expression}'
                f'\nvar {self.variable_name} = {stage_variable_name}'
                f'\n  .polygon({points_var_name})'
                '\n  .attr({'
            )
            expression = self._append_basic_vals_expression(
                expression=expression, indent_num=2)
            expression += '\n  });'
            ap.append_js_expression(expression=expression)
            self._points_var_name = points_var_name
