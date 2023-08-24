"""Class implementation for the mouse event.
"""

from typing import Generic
from typing import TypeVar

from typing_extensions import final

from apysc._event.event import Event
from apysc._event.prevent_default_mixin import PreventDefaultMixIn
from apysc._event.stop_propagation_mixin import StopPropagationMixIn
from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.number import Number
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos

_Target = TypeVar("_Target", bound=VariableNameMixIn)


class MouseEvent(
    Event[_Target],
    Generic[_Target],
    StopPropagationMixIn,
    PreventDefaultMixIn,
):
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
    ...     rectangle.fill_color = ap.Color("#f0a")
    ...     rectangle.unbind_mousedown_all()
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> _ = rectangle.mousedown(on_mousedown)
    """

    @final
    @arg_validation_decos.is_variable_name_interface_type(arg_position_index=1)
    @add_debug_info_setting(module_name=__name__)
    def __init__(self, *, this: _Target) -> None:
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
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> e: ap.MouseEvent = ap.MouseEvent(this=rectangle)
        """
        from apysc._expression import var_names

        super(MouseEvent, self).__init__(this=this, type_name=var_names.MOUSE_EVENT)

    @property
    @add_debug_info_setting(module_name=__name__)
    def stage_x(self) -> Number:
        """
        Get the x-coordinate of the stage reference.

        Returns
        -------
        x : Number
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
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        x: Number = Number(0)
        self._append_stage_x_getter_expression(x=x)
        return x

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_stage_x_getter_expression(self, *, x: Number) -> None:
        """
        Append stage_x getter property expression.

        Parameters
        ----------
        x : Number
            Target x-coordinate value.
        """
        from apysc._display.stage import get_stage_elem_str
        from apysc._expression import expression_data_util

        expression: str = (
            f"{x.variable_name} = {self.variable_name}.pageX - "
            f"{get_stage_elem_str()}.offset().left;"
        )
        expression_data_util.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def stage_y(self) -> Number:
        """
        Get the y-coordinate of the stage reference.

        Returns
        -------
        y : Number
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     stage_y: ap.Number = e.stage_y
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        y: Number = Number(0)
        self._append_stage_y_getter_expression(y=y)
        return y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_stage_y_getter_expression(self, *, y: Number) -> None:
        """
        Append stage_y getter property expression.

        Parameters
        ----------
        y : Number
            Target y-coordinate value.
        """
        from apysc._display.stage import get_stage_elem_str
        from apysc._expression import expression_data_util

        expression: str = (
            f"{y.variable_name} = {self.variable_name}.pageY - "
            f"{get_stage_elem_str()}.offset().top;"
        )
        expression_data_util.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def local_x(self) -> Number:
        """
        Get a local x-coordinate event listening instance.
        For example, this value becomes x-coordinate from
        Sprite's left-end position by clicking a Sprite instance.

        Returns
        -------
        x : Number
            x-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     local_x: ap.Number = e.local_x
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        x: Number = Number(0)
        self._append_local_x_getter_expression(x=x)
        return x

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_local_x_getter_expression(self, *, x: Number) -> None:
        """
        Append local_x getter property expression.

        Parameters
        ----------
        x : Number
            Target x-coordinate value.
        """
        from apysc._expression import expression_data_util

        stage_x: Number = self.stage_x
        this: _Target = self.this
        expression: str = (
            f"{x.variable_name} = {stage_x.variable_name} - "
            f"get_total_x({this.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)

    @property
    @add_debug_info_setting(module_name=__name__)
    def local_y(self) -> Number:
        """
        Get the local y-coordinate of the event listening instance.
        For example, this value becomes y-coordinate from Sprite's
        top-end position by clicking a Sprite instance.

        Returns
        -------
        y : Number
            y-coordinate.

        References
        ----------
        - Common mouse event interfaces
            - https://simon-ritchie.github.io/apysc/en/mouse_event_basic.html

        Examples
        --------
        >>> import apysc as ap
        >>> def on_mousedown(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
        ...     local_y: ap.Number = e.local_y
        ...     # Do something here with the coordinate.
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> _ = rectangle.mousedown(on_mousedown)
        """
        y: Number = Number(0)
        self._append_local_y_getter_expression(y=y)
        return y

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_local_y_getter_expression(self, *, y: Number) -> None:
        """
        Append local_y getter property expression.

        Parameters
        ----------
        y : Number
            Target y-coordinate value.
        """
        from apysc._expression import expression_data_util

        stage_y: Number = self.stage_y
        this: _Target = self.this
        expression: str = (
            f"{y.variable_name} = {stage_y.variable_name} - "
            f"get_total_y({this.variable_name});"
        )
        expression_data_util.append_js_expression(expression=expression)
