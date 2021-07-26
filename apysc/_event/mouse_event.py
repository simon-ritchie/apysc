"""Class implementation for the mouse event.
"""

from typing import Generic
from typing import TypeVar

import apysc as ap
from apysc._event.event import Event
from apysc._type.variable_name_interface import VariableNameInterface

T = TypeVar('T', bound=VariableNameInterface)


class MouseEvent(Event, Generic[T]):
    """
    Mouse event class.

    References
    ----------
    - Common mouse event interfaces
        - https://bit.ly/3eDWY1v
    """

    _this: T

    def __init__(self, this: T) -> None:
        """
        Mouse event class.

        Parameters
        ----------
        this : VariableNameInterface
            Instance that listening event (e.g., Sprite).

        References
        ----------
        - Common mouse event interfaces
            - https://bit.ly/3eDWY1v
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
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

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_common.html
        """
        return super(MouseEvent, self).this

    @property
    def stage_x(self) -> ap.Int:
        """
        Get the x-coordinate of the stage reference.

        Returns
        -------
        x : Int
            x-coordinate.

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_common.html
        """
        with ap.DebugInfo(
                callable_='stage_x', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            x: ap.Int = ap.Int(0)
            self._append_stage_x_getter_expression(x=x)
            return x

    def _append_stage_x_getter_expression(self, x: ap.Int) -> None:
        """
        Append stage_x getter property expression to file.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        with ap.DebugInfo(
                callable_=self._append_stage_x_getter_expression,
                locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            from apysc._display.stage import get_stage_elem_str
            expression: str = (
                f'{x.variable_name} = {self.variable_name}.pageX - '
                f'{get_stage_elem_str()}.offset().left;'
            )
            ap.append_js_expression(expression=expression)

    @property
    def stage_y(self) -> ap.Int:
        """
        Get the y-coordinate of the stage reference.

        Returns
        -------
        y : Int
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_common.html
        """
        with ap.DebugInfo(
                callable_='stage_y', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            y: ap.Int = ap.Int(0)
            self._append_stage_y_getter_expression(y=y)
            return y

    def _append_stage_y_getter_expression(self, y: ap.Int) -> None:
        """
        Append stage_y getter property expression to file.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        with ap.DebugInfo(
                callable_=self._append_stage_y_getter_expression,
                locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            from apysc._display.stage import get_stage_elem_str
            expression: str = (
                f'{y.variable_name} = {self.variable_name}.pageY - '
                f'{get_stage_elem_str()}.offset().top;'
            )
            ap.append_js_expression(expression=expression)

    @property
    def local_x(self) -> ap.Int:
        """
        Get the local x-coordinate of the event listening instance.
        For example, if a Sprite instance is clicked, this value will be
        x-coordinate from Sprite's left end position.

        Returns
        -------
        x : Int
            x-coordinate.

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_common.html
        """
        with ap.DebugInfo(
                callable_='local_x', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            x: ap.Int = ap.Int(0)
            self._append_local_x_getter_expression(x=x)
            return x

    def _append_local_x_getter_expression(self, x: ap.Int) -> None:
        """
        Append local_x getter property expression to file.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_local_x_getter_expression,
                locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            stage_x: ap.Int = self.stage_x
            this: T = self.this
            expression: str = (
                f'{x.variable_name} = {stage_x.variable_name} - '
                f'get_total_x({this.variable_name});'
            )
            ap.append_js_expression(expression=expression)

    @property
    def local_y(self) -> ap.Int:
        """
        Get the local y-coordinate of the event listening instance.
        For example, if a Sprite instance is clicked, this value will be
        y-coordinate from Sprite's top end position.

        Returns
        -------
        y : Int
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_common.html
        """
        with ap.DebugInfo(
                callable_='local_y', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            y: ap.Int = ap.Int(0)
            self._append_local_y_getter_expression(y=y)
            return y

    def _append_local_y_getter_expression(self, y: ap.Int) -> None:
        """
        Append local_y getter property expression to file.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_local_y_getter_expression,
                locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            stage_y: ap.Int = self.stage_y
            this: T = self.this
            expression: str = (
                f'{y.variable_name} = {stage_y.variable_name} - '
                f'get_total_y({this.variable_name});'
            )
            ap.append_js_expression(expression=expression)
