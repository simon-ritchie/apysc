"""Class implementation for the timer.
"""

from typing import Any
from typing import Dict
from typing import Optional
from typing import Union

import apysc as ap
from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.handler import Handler
from apysc._event.handler import HandlerData
from apysc._time.fps import FPS
from apysc._type.number_value_interface import NumberValueInterface
from apysc._type.variable_name_interface import VariableNameInterface


class Timer(VariableNameInterface, CustomEventInterface):
    """
    Timer class to handle function calling at regular intervals.

    References
    ----------
    - Timer document
        - https://simon-ritchie.github.io/apysc/timer.html
    - TimerEvent class document
        - https://simon-ritchie.github.io/apysc/timer_event.html
    - Timer class delay setting document
        - https://simon-ritchie.github.io/apysc/timer_delay.html
    - FPS enum document
        - https://simon-ritchie.github.io/apysc/fps.html
    - Timer class repeat_count setting
        - https://simon-ritchie.github.io/apysc/timer_repeat_count.html
    """

    _handler: Handler
    _delay: ap.Number
    _repeat_count: ap.Int
    _current_count: ap.Int
    _handler_data: HandlerData
    _handler_name: str
    _running: ap.Boolean

    def __init__(
            self,
            handler: Handler,
            delay: Union[int, float, NumberValueInterface, FPS],
            repeat_count: Union[int, ap.Int] = 0,
            options: Optional[Dict[str, Any]] = None) -> None:
        """
        Timer class to handle function calling at regular intervals.

        Parameters
        ----------
        handler : Handler
            A handler would be called at regular intervals.
        delay : int or float or Int or Number or FPS
            A delay between each handler's calling in milisecond
            or FPS value.
            If `FPS` value is specified, then this value will be
            a milisecond calculated with that FPS value (e.g., if
            the `FPS_60` value is specified, then `delay` will be
            16.6666667).
        repeat_count : int or Int
            Max count of a handler's calling. If the handler's calling
            count has reached this value, then a timer will stop.
            If 0 is specified, then a timer will loop forever.
        options : dict or None, default None
            Optional arguments dictionary to pass the the handler.

        References
        ----------
        - Timer document
            - https://simon-ritchie.github.io/apysc/timer.html
        - TimerEvent class document
            - https://simon-ritchie.github.io/apysc/timer_event.html
        - Timer class delay setting document
            - https://simon-ritchie.github.io/apysc/timer_delay.html
        - FPS enum document
            - https://simon-ritchie.github.io/apysc/fps.html
        - Timer class repeat_count setting
            - https://simon-ritchie.github.io/apysc/timer_repeat_count.html
        """
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._event.handler import append_handler_expression
            from apysc._event.handler import get_handler_name
            from apysc._expression import expression_variables_util
            from apysc._expression import var_names
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
                delay = self._convert_delay_to_number(delay=delay)
                number_validation.validate_num_is_gte_zero(num=delay)
                self._delay = delay
                if not isinstance(repeat_count, ap.Int):
                    repeat_count = ap.Int(repeat_count)
                number_validation.validate_num_is_gte_zero(num=repeat_count)
                self._repeat_count = repeat_count
                self._running = ap.Boolean(False)
                self._current_count = ap.Int(0)
                if options is None:
                    options = {}
                self._handler_data = {
                    'handler': self._handler,
                    'options': options,
                }
                e: ap.TimerEvent = ap.TimerEvent(this=self)
                append_handler_expression(
                    handler_data=self._handler_data,
                    handler_name=self._handler_name,
                    e=e)
                ap.append_js_expression(
                    expression=f'var {self.variable_name};')

    def _convert_delay_to_number(
            self,
            delay: Union[int, float, NumberValueInterface, FPS]) -> ap.Number:
        """
        Convert each type of delay value to a `Number` value.

        Parameters
        ----------
        delay : int or float or Int or Number or FPS
            A delay between each handler's calling in milisecond
            or FPS value.

        Returns
        -------
        delay : Number
            Converted delay value.
        """
        with ap.DebugInfo(
                callable_=self._convert_delay_to_number, locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._time.fps import FPSDefinition
            if isinstance(delay, FPS):
                fps_definition: FPSDefinition = delay.value
                delay = fps_definition.milisecond_intervals
            if not isinstance(delay, ap.Number):
                delay = ap.Number(delay)
            return delay

    @property
    def delay(self) -> ap.Number:
        """
        Get a delay value.

        Returns
        -------
        delay : Number
            A delay value of each handler's calling in milisecond.

        References
        ----------
        - Timer class delay setting document
            - https://simon-ritchie.github.io/apysc/timer_delay.html
        """
        with ap.DebugInfo(
                callable_='delay', locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._type import value_util
            return value_util.get_copy(value=self._delay)

    @property
    def repeat_count(self) -> ap.Int:
        """
        Get a max count value of a handler's calling.

        Returns
        -------
        repeat_count : Int
            Max count of a handler's calling. If 0 is set, then a
            timer will loop forever.

        References
        ----------
        - Timer class repeat_count setting
            - https://simon-ritchie.github.io/apysc/timer_repeat_count.html
        """
        with ap.DebugInfo(
                callable_='repeat_count', locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._type import value_util
            return value_util.get_copy(value=self._repeat_count)

    @property
    def running(self) -> ap.Boolean:
        """
        Get a boolean value whether this timer is running or not.

        Returns
        -------
        running : Boolean.
            A boolean value whether this timer is running or not.
        """
        with ap.DebugInfo(
                callable_='running', locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._type import value_util
            return value_util.get_copy(value=self._running)

    @property
    def current_count(self) -> ap.Int:
        """
        Get a current timer count.

        Returns
        -------
        current_count : Int
            A current timer count.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='current_count', locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._type import value_util
            return value_util.get_copy(value=self._current_count)

    def start(self) -> None:
        """
        Start this timer.

        References
        ----------
        - Timer class start and stop interfaces
            - https://simon-ritchie.github.io/apysc/timer_start_and_stop.html
        """
        with ap.DebugInfo(
                callable_=self.start, locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._expression import expression_file_util
            from apysc._type import value_util
            self._running.value = True
            delay_val_str: str = value_util.get_value_str_for_expression(
                value=self._delay)
            expression: str = (
                f'\nif (_.isUndefined({self.variable_name})) {{'
                f'\n  {self.variable_name} = setInterval('
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

        def wrapped(e: ap.TimerEvent, options: Dict[str, Any]) -> None:
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
            self._append_count_branch_expression()

        return wrapped

    def _append_count_branch_expression(self) -> None:
        """
        Append the timer stopping expression by the counting
        to the file.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self._append_count_branch_expression,
                locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._event.custom_event_type import CustomEventType
            from apysc._expression import expression_file_util
            from apysc._expression.indent_num import Indent
            from apysc._type import value_util
            current_count_val_str: str = value_util.\
                get_value_str_for_expression(value=self._current_count)
            repeat_count_val_str: str = value_util.\
                get_value_str_for_expression(value=self._repeat_count)
            expression: str = (
                f'if ({repeat_count_val_str} !== 0 '
                f'&& {current_count_val_str} === {repeat_count_val_str}) {{'
                f'\n{self._get_stop_expression(indent_num=1)}'
            )
            expression_file_util.append_js_expression(expression=expression)
            with Indent():
                self._running.value = False
                self.trigger_custom_event(
                    custom_event_type=CustomEventType.TIMER_COMPLETE)
            expression = '\n}'
            expression_file_util.append_js_expression(expression=expression)

    def stop(self) -> None:
        """
        Stop this timer.

        - Timer class start and stop interfaces
            - https://simon-ritchie.github.io/apysc/timer_start_and_stop.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.stop, locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._expression import expression_file_util
            self._running.value = False
            expression: str = self._get_stop_expression(indent_num=0)
            expression_file_util.append_js_expression(expression=expression)

    def _get_stop_expression(self, indent_num: int) -> str:
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
        with ap.DebugInfo(
                callable_=self._get_stop_expression, locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._string import indent_util
            expression: str = (
                f'if (!_.isUndefined({self.variable_name})) {{'
                f'\n  clearInterval({self.variable_name});'
                f'\n  {self.variable_name} = undefined;'
                '\n}'
            )
            expression = indent_util.append_spaces_to_expression(
                expression=expression, indent_num=indent_num)
            return expression

    def reset(self) -> None:
        """
        Reset the timer count and stop this timer.

        References
        ----------
        - Timer class reset interface document
            - https://simon-ritchie.github.io/apysc/timer_reset.html
        """
        with ap.DebugInfo(
                callable_=self.reset, locals_=locals(),
                module_name=__name__, class_=Timer):
            self.stop()
            self._current_count.value = 0

    def timer_complete(
            self, handler: Handler,
            options: Optional[Dict[str, Any]] = None) -> str:
        """
        Add a timer complete event listener setting.

        Parameters
        ----------
        handler : Handler
            A callable would be called when the timer is complete.
        options : dict or None, default None
            Optional arguments dictionary to be passed to handler.

        Returns
        -------
        name : str
            Handler's name.

        References
        ----------
        - Timer class timer_complete interface document
            - https://simon-ritchie.github.io/apysc/timer_complete.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.timer_complete, locals_=locals(),
                module_name=__name__, class_=Timer):
            from apysc._event.custom_event_type import CustomEventType
            e: ap.TimerEvent = ap.TimerEvent(this=self)
            name: str = self.bind_custom_event(
                custom_event_type=CustomEventType.TIMER_COMPLETE,
                handler=handler,
                e=e,
                options=options)
            return name
