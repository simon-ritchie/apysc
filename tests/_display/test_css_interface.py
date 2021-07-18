from random import randint

from retrying import retry

import apysc as ap
from apysc._display.css_interface import CssInterface
from apysc._expression import expression_file_util


class _TestInterface(CssInterface):

    def __init__(self) -> None:
        """The class for testing.
        """
        self.variable_name = 'test_css_interface'


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
        interface: _TestInterface = _TestInterface()
        css: ap.String = interface.get_css(name='display')
        assert css == ''

        interface._css['display'] = ap.String('none')
        css = interface.get_css(name='display')
        assert css == 'none'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_get_css_expresion(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: _TestInterface = _TestInterface()
        name: ap.String = ap.String('display')
        css: ap.String = interface.get_css(name=name)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{css.variable_name} = {interface.variable_name}'
            f'.css({name.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_set_css(self) -> None:
        interface: _TestInterface = _TestInterface()
        name: ap.String = ap.String('display')
        interface.set_css(name=name, value='none')
        assert interface._css == {'display': ap.String('none')}
