from apysc.type.variable_name_interface import VariableNameInterface


class TestVariableNameInterface:

    def test_variable_name(self) -> None:
        interface: VariableNameInterface = VariableNameInterface()
        interface.variable_name = 'test_interface_1'
        assert interface.variable_name == 'test_interface_1'
        assert interface._variable_name_history == ['test_interface_1']

        interface.variable_name = 'test_interface_2'
        assert interface.variable_name == 'test_interface_2'
        assert interface._variable_name_history == [
            'test_interface_1', 'test_interface_2']
