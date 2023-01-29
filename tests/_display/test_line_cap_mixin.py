import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display.line_cap_mixin import LineCapMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestLineCapMixIn:
    @apply_test_settings()
    def test__initialize_line_cap_if_not_initialized(self) -> None:
        mixin: LineCapMixIn = LineCapMixIn()
        mixin._initialize_line_cap_if_not_initialized()
        assert mixin._line_cap == ap.LineCaps.BUTT.value

        mixin._line_cap = ap.String(ap.LineCaps.ROUND.value)
        mixin._initialize_line_cap_if_not_initialized()
        assert mixin._line_cap == ap.LineCaps.ROUND.value

    @apply_test_settings()
    def test_line_cap(self) -> None:
        mixin: LineCapMixIn = LineCapMixIn()
        mixin.variable_name = "test_line_cap_mixin"
        assert mixin.line_cap == ap.LineCaps.BUTT.value

        mixin.line_cap = ap.LineCaps.ROUND
        assert mixin.line_cap == ap.LineCaps.ROUND.value  # type: ignore

        mixin.line_cap = ap.String(ap.LineCaps.BUTT.value)
        assert mixin.line_cap == ap.LineCaps.BUTT.value

    @apply_test_settings()
    def test__append_line_cap_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineCapMixIn = LineCapMixIn()
        mixin.variable_name = "test_line_cap_mixin"
        mixin.line_cap = ap.LineCaps.ROUND
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{mixin.variable_name}.attr\({{"
                rf'"stroke-linecap": {var_names.STRING}\_.+?}}\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: LineCapMixIn = LineCapMixIn()
        mixin.variable_name = "test_line_cap_mixin"
        mixin.line_cap = ap.LineCaps.ROUND
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._line_cap_snapshots == {snapshot_name: ap.LineCaps.ROUND.value}

        mixin.line_cap = ap.LineCaps.BUTT
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._line_cap_snapshots == {snapshot_name: ap.LineCaps.ROUND.value}

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: LineCapMixIn = LineCapMixIn()
        mixin.variable_name = "test_line_cap_mixin"
        mixin.line_cap = ap.LineCaps.ROUND
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.line_cap = ap.LineCaps.BUTT
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.line_cap == ap.LineCaps.ROUND.value  # type: ignore

        mixin.line_cap = ap.LineCaps.BUTT
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.line_cap == ap.LineCaps.BUTT.value  # type: ignore

    @apply_test_settings()
    def test__update_line_cap_and_skip_appending_exp(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineCapMixIn = LineCapMixIn()
        mixin.variable_name = "test_line_cap_mixin"
        mixin._update_line_cap_and_skip_appending_exp(value=ap.LineCaps.ROUND)
        assert mixin.line_cap == ap.LineCaps.ROUND.value
        mixin._update_line_cap_and_skip_appending_exp(
            value=ap.String(ap.LineCaps.BUTT.value)
        )
        assert mixin.line_cap == ap.LineCaps.BUTT.value
        expression: str = expression_data_util.get_current_expression()
        assert f"{mixin.variable_name}.attr" not in expression
