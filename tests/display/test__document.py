from apysc import document
from apysc.expression import var_names


class TestDocument:

    def test___init__(self) -> None:
        assert document.variable_name == var_names.DOCUMENT
