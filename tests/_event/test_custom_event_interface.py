from random import randint

from retrying import retry

from apysc._event.custom_event_interface import CustomEventInterface
from apysc._event.custom_event_type import CustomEventType


class TestCustomEventInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_custom_event_type_str(self) -> None:
        interface: CustomEventInterface = CustomEventInterface()
        custom_event_type_str: str = interface._get_custom_event_type_str(
            custom_event_type='test_custom_event')
        assert custom_event_type_str == 'test_custom_event'

        custom_event_type_str = interface._get_custom_event_type_str(
            custom_event_type=CustomEventType.TIMER_COMPLETE)
        assert custom_event_type_str == CustomEventType.TIMER_COMPLETE.value
        assert isinstance(custom_event_type_str, str)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_custom_event_handlers_if_not_initialized(
            self) -> None:
        interface: CustomEventInterface = CustomEventInterface()
        interface._initialize_custom_event_handlers_if_not_initialized(
            custom_event_type_str='test_custom_event')
        assert 'test_custom_event' in interface._custom_event_handlers
