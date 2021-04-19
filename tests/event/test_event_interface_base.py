from apysc.event.event_interface_base import EventInterfaceBase
from tests import testing_helper


class TestEventInterfaceBase:

    def test_validate_self_is_variable_name_interface(self) -> None:
        interface_1: EventInterfaceBase = EventInterfaceBase()
        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=interface_1.
            validate_self_is_variable_name_interface,
            match=interface_1.VARIABLE_NAME_INTERFACE_TYPE_ERR_MSG)
