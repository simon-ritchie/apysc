from apyscript.type.copy_interface import CopyInterface


class TestCopyInterface:

    def test__copy(self) -> None:
        interface: CopyInterface = CopyInterface()
        interface.variable_name = 'test_copy_interface'
        interface._type_name = 'test_copy_interface'
        result: CopyInterface = interface._copy()
        assert result.variable_name.startswith('test_copy_interface_')
        assert result.variable_name != interface.variable_name
