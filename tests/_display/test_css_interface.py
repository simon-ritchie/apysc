from apysc._display.css_interface import CssInterface


class TestCssInterface:

    def test__initialize_css_if_not_initialized(self) -> None:
        interface: CssInterface = CssInterface()
        interface._initialize_css_if_not_initialized()
        assert interface._css._value == {}

        interface._css['display'] = 'none'
        interface._initialize_css_if_not_initialized()
        assert interface._css._value == {'display': 'none'}
