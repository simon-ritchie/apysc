from apysc.type.variable_name_interface import VariableNameInterface


class TestVariableNameInterface:

    def test_variable_name(self) -> None:
        interface: VariableNameInterface = VariableNameInterface()
        interface.variable_name = 'test_interface'
        assert interface.variable_name == 'test_interface'
