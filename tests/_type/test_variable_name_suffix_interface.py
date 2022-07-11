from random import randint

from retrying import retry

from apysc._type.variable_name_suffix_interface import \
    VariableNameSuffixInterface


class TestVariableNameSuffixInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_variable_name_suffix(self) -> None:
        interface: VariableNameSuffixInterface = VariableNameSuffixInterface()
        assert interface.variable_name_suffix == ''

        interface.variable_name_suffix = 'test_instance'
        assert interface.variable_name_suffix == 'test_instance'
