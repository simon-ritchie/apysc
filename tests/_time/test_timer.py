from random import randint
import re

from retrying import retry

from typing import Any, Dict, Match, Optional
from apysc import Timer, Event, Number, Int
from tests.testing_helper import assert_attrs
from apysc._expression import var_names
from apysc._expression import expression_file_util


class TestTimer:

    def on_timer(self, e: Event, options: Dict[str, Any]) -> None:
        """
        The handler for the timer event.

        Parameters
        ----------
        e : Event
            Event instance.
        options : dict
            Optional arguments dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        expression_file_util.remove_expression_file()
        timer: Timer = Timer(
            handler=self.on_timer,
            delay=33.3,
            repeat_count=10)
        assert_attrs(
            expected_attrs={
                '_handler': self.on_timer,
                '_delay': Number(33.3),
                '_repeat_count': Int(10),
                '_handler_data': {
                    'handler': self.on_timer,
                    'options': {},
                },
            },
            any_obj=timer)
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
