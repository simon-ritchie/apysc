from apysc import Event
from apysc import Int
from apysc import MouseEventType
from apysc._validation import event_validation
from tests import testing_helper


def test_validate_event() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=event_validation.validate_event,
        kwargs={'e': 100})

    int_1: Int = Int(10)
    e: Event = Event(this=int_1)
    e = event_validation.validate_event(e=e)
    assert isinstance(e, Event)


def test_validate_event_type() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        func_or_method=event_validation.validate_event_type,
        kwargs={'mouse_event_type': 100})

    mouse_event_type: MouseEventType = event_validation.validate_event_type(
        mouse_event_type=MouseEventType.CLICK)
    assert isinstance(mouse_event_type, MouseEventType)
