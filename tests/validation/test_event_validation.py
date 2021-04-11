from apysc import Event
from apysc import Int
from apysc.validation import event_validation
from tests import testing_helper


def test_validate_event() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=event_validation.validate_event,
        kwargs={'e': 100})

    int_1: Int = Int(10)
    e: Event = Event(this=int_1)
    event_validation.validate_event(e=e)
