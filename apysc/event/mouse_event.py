"""Class implementation for mouse event.
"""

from typing import Generic
from typing import Optional
from typing import TypeVar

from apysc.event.event import Event
from apysc.type.variable_name_interface import VariableNameInterface
from apysc import Int

T = TypeVar('T', bound=VariableNameInterface)


class MouseEvent(Generic[T], Event):

    _this: T

    def __init__(self, this: T) -> None:
        """
        Mouse event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance that listening event (e.g., Sprite).
        """
        from apysc.expression import var_names
        super(MouseEvent, self).__init__(
            this=this, type_name=var_names.MOUSE_EVENT)

    @property
    def stage_x(self) -> Int:
        """
        Get the x-coordinate of the stage reference.

        Returns
        -------
        x : Int
            x-coordinate.
        """
        x: Int = Int(0)
        self._append_stage_x_getter_expression(x=x)
        return x

    def _append_stage_x_getter_expression(self, x: Int) -> None:
        """
        Append stage_x getter property expression to file.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        from apysc.display.stage import get_stage_variable_name
        from apysc.expression import expression_file_util
        stage_var_name: str = get_stage_variable_name()
        expression: str = (
            f'{x.variable_name} = {self.variable_name}.pageX - '
            f'{stage_var_name}.offset().left - '
            f'parseInt({stage_var_name}.css("margin-left")) - '
            f'parseInt({stage_var_name}.css("padding-left"));'
        )
        expression_file_util.append_js_expression(expression=expression)
