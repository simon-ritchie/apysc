"""Implementations for Graphics class.
"""

from typing import Any
from typing import List
from typing import Optional
from typing import Union

from apysc import Array
from apysc import Int
from apysc.display.begin_fill_interface import BeginFillInterface
from apysc.display.child_interface import ChildInterface
from apysc.display.circle import Circle
from apysc.display.ellipse import Ellipse
from apysc.display.graphics_clear_interface import GraphicsClearInterface
from apysc.display.line import Line
from apysc.display.line_style_interface import LineStyleInterface
from apysc.display.polygon import Polygon
from apysc.display.polyline import Polyline
from apysc.display.rectangle import Rectangle
from apysc.geom.point2d import Point2D
from apysc.type.variable_name_interface import VariableNameInterface


class Graphics(
        BeginFillInterface, LineStyleInterface, VariableNameInterface,
        GraphicsClearInterface, ChildInterface):

    _current_line: Optional[Polyline] = None

    def __init__(
            self, parent: Any,
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
        """
        from apysc import Array
        from apysc import Number
        from apysc import Sprite
        from apysc import String
        from apysc.expression import expression_variables_util
        from apysc.expression import var_names
        from apysc.validation import display_validation

        display_validation.validate_sprite(sprite=parent)
        self.parent_sprite: Sprite = parent
        if variable_name is None:
            variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.GRAPHICS)
        self.variable_name = variable_name
        self._fill_color = String('')
        self._fill_alpha = Number(1.0)
        self._line_color = String('')
        self._line_alpha = Number(1.0)
        self._line_thickness = Int(1.0)
        self._children = Array([])
        self._append_constructor_expression()

    def _append_constructor_expression(self) -> None:
        """
        Append constructor expression to file.
        """
        from apysc.expression import expression_file_util
        stage_name: str = self.parent_sprite.stage.variable_name
        parent_name: str = self.parent_sprite.variable_name
        expression: str = (
            f'var {self.variable_name} = {stage_name}.nested();'
            f'\n{parent_name}.add({self.variable_name});'
        )
        expression_file_util.append_js_expression(expression=expression)

    def draw_rect(
            self, x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int]) -> Rectangle:
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
        """
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height)
        self.add_child(child=rectangle)
        return rectangle

    def draw_round_rect(
            self, x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int],
            ellipse_width: Union[int, Int],
            ellipse_height: Union[int, Int]) -> Rectangle:
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
        """
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height)
        if isinstance(ellipse_width, int):
            ellipse_width = Int(ellipse_width)
        if isinstance(ellipse_height, int):
            ellipse_height = Int(ellipse_height)
        rectangle.ellipse_width = ellipse_width
        rectangle.ellipse_height = ellipse_height
        self.add_child(child=rectangle)
        return rectangle

    def draw_circle(
            self,
            x: Union[int, Int],
            y: Union[int, Int],
            radius: Union[int, Int]) -> Circle:
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
        """
        circle: Circle = Circle(parent=self, x=x, y=y, radius=radius)
        self.add_child(child=circle)
        return circle

    def draw_ellipse(
            self,
            x: Union[int, Int],
            y: Union[int, Int],
            width: Union[int, Int],
            height: Union[int, Int]) -> Ellipse:
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
        """
        ellipse: Ellipse = Ellipse(
            parent=self, x=x, y=y, width=width, height=height)
        self.add_child(child=ellipse)
        return ellipse

    def line_to(self, x: Union[int, Int], y: Union[int, Int]) -> Polyline:
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
        """
        from apysc import Array
        if self._current_line is None:
            self._current_line = Polyline(
                parent=self,
                points=Array([Point2D(x=0, y=0), Point2D(x=x, y=y)]))
            self.add_child(self._current_line)
        else:
            self._current_line.append_line_point(x=x, y=y)
        return self._current_line

    def move_to(self, x: Union[int, Int], y: Union[int, Int]) -> Polyline:
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
        """
        from apysc import Array
        self._current_line = Polyline(
            parent=self, points=Array([Point2D(x=x, y=y)]))
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
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int]) -> Line:
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
        """
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
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            dot_size: Union[int, Int]) -> Line:
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
        """
        from apysc import LineDotSetting
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dot_setting = LineDotSetting(dot_size=dot_size)
        line: Line = Line(
            parent=self,
            start_point=Point2D(x=x_start, y=y_start),
            end_point=Point2D(x=x_end, y=y_end))
        self._run_all_revert_methods(snapshot_name=snapshot_name)
        self.add_child(child=line)
        return line

    def draw_dashed_line(
            self,
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> Line:
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
        """
        from apysc import LineDashSetting
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dash_setting = LineDashSetting(
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
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            round_size: Union[int, Int],
            space_size: Union[int, Int]) -> Line:
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
        """
        from apysc import LineRoundDotSetting
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_round_dot_setting = LineRoundDotSetting(
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
            x_start: Union[int, Int],
            y_start: Union[int, Int],
            x_end: Union[int, Int],
            y_end: Union[int, Int],
            dot_size: Union[int, Int],
            dash_size: Union[int, Int],
            space_size: Union[int, Int]) -> Line:
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
        """
        from apysc import LineDashDotSetting
        snapshot_name: str = self._get_next_snapshot_name()
        self._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        self._reset_each_line_settings()
        self._line_dash_dot_setting = LineDashDotSetting(
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
            self, points: Union[List[Point2D], Array[Point2D]]) -> Polygon:
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
        """
        if isinstance(points, list):
            points = Array(points)
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
