"""Implementations for Graphics class.
"""

from typing import Any
from typing import Optional
from typing import Union

from apysc import Int
from apysc.display.begin_fill_interface import BeginFillInterface
from apysc.display.child_interface import ChildInterface
from apysc.display.graphics_clear_interface import GraphicsClearInterface
from apysc.display.line_style_interface import LineStyleInterface
from apysc.display.rectangle import Rectangle
from apysc.type.variable_name_interface import VariableNameInterface


class Graphics(
        BeginFillInterface, LineStyleInterface, VariableNameInterface,
        GraphicsClearInterface, ChildInterface):

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
        Draw rectangle vector graphics.

        Parameters
        ----------
        x : int
            X position to start drawing.
        y : int
            Y position to start drawing.
        width : int
            Rectangle width.
        height : int
            Rectangle height.

        Returns
        -------
        rectangle : Rectangle
            Created rectangle.
        """
        from apysc.display.rectangle import append_draw_rect_expression
        rectangle: Rectangle = Rectangle(
            parent=self, x=x, y=y, width=width, height=height,
            fill_color=self.fill_color, fill_alpha=self.fill_alpha,
            line_color=self.line_color, line_thickness=self.line_thickness,
            line_alpha=self.line_alpha)
        append_draw_rect_expression(rectangle=rectangle)
        self.add_child(child=rectangle)
        return rectangle
