"""Class implementation for the mouse event.
"""

from typing import Generic
from typing import TypeVar

from typing_extensions import final

from apysc._event.event import Event
from apysc._event.prevent_default_mixin import PreventDefaultMixIn
from apysc._event.stop_propagation_mixin import StopPropagationMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos

T = TypeVar("T", bound=VariableNameMixIn)


class MouseEvent(Event[T], Generic[T], StopPropagationMixIn, PreventDefaultMixIn):
    """
    Mouse event class.

    References
    ----------
    - Basic mouse event interfaces
        - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

    Examples
    --------
    >>> import apysc as ap
    >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    ...     rectangle: ap.Rectangle = e.this
    ...     rectangle.fill_color = ap.String("#f0a")
    ...     rectangle.unbind_mousedown_all()
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color="#0af")
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> _ = rectangle.mousedown(on_mousedown)
    """

    @final
    @arg_validation_decos.is_variable_name_interface_type(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, this: T) -> None:
        """
        Mouse event class.

        Parameters
        ----------
        this : VariableNameMixIn
            An instance of a listening event (e.g., Sprite).

        References
        ----------
        - Basic mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> e: ap.MouseEvent = ap.MouseEvent(this=rectangle)
        """
        from apysc._expression import var_names

        super(MouseEvent, self).__init__(this=this, type_name=var_names.MOUSE_EVENT)

    @property
    @add_debug_info_setting(module_name=__name__)
    def stage_x(self) -> Int:
        """
        Get the x-coordinate of the stage reference.

        Returns
        -------
        x : Int
            x-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_x: ap.Int = e.stage_x
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap

        x: ap.Int = ap.Int(0)
        self._append_stage_x_getter_expression(x=x)
        return x

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_stage_x_getter_expression(self, *, x: Int) -> None:
        """
        Append stage_x getter property expression.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        import apysc as ap
        from apysc._display.stage import get_stage_elem_str

        expression: str = (
            f"{x.variable_name} = {self.variable_name}.pageX - "
            f"{get_stage_elem_str()}.offset().left;"
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def stage_y(self) -> Int:
        """
        Get the y-coordinate of the stage reference.

        Returns
        -------
        y : Int
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_y: ap.Int = e.stage_y
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap

        y: ap.Int = ap.Int(0)
        self._append_stage_y_getter_expression(y=y)
        return y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_stage_y_getter_expression(self, *, y: Int) -> None:
        """
        Append stage_y getter property expression.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        import apysc as ap
        from apysc._display.stage import get_stage_elem_str

        expression: str = (
            f"{y.variable_name} = {self.variable_name}.pageY - "
            f"{get_stage_elem_str()}.offset().top;"
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def local_x(self) -> Int:
        """
        Get a local x-coordinate event listening instance.
        For example, this value becomes x-coordinate from
        Sprite's left-end position by clicking a Sprite instance.

        Returns
        -------
        x : Int
            x-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     local_x: ap.Int = e.local_x
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap

        x: ap.Int = ap.Int(0)
        self._append_local_x_getter_expression(x=x)
        return x

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_local_x_getter_expression(self, *, x: Int) -> None:
        """
        Append local_x getter property expression.

        Parameters
        ----------
        x : Int
            Target x-coordinate value.
        """
        import apysc as ap

        stage_x: ap.Int = self.stage_x
        this: T = self.this
        expression: str = (
            f"{x.variable_name} = {stage_x.variable_name} - "
            f"get_total_x({this.variable_name});"
        )
        ap.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def local_y(self) -> Int:
        """
        Get the local y-coordinate of the event listening instance.
        For example, this value becomes y-coordinate from Sprite's
        top-end position by clicking a Sprite instance.

        Returns
        -------
        y : Int
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     local_y: ap.Int = e.local_y
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color="#0af")
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        import apysc as ap

        y: ap.Int = ap.Int(0)
        self._append_local_y_getter_expression(y=y)
        return y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_local_y_getter_expression(self, *, y: Int) -> None:
        """
        Append local_y getter property expression.

        Parameters
        ----------
        y : Int
            Target y-coordinate value.
        """
        import apysc as ap

        stage_y: ap.Int = self.stage_y
        this: T = self.this
        expression: str = (
            f"{y.variable_name} = {stage_y.variable_name} - "
            f"get_total_y({this.variable_name});"
        )
        ap.append_js_expression(expression=expression)
