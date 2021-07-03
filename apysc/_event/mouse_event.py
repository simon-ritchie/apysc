"""Class implementation for the mouse event.
"""

from typing import Generic
from typing import TypeVar

from apysc import Int
from apysc._event.event import Event
from apysc._type.variable_name_interface import VariableNameInterface

T = TypeVar('T', bound=VariableNameInterface)


class MouseEvent(Event, Generic[T]):

    _this: T

    def __init__(self, this: T) -> None:
        """
        Mouse event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance that listening event (e.g., Sprite).
        """
        from apysc._expression import var_names
        super(MouseEvent, self).__init__(
            this=this, type_name=var_names.MOUSE_EVENT)

    @property
    def this(self) -> T:
        """
        Get instance that listening this event.

        Returns
        -------
        this : VariableNameInterface
            Instance that listening this event.
        """
        return super(MouseEvent, self).this

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
        from apysc import append_js_expression
        from apysc._display.stage import get_stage_elem_str
        expression: str = (
            f'{x.variable_name} = {self.variable_name}.pageX - '
            f'{get_stage_elem_str()}.offset().left;'
        )
        append_js_expression(expression=expression)

    @property
    def stage_y(self) -> Int:
        """
        Get the y-coordinate of the stage reference.

        Returns
        -------
        y : Int
            y-coordinate.
        """
        y: Int = Int(0)
        self._append_stage_y_getter_expression(y=y)
        return y

    def _append_stage_y_getter_expression(self, y: Int) -> None:
        """
        Append stage_y getter property expression to file.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        from apysc import append_js_expression
        from apysc._display.stage import get_stage_elem_str
        expression: str = (
            f'{y.variable_name} = {self.variable_name}.pageY - '
            f'{get_stage_elem_str()}.offset().top;'
        )
        append_js_expression(expression=expression)

    @property
    def local_x(self) -> Int:
        """
        Get the local x-coordinate of the event listening instance.
        For example, if a Sprite instance is clicked, this value will be
        x-coordinate from Sprite's left end position.

        Returns
        -------
        x : Int
            x-coordinate.
        """
        x: Int = Int(0)
        self._append_local_x_getter_expression(x=x)
        return x

    def _append_local_x_getter_expression(self, x: Int) -> None:
        """
        Append local_x getter property expression to file.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        from apysc import append_js_expression
        stage_x: Int = self.stage_x
        this: T = self.this
        expression: str = (
            f'{x.variable_name} = {stage_x.variable_name} - '
            f'get_total_x({this.variable_name});'
        )
        append_js_expression(expression=expression)

    @property
    def local_y(self) -> Int:
        """
        Get the local y-coordinate of the event listening instance.
        For example, if a Sprite instance is clicked, this value will be
        y-coordinate from Sprite's top end position.

        Returns
        -------
        y : Int
            y-coordinate.
        """
        y: Int = Int(0)
        self._append_local_y_getter_expression(y=y)
        return y

    def _append_local_y_getter_expression(self, y: Int) -> None:
        """
        Append local_y getter property expression to file.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        from apysc import append_js_expression
        stage_y: Int = self.stage_y
        this: T = self.this
        expression: str = (
            f'{y.variable_name} = {stage_y.variable_name} - '
            f'get_total_y({this.variable_name});'
        )
        append_js_expression(expression=expression)
