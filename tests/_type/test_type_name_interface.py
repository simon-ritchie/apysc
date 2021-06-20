from apysc._type.type_name_interface import TypeNameInterface


class TestTypeNameInterface:

    def test_type_name(self) -> None:
        interface: TypeNameInterface = TypeNameInterface()
        interface._type_name = 'test_type_name'
        assert interface.type_name == 'test_type_name'
