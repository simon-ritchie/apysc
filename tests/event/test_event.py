from random import randint

from retrying import retry

from apysc import Event, Int
from apysc.expression import var_names
from tests import testing_helper


class TestEvent:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test___init__(self) -> None:
        int_1: Int = Int(10)
        event: Event = Event(this=int_1)
        testing_helper.assert_attrs(
            expected_attrs={
                '_this': int_1,
            },
            any_obj=event)
        assert event.variable_name.startswith(
            f'{var_names.EVENT}_'
        )
