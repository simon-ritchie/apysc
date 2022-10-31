from apysc._type.type_name_mixin import TypeNameMixIn


class TestTypeNameMixIn:
    def test_type_name(self) -> None:
        interface: TypeNameMixIn = TypeNameMixIn()
        interface._type_name = "test_type_name"
        assert interface.type_name == "test_type_name"
