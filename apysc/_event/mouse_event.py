"""Class implementation for the mouse event.
"""

from typing import Generic
from typing import TypeVar

from apysc._event.event import Event
from apysc._event.prevent_default_interface import PreventDefaultInterface
from apysc._event.stop_propagation_interface import StopPropagationInterface
from apysc._type.int import Int
from apysc._type.variable_name_interface import VariableNameInterface

T = TypeVar('T', bound=VariableNameInterface)


class MouseEvent(
        Event[T], Generic[T], StopPropagationInterface,
        PreventDefaultInterface):
    """
    Mouse event class.

    References
    ----------
    - Common mouse event interfaces
        - https://bit.ly/3eDWY1v

    Examples
    --------
    >>> import apysc as ap
    >>> def on_mousedown(
    ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    ...     rectangle: ap.Rectangle = e.this
    ...     rectangle.fill_color = ap.String('#f0a')
    ...     rectangle.unbind_mousedown_all()
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color='#0af')
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50)
    >>> _ = rectangle.mousedown(on_mousedown)
    """

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

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> e: ap.MouseEvent = ap.MouseEvent(this=rectangle)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            from apysc._expression import var_names
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

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_x: ap.Int = e.stage_x
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='stage_x', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            x: ap.Int = ap.Int(0)
            self._append_stage_x_getter_expression(x=x)
            return x

    def _append_stage_x_getter_expression(self, *, x: Int) -> None:
        """
        Append stage_x getter property expression.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        import apysc as ap
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
    def stage_y(self) -> Int:
        """
        Get the y-coordinate of the stage reference.

        Returns
        -------
        y : Int
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces document
            - https://simon-ritchie.github.io/apysc/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_y: ap.Int = e.stage_y
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='stage_y', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            y: ap.Int = ap.Int(0)
            self._append_stage_y_getter_expression(y=y)
            return y

    def _append_stage_y_getter_expression(self, *, y: Int) -> None:
        """
        Append stage_y getter property expression.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        import apysc as ap
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
    def local_x(self) -> Int:
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
            - https://simon-ritchie.github.io/apysc/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     local_x: ap.Int = e.local_x
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='local_x', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            x: ap.Int = ap.Int(0)
            self._append_local_x_getter_expression(x=x)
            return x

    def _append_local_x_getter_expression(self, *, x: Int) -> None:
        """
        Append local_x getter property expression.

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
    def local_y(self) -> Int:
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
            - https://simon-ritchie.github.io/apysc/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(
        ...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     local_y: ap.Int = e.local_y
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color='#0af')
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50)
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='local_y', locals_=locals(),
                module_name=__name__, class_=MouseEvent):
            y: ap.Int = ap.Int(0)
            self._append_local_y_getter_expression(y=y)
            return y

    def _append_local_y_getter_expression(self, *, y: Int) -> None:
        """
        Append local_y getter property expression.

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
