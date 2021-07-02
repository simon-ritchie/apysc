from typing import Any, Dict
from apysc import Timer, Event, Number, Int
from tests.testing_helper import assert_attrs
from apysc._expression import var_names


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
        pass

    def test___init__(self) -> None:
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
