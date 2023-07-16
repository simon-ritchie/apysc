import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.line_alpha_mixin import LineAlphaMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestLineAlphaMixIn:
    @apply_test_settings()
    def test_line_alpha(self) -> None:
        line_alpha_mixin: LineAlphaMixIn = LineAlphaMixIn()
        line_alpha_mixin.variable_name = "test_line_alpha_mixin"
        line_alpha_mixin.line_alpha = ap.Number(0.3)
        assert line_alpha_mixin.line_alpha == 0.3

    @apply_test_settings()
    def test__append_line_alpha_update_expression(self) -> None:
        line_alpha_mixin: LineAlphaMixIn = LineAlphaMixIn()
        line_alpha_mixin.variable_name = "test_line_alpha_mixin"
        ap.Stage()
        line_alpha_mixin.line_alpha = ap.Number(0.5)
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                r"test_line_alpha_mixin\.stroke"
                rf"\({{opacity: {var_names.NUMBER}_.+?}}\);"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__update_line_alpha_and_skip_appending_exp(self) -> None:
        line_alpha_mixin: LineAlphaMixIn = LineAlphaMixIn()
        line_alpha_mixin.variable_name = "test_line_alpha_mixin"
        ap.Stage()
        line_alpha_mixin._update_line_alpha_and_skip_appending_exp(
            value=ap.Number(0.25)
        )
        assert line_alpha_mixin.line_alpha == 0.25
        expression: str = expression_data_util.get_current_expression()
        assert "stroke-opacity" not in expression

        line_alpha_mixin._update_line_alpha_and_skip_appending_exp(value=0.3)
        assert line_alpha_mixin.line_alpha == 0.3

    @apply_test_settings()
    def test__initialize_line_alpha_if_not_initialized(self) -> None:
        line_alpha_mixin: LineAlphaMixIn = LineAlphaMixIn()
        line_alpha_mixin.variable_name = "test_line_alpha_mixin"
        line_alpha_mixin._initialize_line_alpha_if_not_initialized()
        assert line_alpha_mixin.line_alpha == 1.0

        line_alpha_mixin.line_alpha = ap.Number(0.5)
        line_alpha_mixin._initialize_line_alpha_if_not_initialized()
        assert line_alpha_mixin.line_alpha == 0.5

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        line_alpha_mixin: LineAlphaMixIn = LineAlphaMixIn()
        line_alpha_mixin.variable_name = "test_line_alpha_mixin"
        line_alpha_mixin.line_alpha = ap.Number(0.5)
        snapshot_name: str = "snapshot_1"
        line_alpha_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if line_alpha_mixin._line_alpha_snapshots is None:
            raise AssertionError()
        assert line_alpha_mixin._line_alpha_snapshots[snapshot_name] == 0.5

        line_alpha_mixin.line_alpha = ap.Number(0.3)
        line_alpha_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert line_alpha_mixin._line_alpha_snapshots[snapshot_name] == 0.5

    @apply_test_settings()
    def test__revert(self) -> None:
        line_alpha_mixin: LineAlphaMixIn = LineAlphaMixIn()
        line_alpha_mixin.variable_name = "test_line_alpha_mixin"
        line_alpha_mixin.line_alpha = ap.Number(0.5)
        snapshot_name: str = "snapshot_1"
        line_alpha_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        line_alpha_mixin.line_alpha = ap.Number(0.3)
        line_alpha_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert line_alpha_mixin.line_alpha == 0.5

        line_alpha_mixin.line_alpha = ap.Number(0.3)
        line_alpha_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert line_alpha_mixin.line_alpha == 0.3

    @apply_test_settings()
    def test__append_line_alpha_attr_linking_setting(self) -> None:
        interface: LineAlphaMixIn = LineAlphaMixIn()
        interface.variable_name = "test_line_alpha_mixin"
        interface._initialize_line_alpha_if_not_initialized()
        assert interface._attr_linking_stack["line_alpha"] == [ap.Number(1.0)]
