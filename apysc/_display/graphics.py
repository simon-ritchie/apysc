"""Implementations for Graphics class.
"""

from typing import List
from typing import Optional
from typing import Union

import apysc as ap
from apysc._display.begin_fill_interface import BeginFillInterface
from apysc._display.child_interface import ChildInterface
from apysc._display.circle import Circle
from apysc._display.display_object import DisplayObject
from apysc._display.ellipse import Ellipse
from apysc._display.graphics_clear_interface import GraphicsClearInterface
from apysc._display.line import Line
from apysc._display.line_style_interface import LineStyleInterface
from apysc._display.polygon import Polygon
from apysc._display.polyline import Polyline
from apysc._display.rectangle import Rectangle
from apysc._geom.point2d import Point2D
from apysc._type.variable_name_interface import VariableNameInterface


class Graphics(
        DisplayObject,
        BeginFillInterface, LineStyleInterface, VariableNameInterface,
        GraphicsClearInterface, ChildInterface):
    """
    Create a object that has each vector graphics interface.

    References
    ----------
    - Graphics document
        - https://simon-ritchie.github.io/apysc/graphics.html
    """

    _current_line: Optional[Polyline] = None

    def __init__(
            self, parent: 'ap.Sprite',
            variable_name: Optional[str] = None) -> None:
        """
        Create a object that has each vector graphics interface.

        Parameters
        ----------
        parent : Sprite
            This instance's parent instance.
        variable_name : str or None, default None
            Variable name to set. Specified only when subclass
            instantiation.

        References
        ----------
        - Graphics document
            - https://simon-ritchie.github.io/apysc/graphics.html
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Graphics):
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
            from apysc._validation import display_validation

            display_validation.validate_sprite(sprite=parent)
            self.parent_sprite: ap.Sprite = parent
            if variable_name is None:
                variable_name = expression_variables_util.\
                    get_next_variable_name(type_name=var_names.GRAPHICS)
            super(Graphics, self).__init__(
                stage=self.parent_sprite.stage, variable_name=variable_name)
            self._fill_color = ap.String('')
            self._fill_alpha = ap.Number(1.0)
            self._line_color = ap.String('')
            self._line_alpha = ap.Number(1.0)
            self._line_thickness = ap.Int(1.0)
            self._children = ap.Array([])
            self._append_constructor_expression()
            self.parent_sprite.add_child(self)
            self._set_overflow_visible_setting()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression.
        """
        with ap.DebugInfo(
                callable_=self._append_constructor_expression,
                locals_=locals(),
                module_name=__name__, class_=Graphics):
            stage_name: str = self.parent_sprite.stage.variable_name
            expression: str = (
                f'var {self.variable_name} = {stage_name}.nested();'
            )
            ap.append_js_expression(expression=expression)

    def draw_rect(
            self, x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            width: Union[int, ap.Int],
            height: Union[int, ap.Int]) -> Rectangle:
        """
        Draw a rectangle vector graphics.

        Parameters
        ----------
        x : int or Int
            X position to start drawing.
        y : int or Int
            Y position to start drawing.
        width : int or Int
            Rectangle width.
        height : int or Int
            Rectangle height.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.

        References
        ----------
        - Graphics draw_rect interface document
            - https://bit.ly/3zbSG9o
        """
        with ap.DebugInfo(
                callable_=self.draw_rect, locals_=locals(),
                module_name=__name__, class_=Graphics):
            rectangle: Rectangle = Rectangle(
                parent=self, x=x, y=y, width=width, height=height)
            self.add_child(child=rectangle)
            return rectangle

    def draw_round_rect(
            self, x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            width: Union[int, ap.Int],
            height: Union[int, ap.Int],
            ellipse_width: Union[int, ap.Int],
            ellipse_height: Union[int, ap.Int]) -> Rectangle:
        """
        Draw a rounded rectangle vector graphics.

        Parameters
        ----------
        x : int or Int
            X-coordinate to start drawing.
        y : int or Int
            Y-coordinate to start drawing.
        width : int or Int
            Rectangle width.
        height : int or Int
            Rectangle height.
        ellipse_width : int or Int
            Ellipse width of the rectangle corner.
        ellipse_height : int or Int
            Ellipse height of the rectangle corner.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.

        References
        ----------
        - Graphics draw_round_rect interface document
            - https://bit.ly/2ThGcxJ
        """
        with ap.DebugInfo(
                callable_=self.draw_round_rect, locals_=locals(),
                module_name=__name__, class_=Graphics):
            rectangle: Rectangle = Rectangle(
                parent=self, x=x, y=y, width=width, height=height)
            if isinstance(ellipse_width, int):
                ellipse_width = ap.Int(ellipse_width)
            if isinstance(ellipse_height, int):
                ellipse_height = ap.Int(ellipse_height)
            rectangle.ellipse_width = ellipse_width
            rectangle.ellipse_height = ellipse_height
            self.add_child(child=rectangle)
            return rectangle

    def draw_circle(
            self,
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            radius: Union[int, ap.Int]) -> Circle:
        """
        Draw a circle vector graphics.

        Parameters
        ----------
        x : int or Int
            X-coordinate of the circle center.
        y : int or Int
            Y-coordinate of the circle center.
        radius : int or Int
            Circle radius.

        Returns
        -------
        circle : Circle
            Created circle graphics instance.

        References
        ----------
        - Graphics draw_circle interface document
            - https://bit.ly/3it1q4y
        """
        with ap.DebugInfo(
                callable_=self.draw_circle, locals_=locals(),
                module_name=__name__, class_=Graphics):
            circle: Circle = Circle(parent=self, x=x, y=y, radius=radius)
            self.add_child(child=circle)
            return circle

    def draw_ellipse(
            self,
            x: Union[int, ap.Int],
            y: Union[int, ap.Int],
            width: Union[int, ap.Int],
            height: Union[int, ap.Int]) -> Ellipse:
        """
        Draw a ellipse vector graphics.

        Parameters
        ----------
        x : int or Int
            X-coordinate of the ellipse center.
        y : int or Int
            Y-coordinate of the ellipse center.
        width : int or Int
            Ellipse width.
        height : int or Int
            Ellipse height.

        Returns
        -------
        ellipse : Ellipse
            Created ellipse graphics instance.

        References
        ----------
        - Graphics draw_ellipse interface
            - https://bit.ly/3xPVicP
        """
        with ap.DebugInfo(
                callable_=self.draw_ellipse, locals_=locals(),
                module_name=__name__, class_=Graphics):
            ellipse: Ellipse = Ellipse(
                parent=self, x=x, y=y, width=width, height=height)
            self.add_child(child=ellipse)
            return ellipse

    def line_to(
            self, x: Union[int, ap.Int],
            y: Union[int, ap.Int]) -> Polyline:
        """
        Draw a line from previous point to specified point (initial
        point is x = 0, y = 0).

        Parameters
        ----------
        x : int or Int
            X destination point to draw line.
        y : int or Int
            Y destination point to draw line.

        Returns
        -------
        line : Polyline
            Line graphic instance.

        References
        ----------
        - Graphics move_to and line_to interfaces document
            - https://bit.ly/3eybhEP
        """
        with ap.DebugInfo(
                callable_=self.line_to, locals_=locals(),
                module_name=__name__, class_=Graphics):
            if self._current_line is None:
                self._current_line = Polyline(
                    parent=self,
                    points=ap.Array([Point2D(x=0, y=0), Point2D(x=x, y=y)]))
                self.add_child(self._current_line)
            else:
                self._current_line.append_line_point(x=x, y=y)
            return self._current_line

    def move_to(
            self, x: Union[int, ap.Int], y: Union[int, ap.Int]) -> Polyline:
        """
        Move a line position to specified point.

        Parameters
        ----------
        x : int or Int
            X destination point to move to.
        y : int or Int
            Y destination point to move to.

        Returns
        -------
        line : Polyline
            Line graphic instance.

        References
        ----------
        - Graphics move_to and line_to interfaces document
            - https://bit.ly/3eybhEP
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.move_to, locals_=locals(),
                module_name=__name__, class_=Graphics):
            self._current_line = Polyline(
                parent=self, points=ap.Array([Point2D(x=x, y=y)]))
            return self._current_line

    def _reset_each_line_settings(self) -> None:
        """
        Reset each line settings (e.g., LineDotSetting, LineDashSetting,
        and so on).

        Notes
        -----
        expression will not be appended.
        """
        self._line_dot_setting = None
        self._line_dash_setting = None
        self._line_round_dot_setting = None
        self._line_dash_dot_setting = None

    def draw_line(
            self,
            x_start: Union[int, ap.Int],
            y_start: Union[int, ap.Int],
            x_end: Union[int, ap.Int],
            y_end: Union[int, ap.Int]) -> Line:
        """
        Draw a normal line vector graphics.

        Notes
        -----
        - This interface will ignore line settings, like a
            LineDotSetting, LineDashSetting, and so on.

        Parameters
        ----------
        x_start : int or Int
            Line start x-coordinate.
        y_start : int or Int
            Line start y-coordinate.
        x_end : int or Int
            Line end x-coordinate.
        y_end : int or Int
            Line end y-coordinate.

        Returns
        -------
        line : Line
            Created line graphic instance.

        References
        ----------
        - Graphics draw_line interface document
            - https://bit.ly/3ey4pYe
        """
        with ap.DebugInfo(
                callable_=self.draw_line, locals_=locals(),
                module_name=__name__, class_=Graphics):
            snapshot_name: str = self._get_next_snapshot_name()
            self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
            self._reset_each_line_settings()
            line: Line = Line(
                parent=self,
                start_point=Point2D(x=x_start, y=y_start),
                end_point=Point2D(x=x_end, y=y_end))
            self._run_all_revert_methods(snapshot_name=snapshot_name)
            self.add_child(child=line)
            return line

    def draw_dotted_line(
            self,
            x_start: Union[int, ap.Int],
            y_start: Union[int, ap.Int],
            x_end: Union[int, ap.Int],
            y_end: Union[int, ap.Int],
            dot_size: Union[int, ap.Int]) -> Line:
        """
        Draw a dotted line vector graphics.

        Notes
        -----
        - This interface will ignore line settings, line a
            LineDashSetting, except LineDotSetting.

        Parameters
        ----------
        x_start : int or Int
            Line start x-coordinate.
        y_start : int or Int
            Line start y-coordinate.
        x_end : int or Int
            Line end x-coordinate.
        y_end : int or Int
            Line end y-coordinate.
        dot_size : int or Int
            Dot size.

        Returns
        -------
        line : Line
            Created line graphic instance.

        References
        ----------
        - Graphics draw_dotted_line interface document
            - https://bit.ly/3ig7Tzy
        """
        with ap.DebugInfo(
                callable_=self.draw_dotted_line, locals_=locals(),
                module_name=__name__, class_=Graphics):
            snapshot_name: str = self._get_next_snapshot_name()
            self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
            self._reset_each_line_settings()
            self._line_dot_setting = ap.LineDotSetting(dot_size=dot_size)
            line: Line = Line(
                parent=self,
                start_point=Point2D(x=x_start, y=y_start),
                end_point=Point2D(x=x_end, y=y_end))
            self._run_all_revert_methods(snapshot_name=snapshot_name)
            self.add_child(child=line)
            return line

    def draw_dashed_line(
            self,
            x_start: Union[int, ap.Int],
            y_start: Union[int, ap.Int],
            x_end: Union[int, ap.Int],
            y_end: Union[int, ap.Int],
            dash_size: Union[int, ap.Int],
            space_size: Union[int, ap.Int]) -> Line:
        """
        Draw a dashed line vector graphics.

        Notes
        -----
        - This interface will ignore line settings, like a
            LineDotSetting, except LineDashSetting.

        Parameters
        ----------
        x_start : int or Int
            Line start x-coordinate.
        y_start : int or Int
            Line start y-coordinate.
        x_end : int or Int
            Line end x-coordinate.
        y_end : int or Int
            Line end y-coordinate.
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dashes.

        Returns
        -------
        line : Line
            Created line graphic instance.

        References
        ----------
        - Graphics draw_dashed_line interface document
            - https://bit.ly/3ewoMF8
        """
        with ap.DebugInfo(
                callable_=self.draw_dashed_line, locals_=locals(),
                module_name=__name__, class_=Graphics):
            snapshot_name: str = self._get_next_snapshot_name()
            self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
            self._reset_each_line_settings()
            self._line_dash_setting = ap.LineDashSetting(
                dash_size=dash_size, space_size=space_size)
            line: Line = Line(
                parent=self,
                start_point=Point2D(x=x_start, y=y_start),
                end_point=Point2D(x=x_end, y=y_end))
            self._run_all_revert_methods(snapshot_name=snapshot_name)
            self.add_child(child=line)
            return line

    def draw_round_dotted_line(
            self,
            x_start: Union[int, ap.Int],
            y_start: Union[int, ap.Int],
            x_end: Union[int, ap.Int],
            y_end: Union[int, ap.Int],
            round_size: Union[int, ap.Int],
            space_size: Union[int, ap.Int]) -> Line:
        """
        Draw a round dotted line vector graphics.

        Notes
        -----
        - This interface will ignore line settings, like a
            LineDotSetting, except LineRoundDotSetting.

        Parameters
        ----------
        x_start : int or Int
            Line start x-coordinate.
        y_start : int or Int
            Line start y-coordinate.
        x_end : int or Int
            Line end x-coordinate.
        y_end : int or Int
            Line end y-coordinate.
        round_size : int or Int
            Dot round size.
        space_size : int or Int
            Blank space size between dots.

        Returns
        -------
        line : Line
            Created line graphic instance.

        References
        ----------
        - Graphics draw_round_dotted_line interface document
            - https://bit.ly/3ri985m
        """
        with ap.DebugInfo(
                callable_=self.draw_round_dotted_line, locals_=locals(),
                module_name=__name__, class_=Graphics):
            snapshot_name: str = self._get_next_snapshot_name()
            self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
            self._reset_each_line_settings()
            self._line_round_dot_setting = ap.LineRoundDotSetting(
                round_size=round_size, space_size=space_size)
            line: Line = Line(
                parent=self,
                start_point=Point2D(x=x_start, y=y_start),
                end_point=Point2D(x=x_end, y=y_end))
            self._run_all_revert_methods(snapshot_name=snapshot_name)
            self.add_child(child=line)
            return line

    def draw_dash_dotted_line(
            self,
            x_start: Union[int, ap.Int],
            y_start: Union[int, ap.Int],
            x_end: Union[int, ap.Int],
            y_end: Union[int, ap.Int],
            dot_size: Union[int, ap.Int],
            dash_size: Union[int, ap.Int],
            space_size: Union[int, ap.Int]) -> Line:
        """
        Draw a dash dotted (1-dot chain) line vector graphics.

        Parameters
        ----------
        x_start : int or Int
            Line start x-coordinate.
        y_start : int or Int
            Line start y-coordinate.
        x_end : int or Int
            Line end x-coordinate.
        y_end : int or Int
            Line end y-coordinate.
        dot_size : int or Int
            Dot size.
        dash_size : int or Int
            Dash size.
        space_size : int or Int
            Blank space size between dots and dashes.

        Returns
        -------
        line : Line
            Created line graphic instance.

        References
        ----------
        - Graphics draw_dash_dotted_line interface document
            - https://bit.ly/3wKRtUZ
        """
        with ap.DebugInfo(
                callable_=self.draw_dash_dotted_line, locals_=locals(),
                module_name=__name__, class_=Graphics):
            snapshot_name: str = self._get_next_snapshot_name()
            self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
            self._reset_each_line_settings()
            self._line_dash_dot_setting = ap.LineDashDotSetting(
                dot_size=dot_size,
                dash_size=dash_size,
                space_size=space_size)
            line: Line = Line(
                parent=self,
                start_point=Point2D(x=x_start, y=y_start),
                end_point=Point2D(x=x_end, y=y_end))
            self._run_all_revert_methods(snapshot_name=snapshot_name)
            self.add_child(child=line)
            return line

    def draw_polygon(
            self, points: Union[List[Point2D], ap.Array[Point2D]]) -> Polygon:
        """
        Draw a polygon vector graphics. This is similar to Polyline
        class (created by move_to or line_to, or other interface),
        but unlike that, end point and start one will be connected.

        Parameters
        ----------
        points : list of Point2D or Array.
            Polygon vertex points.

        Returns
        -------
        polygon : Polygon
            Created polygon graphic instance.

        References
        ----------
        - Graphics draw_polygon interface document
            - https://bit.ly/3wHVZUk
        """
        with ap.DebugInfo(
                callable_=self.draw_polygon, locals_=locals(),
                module_name=__name__, class_=Graphics):
            if isinstance(points, list):
                points = ap.Array(points)
            polygon: Polygon = Polygon(parent=self, points=points)
            self.add_child(polygon)
            return polygon

    def __repr__(self) -> str:
        """
        Get a string representation of this instance (for the sake of
        debugging).

        Returns
        -------
        repr_str : str
            Type name and variable name will be set
            (e.g., `Graphics('<variable_name>')`).
        """
        repr_str: str = f"Graphics('{self.variable_name}')"
        return repr_str
