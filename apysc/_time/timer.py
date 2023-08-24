"""Class implementation for the timer.
"""

from typing import TYPE_CHECKING
from typing import Any
from typing import Callable
from typing import Optional
from typing import TypeVar
from typing import Union

from typing_extensions import final

from apysc._event.custom_event_mixin import CustomEventMixIn
from apysc._event.handler import HandlerData
from apysc._html.debug_mode import add_debug_info_setting
from apysc._time.fps import FPS
from apysc._type.boolean import Boolean
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.number_value_mixin import NumberValueMixIn
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._validation import arg_validation_decos

if TYPE_CHECKING:
    from apysc._event.timer_event import TimerEvent

_ConstructorOptions = TypeVar("_ConstructorOptions")
_TimerCompleteOptions = TypeVar("_TimerCompleteOptions")
_Handler = Callable[["TimerEvent", _ConstructorOptions], None]


class Timer(VariableNameMixIn, CustomEventMixIn["TimerEvent"]):
    """
    Timer class to handle function calling at regular intervals.

    References
    ----------
    - Timer
        - https://simon-ritchie.github.io/apysc/en/timer.html
    - TimerEvent class
        - https://simon-ritchie.github.io/apysc/en/timer_event.html
    - Timer class delay setting
        - https://simon-ritchie.github.io/apysc/en/timer_delay.html
    - FPS enum
        - https://simon-ritchie.github.io/apysc/en/fps.html
    - Timer class repeat_count setting
        - https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html

    Examples
    --------
    >>> from typing_extensions import TypedDict
    >>> import apysc as ap
    >>> _ = ap.Stage()
    >>> class RectOptions(TypedDict):
    ...     rectangle: ap.Rectangle
    ...
    >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
    ...     rectangle: ap.Rectangle = options["rectangle"]
    ...     rectangle.x += 1
    >>> def on_timer_complete(e: ap.TimerEvent, options: dict) -> None:
    ...     ap.trace("Timer completed!")
    >>> stage: ap.Stage = ap.Stage()
    >>> sprite: ap.Sprite = ap.Sprite()
    >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
    >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    ...     x=50, y=50, width=50, height=50
    ... )
    >>> options: RectOptions = {"rectangle": rectangle}
    >>> timer: ap.Timer = ap.Timer(
    ...     on_timer, delay=ap.FPS.FPS_60, repeat_count=50, options=options
    ... )
    >>> _ = timer.timer_complete(on_timer_complete)
    >>> timer.start()
    """

    _delay: Number
    _repeat_count: Int
    _current_count: Int
    _handler_data: HandlerData["TimerEvent"]
    _handler_name: str
    _running: Boolean

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @arg_validation_decos.is_integer(arg_position_index=3, optional=False)
    @arg_validation_decos.num_is_gte_zero(arg_position_index=3, optional=False)
    @arg_validation_decos.handler_options_type(arg_position_index=4)
    @add_debug_info_setting(module_name=__name__)
    def __init__(
        self,
        handler: _Handler[_ConstructorOptions],
        *,
        delay: Union[int, float, NumberValueMixIn, FPS],
        repeat_count: Union[int, Int] = 0,
        options: Optional[_ConstructorOptions] = None,
    ) -> None:
        """
        Timer class to handle function calling at regular intervals.

        Parameters
        ----------
        handler : _Handler
            A handler would be called at regular intervals.
        delay : Int or int or Number or float or FPS
            A delay between each `Handler` calling in a millisecond
            or FPS value. If an `FPS` value is specified, this
            value becomes a millisecond calculated with that
            FPS value (e.g., if the `FPS_60` value is specified,
            then `delay` becomes 16.6666667).
        repeat_count : Int or int
            Max count of a `Handler`'s calling. A timer stops
            if the `Handler`'s calling count has reached this value.
            If 0 is specified, then a timer loops forever.
        options : dict or None, default None
            Optional arguments dictionary to pass a `Handler` callable.

        References
        ----------
        - Timer
            - https://simon-ritchie.github.io/apysc/en/timer.html
        - TimerEvent class
            - https://simon-ritchie.github.io/apysc/en/timer_event.html
        - Timer class delay setting
            - https://simon-ritchie.github.io/apysc/en/timer_delay.html
        - FPS enum
            - https://simon-ritchie.github.io/apysc/en/fps.html
        - Timer class repeat_count setting
            - https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html
        - About the handler options' type
            - https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.x += 1
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> options: RectOptions = {"rectangle": rectangle}
        >>> _ = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options).start()
        """
        from apysc._event.handler import get_handler_name
        from apysc._expression import expression_data_util
        from apysc._expression import expression_variables_util
        from apysc._expression import var_names
        from apysc._expression.event_handler_scope import TemporaryNotHandlerScope
        from apysc._validation import number_validation

        with TemporaryNotHandlerScope():
            self.variable_name = expression_variables_util.get_next_variable_name(
                type_name=var_names.TIMER
            )
            self._handler_name = get_handler_name(handler=handler, instance=self)
            handler = self._wrap_handler(handler=handler)
            self._handler: _Handler[_ConstructorOptions] = handler
            delay_: Number = self._convert_delay_to_number(delay=delay)
            number_validation.validate_num_is_gte_zero(num=delay_)
            self._delay = delay_
            if isinstance(repeat_count, Int):
                repeat_count_: Int = repeat_count
            else:
                repeat_count_ = Int(repeat_count)
            self._repeat_count = repeat_count_
            self._running = Boolean(False)
            self._current_count = Int(0)
            if options is None:
                options = {}  # type: ignore
            self._handler_data = HandlerData(
                handler=self._handler,
                options=options,
            )
            expression_data_util.append_js_expression(
                expression=f"var {self.variable_name};"
            )

    @final
    @add_debug_info_setting(module_name=__name__)
    def _convert_delay_to_number(
        self, *, delay: Union[int, float, NumberValueMixIn, FPS]
    ) -> Number:
        """
        Convert each type of delay value to a `Number` value.

        Parameters
        ----------
        delay : int or float or Int or Number or FPS
            A delay between each handler's calling in milliseconds
            or FPS value.

        Returns
        -------
        delay_ : Number
            Converted delay value.
        """
        from apysc._time.fps import FPSDefinition

        if isinstance(delay, FPS):
            fps_definition: FPSDefinition = delay.value
            delay = fps_definition.millisecond_interval
        if not isinstance(delay, Number):
            delay_: Number = Number(delay)
        else:
            delay_ = delay
        return delay_

    @property
    @add_debug_info_setting(module_name=__name__)
    def delay(self) -> Number:
        """
        Get a delay value.

        Returns
        -------
        delay : Number
            A delay value of each `Handler` calling in milliseconds.

        References
        ----------
        - Timer class delay setting
            - https://simon-ritchie.github.io/apysc/en/timer_delay.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
        ...     pass
        >>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)
        >>> timer.delay
        Number(33.3)
        """
        from apysc._type import value_util

        return value_util.get_copy(value=self._delay)

    @property
    @add_debug_info_setting(module_name=__name__)
    def repeat_count(self) -> Int:
        """
        Get a max count value of a handler's calling.

        Returns
        -------
        repeat_count : Int
            Max count of a handler's calling.
            If this value is 0, then a timer loop forever.

        References
        ----------
        - Timer class repeat_count setting
            - https://simon-ritchie.github.io/apysc/en/timer_repeat_count.html

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
        ...     pass
        >>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)
        >>> timer.repeat_count
        Int(50)
        """
        from apysc._type import value_util

        return value_util.get_copy(value=self._repeat_count)

    @property
    @add_debug_info_setting(module_name=__name__)
    def running(self) -> Boolean:
        """
        Get a boolean value whether this timer is running or not.

        Returns
        -------
        running : Boolean.
            A boolean value whether this timer is running or not.

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
        ...     pass
        >>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, repeat_count=50)
        >>> timer.running
        Boolean(False)

        >>> timer.start()
        >>> timer.running
        Boolean(True)
        """
        from apysc._type import value_util

        return value_util.get_copy(value=self._running)

    @property
    @add_debug_info_setting(module_name=__name__)
    def current_count(self) -> Int:
        """
        Get a current timer count.

        Returns
        -------
        current_count : Int
            A current timer count.

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
        ...     timer: ap.Timer = e.this
        ...     ap.trace(timer.current_count)
        >>> _ = ap.Timer(on_timer, delay=33.3, repeat_count=50).start()
        """
        from apysc._type import value_util

        return value_util.get_copy(value=self._current_count)

    @final
    @add_debug_info_setting(module_name=__name__)
    def start(self) -> None:
        """
        Start this timer.

        References
        ----------
        - Timer class start and stop interfaces
            - https://simon-ritchie.github.io/apysc/en/timer_start_and_stop.html  # noqa

        Examples
        --------
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
        ...     pass
        >>> _ = ap.Timer(on_timer, delay=33.3, repeat_count=50).start()
        """
        from apysc._event import handler_circular_calling_util
        from apysc._event.handler import append_handler_expression
        from apysc._event.timer_event import TimerEvent
        from apysc._expression import expression_data_util
        from apysc._type import value_util

        delay_val_str: str = value_util.get_value_str_for_expression(value=self._delay)
        is_handler_circular_calling: bool = (
            handler_circular_calling_util.is_handler_circular_calling(
                handler_name=self._handler_name
            )
        )
        if is_handler_circular_calling:
            handler_name: str = handler_circular_calling_util.get_prev_handler_name(
                handler_name=self._handler_name
            )
            variable_name: str = handler_circular_calling_util.get_prev_variable_name(
                handler_name=self._handler_name
            )
        else:
            handler_name = self._handler_name
            variable_name = self.variable_name
        expression: str = (
            f"\nif (_.isUndefined({variable_name})) {{"
            f"\n  {variable_name} = setInterval("
            f"{handler_name}, {delay_val_str});"
            "\n}"
        )
        expression_data_util.append_js_expression(expression=expression)

        e: TimerEvent = TimerEvent(this=self)
        append_handler_expression(
            handler_data=self._handler_data, handler_name=handler_name, e=e
        )
        self._running.value = True

    @final
    def _wrap_handler(
        self,
        *,
        handler: _Handler[_ConstructorOptions],
    ) -> _Handler[_ConstructorOptions]:
        """
        Wrap a handler to update a current count value when
        it is called.

        Parameters
        ----------
        handler : _Handler
            Target handler.

        Returns
        -------
        wrapped : _Handler
            A wrapped handler.
        """
        from apysc._event.timer_event import TimerEvent

        def wrapped(e: TimerEvent, options: Any) -> None:
            """
            Wrapped handler.

            Parameters
            ----------
            e : TimerEvent
                Event instance.
            options : dict
                Optional arguments dictionary.
            """
            e.this._current_count += 1
            e.this._current_count._value = 0
            handler(e, options)
            self._append_count_branch_expression()

        return wrapped

    @final
    @add_debug_info_setting(module_name=__name__)
    def _append_count_branch_expression(self) -> None:
        """
        Append the timer stopping expression by the counting.
        """
        from apysc._event.custom_event_type import CustomEventType
        from apysc._expression import expression_data_util
        from apysc._expression.indent_num import Indent
        from apysc._type import value_util

        current_count_val_str: str = value_util.get_value_str_for_expression(
            value=self._current_count
        )
        repeat_count_val_str: str = value_util.get_value_str_for_expression(
            value=self._repeat_count
        )
        expression: str = (
            f"if ({repeat_count_val_str} !== 0 "
            f"&& {current_count_val_str} === {repeat_count_val_str}) {{"
            f"\n{self._get_stop_expression(indent_num=1)}"
        )
        expression_data_util.append_js_expression(expression=expression)
        with Indent():
            self._running.value = False
            self.trigger_custom_event(custom_event_type=CustomEventType.TIMER_COMPLETE)
            self.unbind_custom_event_all(
                custom_event_type=CustomEventType.TIMER_COMPLETE
            )
            self._current_count.value = 0
        expression = "\n}"
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def stop(self) -> None:
        """
        Stop this timer.

        References
        ----------
        - Timer class start and stop interfaces
            - https://simon-ritchie.github.io/apysc/en/timer_start_and_stop.html  # noqa

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.x += 1
        ...     with ap.If(rectangle.x > 100):
        ...         timer: ap.Timer = e.this
        ...         timer.stop()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> options: RectOptions = {"rectangle": rectangle}
        >>> _ = ap.Timer(on_timer, delay=33.3, options=options).start()
        """
        from apysc._expression import expression_data_util

        self._running.value = False
        expression: str = self._get_stop_expression(indent_num=0)
        expression_data_util.append_js_expression(expression=expression)

    @final
    @add_debug_info_setting(module_name=__name__)
    def _get_stop_expression(self, *, indent_num: int) -> str:
        """
        Get a stop interface expression string.

        Parameters
        ----------
        indent_num : int
            Indentation number to append.

        Returns
        -------
        expression : str
            Stop interface expression string.
        """
        from apysc._string import indent_util

        expression: str = (
            f"if (!_.isUndefined({self.variable_name})) {{"
            f"\n  clearInterval({self.variable_name});"
            f"\n  {self.variable_name} = undefined;"
            "\n}"
        )
        expression = indent_util.append_spaces_to_expression(
            expression=expression, indent_num=indent_num
        )
        return expression

    @final
    @add_debug_info_setting(module_name=__name__)
    def reset(self) -> None:
        """
        Reset the timer count and stop this timer.

        References
        ----------
        - Timer class reset interface
            - https://simon-ritchie.github.io/apysc/en/timer_reset.html

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.x += 1
        ...     with ap.If(rectangle.x > 100):
        ...         timer: ap.Timer = e.this
        ...         timer.reset()
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> options: RectOptions = {"rectangle": rectangle}
        >>> _ = ap.Timer(on_timer, delay=33.3, options=options).start()
        """
        self.stop()
        self._current_count.value = 0

    @final
    @arg_validation_decos.handler_args_num(arg_position_index=1)
    @arg_validation_decos.handler_options_type(arg_position_index=2)
    @add_debug_info_setting(module_name=__name__)
    def timer_complete(
        self,
        handler: _Handler[_TimerCompleteOptions],
        *,
        options: Optional[_TimerCompleteOptions] = None,
    ) -> str:
        """
        Add a timer complete event listener setting.

        Parameters
        ----------
        handler : _Handler
            A callable that a timer calls when complete.
        options : dict or None, default None
            Optional arguments dictionary to be passed to a handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Timer class timer_complete interface
            - https://simon-ritchie.github.io/apysc/en/timer_complete.html
        - About the handler options' type
            - https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html  # noqa

        Examples
        --------
        >>> from typing_extensions import TypedDict
        >>> import apysc as ap
        >>> _ = ap.Stage()
        >>> class RectOptions(TypedDict):
        ...     rectangle: ap.Rectangle
        ...
        >>> def on_timer(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     rectangle: ap.Rectangle = options["rectangle"]
        ...     rectangle.x += 1
        >>> def on_timer_complete(e: ap.TimerEvent, options: RectOptions) -> None:
        ...     ap.trace("Timer completed!")
        >>> stage: ap.Stage = ap.Stage()
        >>> sprite: ap.Sprite = ap.Sprite()
        >>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
        >>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
        ...     x=50, y=50, width=50, height=50
        ... )
        >>> options: RectOptions = {"rectangle": rectangle}
        >>> timer: ap.Timer = ap.Timer(on_timer, delay=33.3, options=options)
        >>> _ = timer.timer_complete(on_timer_complete)
        >>> timer.start()
        """
        from apysc._event.custom_event_type import CustomEventType
        from apysc._event.timer_event import TimerEvent

        e: TimerEvent = TimerEvent(this=self)
        name: str = self.bind_custom_event(
            custom_event_type=CustomEventType.TIMER_COMPLETE,
            handler=handler,
            e=e,
            options=options,
        )
        return name
