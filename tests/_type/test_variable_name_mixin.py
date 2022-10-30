from random import randint

from retrying import retry

from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._type.variable_name_suffix_interface import VariableNameSuffixInterface


class _TestInterface(VariableNameMixIn, VariableNameSuffixInterface):
    pass


class TestVariableNameMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_variable_name(self) -> None:
        interface: _TestInterface = _TestInterface()
        assert interface.variable_name == ""
        interface.variable_name = "test_interface_1"
        assert interface.variable_name == "test_interface_1"
        assert interface._variable_name_history == ["test_interface_1"]

        interface.variable_name = "test_interface_2"
        assert interface.variable_name == "test_interface_2"
        assert interface._variable_name_history == [
            "test_interface_1",
            "test_interface_2",
        ]

        interface._variable_name_suffix = "test_instance"
        assert interface.variable_name == "test_interface_2__test_instance"

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_previous_variable_name(self) -> None:
        interface: VariableNameMixIn = VariableNameMixIn()
        previous_variable_name: str = interface._get_previous_variable_name()
        assert previous_variable_name == ""

        interface.variable_name = "test_interface_1"
        previous_variable_name = interface._get_previous_variable_name()
        assert previous_variable_name == ""

        interface.variable_name = "test_interface_2"
        previous_variable_name = interface._get_previous_variable_name()
        assert previous_variable_name == "test_interface_1"
