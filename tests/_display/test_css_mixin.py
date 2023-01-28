from random import randint

from retrying import retry

import apysc as ap
from apysc._display.css_mixin import CssMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class _TestMixIn(CssMixIn):
    def __init__(self) -> None:
        """The class for testing."""
        self.variable_name = "test_css_interface"


class TestCssMixIn:
    @apply_test_settings()
    def test__initialize_css_if_not_initialized(self) -> None:
        interface: CssMixIn = CssMixIn()
        interface._initialize_css_if_not_initialized()
        assert interface._css == {}

        interface._css["display"] = ap.String("none")
        interface._initialize_css_if_not_initialized()
        assert interface._css == {"display": ap.String("none")}

    @apply_test_settings()
    def test_get_css(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        css: ap.String = interface.get_css(name="display")
        assert css == ""

        interface._css["display"] = ap.String("none")
        css = interface.get_css(name="display")
        assert css == "none"

    @apply_test_settings()
    def test__append_get_css_expresion(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestMixIn = _TestMixIn()
        name: ap.String = ap.String("display")
        css: ap.String = interface.get_css(name=name)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{css.variable_name} = {interface.variable_name}"
            f".css({name.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test_set_css(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        name: ap.String = ap.String("display")
        interface.set_css(name=name, value="none")
        assert interface._css == {"display": ap.String("none")}

    @apply_test_settings()
    def test__append_set_css_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestMixIn = _TestMixIn()
        name: ap.String = ap.String("display")
        value: ap.String = ap.String("none")
        interface.set_css(name=name, value=value)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{interface.variable_name}.css({name.variable_name}, "
            f"{value.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.set_css(name="display", value="none")
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._css_snapshot[snapshot_name] == {"display": ap.String("none")}

        interface.set_css(name="display", value="none")
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._css_snapshot[snapshot_name] == {"display": ap.String("none")}

    @apply_test_settings()
    def test__revert(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.set_css(name="display", value="none")
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.set_css(name="display", value="")
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._css["display"] == "none"

        interface.set_css(name="display", value="")
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._css["display"] == ""
