"""Class implementation for the timer.
"""

from typing import Union
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._event.handler import Handler
from apysc import Int, Number
from apysc._type.number_value_interface import NumberValueInterface


class Timer(VariableNameInterface):

    _handler: Handler
    _delay: Number
    _repeat_count: Int

    def __init__(
            self,
            handler: Handler,
            delay: Union[int, float, NumberValueInterface],
            repeat_count: Union[int, Int] = 0) -> None:
        """
        Time class to handle function calling at regular intervals.

        Parameters
        ----------
        handler : Handler
            A handler would be called at regular intervals.
        """
        self._handler = handler
        if not isinstance(delay, Number):
            delay = Number(delay)
        self._delay = delay
        if not isinstance(repeat_count, Int):
            repeat_count = Int(repeat_count)
        self._repeat_count = repeat_count
