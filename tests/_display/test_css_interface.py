from random import randint

from retrying import retry

import apysc as ap
from apysc._display.css_interface import CssInterface


class TestCssInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_css_if_not_initialized(self) -> None:
        interface: CssInterface = CssInterface()
        interface._initialize_css_if_not_initialized()
        assert interface._css == {}

        interface._css['display'] = ap.String('none')
        interface._initialize_css_if_not_initialized()
        assert interface._css == {'display': 'none'}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_get_css(self) -> None:
        interface: CssInterface = CssInterface()
        css: ap.String = interface.get_css(name='display')
        assert css == ''

        interface._css['display'] = ap.String('none')
        css = interface.get_css(name='display')
        assert css == 'none'
