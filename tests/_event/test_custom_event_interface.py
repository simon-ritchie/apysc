from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.custom_event_type import CustomEventType


class TestCustomEventInterface:

    def test__get_custom_event_type_str(self) -> None:
        interface: CustomEventInterface = CustomEventInterface()
        custom_event_type_str: str = interface._get_custom_event_type_str(
            custom_event_type='test_custom_event')
        assert custom_event_type_str == 'test_custom_event'

        custom_event_type_str = interface._get_custom_event_type_str(
            custom_event_type=CustomEventType.TIMER_COMPLETE)
        assert custom_event_type_str == CustomEventType.TIMER_COMPLETE.value
        assert isinstance(custom_event_type_str, str)
