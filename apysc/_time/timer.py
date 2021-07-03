"""Class implementation for the timer.
"""

from typing import Any, Dict, Optional, Union
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._event.handler import Handler
from apysc import Int, Number, Boolean
from apysc._type.number_value_interface import NumberValueInterface
from apysc._event.handler import HandlerData


class Timer(VariableNameInterface):

    _handler: Handler
    _delay: Number
    _repeat_count: Int
    _current_count: Int
    _handler_data: HandlerData
    _handler_name: str
    _running: Boolean

    def __init__(
            self,
            handler: Handler,
            delay: Union[int, float, NumberValueInterface],
            repeat_count: Union[int, Int] = 0,
            options: Optional[Dict[str, Any]] = None) -> None:
        """
        Timer class to handle function calling at regular intervals.

        Parameters
        ----------
        handler : Handler
            A handler would be called at regular intervals.
        delay : int or float or Int or Number
            A delay between each handler's calling in milisecond.
        repeat_count : int or Int
            Max count of a handler's calling. If the handler's calling
            count has reached this value, then a timer will stop.
            If 0 is specified, then a timer will loop forever.
        options : dict or None, default None
            Optional arguments dictionary to pass the the handler.
        """
        from apysc._expression import var_names
        from apysc._expression import expression_variables_util
        from apysc._event.handler import get_handler_name
        from apysc._event.handler import append_handler_expression
        from apysc import TimerEvent
        from apysc._expression.event_handler_scope import \
            TemporaryNotHandlerScope
        from apysc._validation import number_validation
        with TemporaryNotHandlerScope():
            self.variable_name = \
                expression_variables_util.get_next_variable_name(
                type_name=var_names.TIMER)
            self._handler_name = get_handler_name(
                handler=handler, instance=self)
            handler = self._wrap_handler(handler=handler)
            self._handler = handler
            if not isinstance(delay, Number):
                delay = Number(delay)
            number_validation.validate_num_is_gte_zero(num=delay)
            self._delay = delay
            if not isinstance(repeat_count, Int):
                repeat_count = Int(repeat_count)
            number_validation.validate_num_is_gte_zero(num=repeat_count)
            self._repeat_count = repeat_count
            self._running = Boolean(False)
            self._current_count = Int(0)
            if options is None:
                options = {}
            self._handler_data = {
                'handler': self._handler,
                'options': options,
            }
            e: TimerEvent = TimerEvent(this=self)
            append_handler_expression(
                handler_data=self._handler_data,
                handler_name=self._handler_name,
                e=e)

    @property
    def delay(self) -> Number:
        """
        Get a delay value.

        Returns
        -------
        delay : Number
            A delay value of each handler's calling in milisecond.
        """
        from apysc._type import value_util
        return value_util.get_copy(value=self._delay)

    @property
    def repeat_count(self) -> Int:
        """
        Get a max count value of a handler's calling.

        Returns
        -------
        repeat_count : Int
            Max count of a handler's calling. If 0 is set, then a
            timer will loop forever.
        """
        from apysc._type import value_util
        return value_util.get_copy(value=self._repeat_count)

    @property
    def running(self) -> Boolean:
        """
        Get a boolean value whether this timer is running or not.

        Returns
        -------
        running : Boolean.
            A boolean value whether this timer is running or not.
        """
        from apysc._type import value_util
        return value_util.get_copy(value=self._running)

    @property
    def current_count(self) -> Int:
        """
        Get a current timer count.

        Returns
        -------
        current_count : Int
            A current timer count.
        """
        from apysc._type import value_util
        return value_util.get_copy(value=self._current_count)

    def start(self) -> None:
        """
        Start this timer.
        """
        from apysc._expression import expression_file_util
        from apysc._type import value_util
        self._running.value = True
        delay_val_str: str = value_util.get_value_str_for_expression(
            value=self._delay)
        expression: str = (
            f'if (_.isUndefined({self.variable_name})) {{'
            f'\n  var {self.variable_name} = setInterval('
            f'{self._handler_name}, {delay_val_str});'
            '\n}'
        )
        expression_file_util.append_js_expression(expression=expression)

    def _wrap_handler(self, handler: Handler) -> Handler:
        """
        Wrap a handler to update a current count value when
        it is called.

        Parameters
        ----------
        handler : Handler
            Target handler.

        Returns
        -------
        wrapped : Handler
            Wrapped handler.
        """
        from apysc import TimerEvent

        def wrapped(e: TimerEvent, options: Dict[str, Any]) -> None:
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
            handler.__call__(e=e, options=options)

        return wrapped

    def stop(self) -> None:
        """
        Stop this timer.
        """
        self._running.value = False
        self._append_stop_expression()

    def _append_stop_expression(self) -> None:
        """
        Append the timer stop expression to the file.
        """
        from apysc._expression import expression_file_util
        expression: str = (
            f'if (!_.isUndefined({self.variable_name})) {{'
            f'\n  clearInterval({self.variable_name});'
            f'\n  {self.variable_name} = undefined;'
            '\n}'
        )
        expression_file_util.append_js_expression(expression=expression)
