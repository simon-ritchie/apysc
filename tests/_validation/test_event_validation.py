import apysc as ap
from apysc._testing import testing_helper
from apysc._validation import event_validation


def test_validate_event() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=event_validation.validate_event,
        match="\nTest error!",
        e=100,
        additional_err_msg="Test error!",
    )

    int_1: ap.Int = ap.Int(10)
    e: ap.Event = ap.Event(this=int_1)
    e = event_validation.validate_event(e=e)
    assert isinstance(e, ap.Event)


def test_validate_event_type() -> None:
    testing_helper.assert_raises(
        expected_error_class=ValueError,
        callable_=event_validation.validate_event_type,
        mouse_event_type=100,
    )

    mouse_event_type: ap.MouseEventType = event_validation.validate_event_type(
        mouse_event_type=ap.MouseEventType.CLICK
    )
    assert isinstance(mouse_event_type, ap.MouseEventType)
