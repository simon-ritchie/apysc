import re
from typing import Any
from typing import Callable
from typing import Dict
from typing import Match
from typing import Optional

import apysc as ap
from apysc._event.custom_event_type import CustomEventType
from apysc._event.handler import HandlerData
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestTimer:
    def on_timer(self, e: ap.TimerEvent, options: Dict[str, Any]) -> None:
        """
        The handler for the timer event.

        Parameters
        ----------
        e : TimerEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    def on_timer_complete(self, e: ap.TimerEvent, options: Dict[str, Any]) -> None:
        """
        Ther handler for the timer complete event.

        Parameters
        ----------
        e : TimerEvent
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @apply_test_settings()
    def test___init__(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3, repeat_count=10)
        assert_attrs(
            expected_attrs={
                "_delay": ap.Number(33.3),
                "_repeat_count": ap.Int(10),
            },
            any_obj=timer,
        )
        assert callable(timer._handler)
        assert callable(timer._handler_data.handler)
        assert timer._handler_data.options == {}
        assert timer.variable_name.startswith(f"{var_names.TIMER}_")
        assert "on_timer" in timer._handler_name
        assert isinstance(timer._delay, ap.Number)
        assert isinstance(timer._repeat_count, ap.Int)

        expression = expression_data_util.get_current_expression()
        assert f"var {timer.variable_name};" in expression

    @apply_test_settings()
    def test_delay(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        assert timer.delay == 33.3
        assert isinstance(timer.delay, ap.Number)
        assert timer._delay.variable_name != timer.delay.variable_name

    @apply_test_settings()
    def test_repeat_count(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3, repeat_count=3)
        assert timer.repeat_count == 3
        assert isinstance(timer.repeat_count, ap.Int)
        assert timer._repeat_count.variable_name != timer.repeat_count.variable_name

    @apply_test_settings()
    def test_running(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        assert not timer.running
        assert isinstance(timer.running, ap.Boolean)
        assert timer._running.variable_name != timer.running.variable_name

    @apply_test_settings()
    def test_start(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        timer.start()
        assert timer.running
        expression: str = expression_data_util.get_current_expression()
        pattern: str = (
            rf"if \(_\.isUndefined\({timer.variable_name}\)\) {{"
            rf"\n  {timer.variable_name} = setInterval\("
            rf"{timer._handler_name}, {var_names.NUMBER}_.+?\);"
            r"\n}"
        )
        match: Optional[Match] = re.search(
            pattern=pattern,
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        expression = expression_data_util.get_current_event_handler_scope_expression()
        match = re.search(
            pattern=(r"function .*on_timer.*\("),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        ap.Stage()
        timer = ap.Timer(handler=self.on_timer, delay=33.3)
        table_name: str = (
            expression_data_util.TableName.CIRCULAR_CALLING_HANDLER_NAME.value
        )
        query: str = (
            f"INSERT INTO {table_name}"
            "(handler_name, prev_handler_name, prev_variable_name) "
            f"VALUES('{timer._handler_name}', 'test_prev_handler', "
            f"'test_prev_variable');"
        )
        expression_data_util.exec_query(sql=query)
        timer.start()
        expression = expression_data_util.get_current_expression()
        assert f"_.isUndefined({timer.variable_name})" not in expression
        assert "_.isUndefined(test_prev_variable)" in expression
        assert f"setInterval({timer._handler_name}" not in expression
        assert "test_prev_variable = setInterval(test_prev_handler" in expression

    @apply_test_settings()
    def test_current_count(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        assert timer.current_count == 0
        assert isinstance(timer.current_count, ap.Int)
        assert timer._current_count.variable_name != timer.current_count.variable_name

    @apply_test_settings()
    def test__wrap_handler(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        wrapped: Callable[[ap.TimerEvent, Any], None] = timer._wrap_handler(
            handler=self.on_timer
        )
        e: ap.TimerEvent = ap.TimerEvent(this=timer)
        wrapped(e, {})
        assert timer.current_count == 0

    @apply_test_settings()
    def test_stop(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        timer.start()
        timer.stop()
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"if (!_.isUndefined({timer.variable_name})) {{"
            f"\n  clearInterval({timer.variable_name});"
            f"\n  {timer.variable_name} = undefined;"
            "\n}"
        )
        assert expected in expression
        assert not timer.running

    @apply_test_settings()
    def test__get_stop_expression(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        expression: str = timer._get_stop_expression(indent_num=1)
        expected: str = (
            f"  if (!_.isUndefined({timer.variable_name})) {{"
            f"\n    clearInterval({timer.variable_name});"
            f"\n    {timer.variable_name} = undefined;"
            "\n  }"
        )
        assert expected in expression

    @apply_test_settings()
    def test__append_count_branch_expression(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3, repeat_count=5)
        timer.start()
        expression: str = (
            expression_data_util.get_current_event_handler_scope_expression()
        )
        match: Optional[Match] = re.search(
            pattern=(
                rf"  if \({var_names.INT}_.+? !== 0 && "
                rf"{var_names.INT}_.+? === {var_names.INT}_.+?\) {{"
                r"\n    if \(.*?"
                r"\n  }"
            ),
            string=expression,
            flags=re.MULTILINE | re.DOTALL,
        )
        assert match is not None

        event_type: str = CustomEventType.TIMER_COMPLETE.value
        match = re.search(
            pattern=(
                rf"\$\({timer.blank_object_variable_name}\)"
                rf'\.trigger\("{event_type}"\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        assert timer._current_count == 0
        expected: str = f"{timer._current_count.variable_name} = 0;"
        assert expected in expression

        expected = f"$({timer.blank_object_variable_name}).off(" f'"{event_type}");'
        assert expected in expression

    @apply_test_settings()
    def test__convert_delay_to_number(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        assert timer.delay == 33.3
        assert isinstance(timer.delay, ap.Number)

        timer = ap.Timer(handler=self.on_timer, delay=ap.Number(33.3))
        assert timer.delay == 33.3
        assert isinstance(timer.delay, ap.Number)

        timer = ap.Timer(handler=self.on_timer, delay=ap.FPS.FPS_60)
        assert timer.delay == 16.6666667
        assert isinstance(timer.delay, ap.Number)

    @apply_test_settings()
    def test_timer_complete(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        name: str = timer.timer_complete(handler=self.on_timer_complete)
        assert isinstance(
            timer._custom_event_handlers[CustomEventType.TIMER_COMPLETE.value][name],
            HandlerData,
        )

    @apply_test_settings()
    def test_reset(self) -> None:
        timer: ap.Timer = ap.Timer(handler=self.on_timer, delay=33.3)
        timer.start()
        timer._current_count._value = 10
        timer.reset()
        assert timer.current_count == 0
        assert not timer.running
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{timer._current_count.variable_name} = 0;"
        assert expected in expression
