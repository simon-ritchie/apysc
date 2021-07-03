"""Class implementation for the timer.
"""

from typing import Any, Dict, Optional, Union
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._event.handler import Handler
from apysc import Int, Number
from apysc._type.number_value_interface import NumberValueInterface
from apysc._event.handler import HandlerData


class Timer(VariableNameInterface):

    _handler: Handler
    _delay: Number
    _repeat_count: Int
    _handler_data: HandlerData
    _handler_name: str

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
            Max count of a handler's call. If the handler's calling
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
        self._handler = handler
        if not isinstance(delay, Number):
            delay = Number(delay)
        self._delay = delay
        if not isinstance(repeat_count, Int):
            repeat_count = Int(repeat_count)
        self._repeat_count = repeat_count
        self.variable_name = expression_variables_util.get_next_variable_name(
            type_name=var_names.TIMER)
        if options is None:
            options = {}
        self._handler_data = {
            'handler': self._handler,
            'options': options,
        }
        self._handler_name = get_handler_name(handler=handler, instance=self)
        e: TimerEvent = TimerEvent(this=self)
        append_handler_expression(
            handler_data=self._handler_data, handler_name=self._handler_name,
            e=e)
