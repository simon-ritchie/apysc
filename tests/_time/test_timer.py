import re
from random import randint
from typing import Any
from typing import Dict
from typing import Match
from typing import Optional

from retrying import retry

from apysc import FPS
from apysc import Boolean
from apysc import Int
from apysc import Number
from apysc import Timer
from apysc import TimerEvent
from apysc._event.custom_event_type import CustomEventType
from apysc._event.handler import Handler
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestTimer:

    def on_timer(self, e: TimerEvent, options: Dict[str, Any]) -> None:
        """
        The handler for the timer event.

        Parameters
        ----------
        e : TimerEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_timer_complete(
            self, e: TimerEvent, options: Dict[str, Any]) -> None:
        """
        Ther handler for the timer complete event.

        Parameters
        ----------
        e : TimerEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        expression_file_util.empty_expression_dir()
        timer: Timer = Timer(
            handler=self.on_timer,
            delay=33.3,
            repeat_count=10)
        assert_attrs(
            expected_attrs={
                '_delay': Number(33.3),
                '_repeat_count': Int(10),
            },
            any_obj=timer)
        assert callable(timer._handler)
        assert callable(timer._handler_data['handler'])
        assert timer._handler_data['options'] == {}
        assert timer.variable_name.startswith(f'{var_names.TIMER}_')
        assert 'on_timer' in timer._handler_name
        assert isinstance(timer._delay, Number)
        assert isinstance(timer._repeat_count, Int)

        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r'function .*on_timer.*\('
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_delay(self) -> None:
        timer: Timer = Timer(
            handler=self.on_timer,
            delay=33.3)
        assert timer.delay == 33.3
        assert isinstance(timer.delay, Number)
        assert timer._delay.variable_name != timer.delay.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_repeat_count(self) -> None:
        timer: Timer = Timer(
            handler=self.on_timer,
            delay=33.3, repeat_count=3)
        assert timer.repeat_count == 3
        assert isinstance(timer.repeat_count, Int)
        assert timer._repeat_count.variable_name \
            != timer.repeat_count.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_running(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33.3)
        assert not timer.running
        assert isinstance(timer.running, Boolean)
        assert timer._running.variable_name != timer.running.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_start(self) -> None:
        expression_file_util.empty_expression_dir()
        timer: Timer = Timer(handler=self.on_timer, delay=33.3)
        timer.start()
        assert timer.running
        expression: str = expression_file_util.get_current_expression()
        pattern: str = (
            rf'if \(_\.isUndefined\({timer.variable_name}\)\) {{'
            rf'\n  var {timer.variable_name} = setInterval\('
            rf'{timer._handler_name}, {var_names.NUMBER}_.+?\);'
            r'\n}'
        )
        match: Optional[Match] = re.search(
            pattern=pattern,
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_current_count(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33.3)
        assert timer.current_count == 0
        assert isinstance(timer.current_count, Int)
        assert timer._current_count.variable_name \
            != timer.current_count.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__wrap_handler(self) -> None:
        timer: Timer = Timer(handler=self.on_timer, delay=33.3)
        wrapped: Handler = timer._wrap_handler(handler=self.on_timer)
        e: TimerEvent = TimerEvent(this=timer)
        wrapped.__call__(e=e, options={})
        assert timer.current_count == 0

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_stop(self) -> None:
        expression_file_util.empty_expression_dir()
        timer: Timer = Timer(handler=self.on_timer, delay=33.3)
        timer.start()
        timer.stop()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'if (!_.isUndefined({timer.variable_name})) {{'
            f'\n  clearInterval({timer.variable_name});'
            f'\n  {timer.variable_name} = undefined;'
            '\n}'
        )
        assert expected in expression
        assert not timer.running

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_stop_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        timer: Timer = Timer(handler=self.on_timer, delay=33.3)
        expression: str = timer._get_stop_expression(indent_num=1)
        expected: str = (
            f'  if (!_.isUndefined({timer.variable_name})) {{'
            f'\n    clearInterval({timer.variable_name});'
            f'\n    {timer.variable_name} = undefined;'
            '\n  }'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_count_branch_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        timer: Timer = Timer(
            handler=self.on_timer, delay=33.3, repeat_count=5)
        timer.start()
        expression: str = \
            expression_file_util.get_current_event_handler_scope_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'  if \({var_names.INT}_.+? !== 0 && '
                rf'{var_names.INT}_.+? === {var_names.INT}_.+?\) {{'
                r'\n    if \(.*?'
                r'\n  }'
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL)
        assert match is not None

        event_type: str = CustomEventType.TIMER_COMPLETE.value
        match = re.search(
            pattern=(
                rf'\$\({timer.blank_object_variable_name}\)'
                rf'\.trigger\("{event_type}"\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__convert_delay_to_number(self) -> None:
        timer: Timer = Timer(
            handler=self.on_timer, delay=33.3)
        assert timer.delay == 33.3
        assert isinstance(timer.delay, Number)

        timer = Timer(
            handler=self.on_timer, delay=Number(33.3))
        assert timer.delay == 33.3
        assert isinstance(timer.delay, Number)

        timer = Timer(
            handler=self.on_timer, delay=FPS.FPS_60)
        assert timer.delay == 16.6666667
        assert isinstance(timer.delay, Number)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_timer_complete(self) -> None:
        expression_file_util.empty_expression_dir()
        timer: Timer = Timer(
            handler=self.on_timer, delay=33.3)
        name: str = timer.timer_complete(handler=self.on_timer_complete)
        assert isinstance(
            timer._custom_event_handlers[
                CustomEventType.TIMER_COMPLETE.value][name],
            dict)
