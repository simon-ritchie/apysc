import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_round_dot_setting_mixin import LineRoundDotSettingMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestLineRoundDotSettingMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_round_dot_setting_if_not_initialized(self) -> None:
        mixin: LineRoundDotSettingMixIn = LineRoundDotSettingMixIn()
        mixin._initialize_line_round_dot_setting_if_not_initialized()
        assert mixin._line_round_dot_setting is None

        mixin._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )
        mixin._initialize_line_round_dot_setting_if_not_initialized()
        assert isinstance(mixin._line_round_dot_setting, ap.LineRoundDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_round_dot_setting(self) -> None:
        mixin: LineRoundDotSettingMixIn = LineRoundDotSettingMixIn()
        line_round_dot_setting: Optional[
            ap.LineRoundDotSetting
        ] = mixin.line_round_dot_setting
        assert line_round_dot_setting is None

        mixin._line_round_dot_setting = ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )
        line_round_dot_setting = mixin.line_round_dot_setting
        assert isinstance(line_round_dot_setting, ap.LineRoundDotSetting)

        mixin.variable_name = "test_line_round_dot_setting_mixin"
        line_round_dot_setting = ap.LineRoundDotSetting(round_size=10, space_size=5)
        mixin.line_round_dot_setting = line_round_dot_setting
        assert mixin.line_round_dot_setting == line_round_dot_setting
        assert mixin.line_cap.value == ap.LineCaps.ROUND.value
        assert mixin.line_thickness == 10

        mixin.line_round_dot_setting = None
        assert mixin.line_cap.value == ap.LineCaps.BUTT.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_round_dot_setting_and_skip_appending_exp(self) -> None:
        mixin: LineRoundDotSettingMixIn = LineRoundDotSettingMixIn()
        line_round_dot_setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )
        mixin._update_line_round_dot_setting_and_skip_appending_exp(
            value=line_round_dot_setting
        )
        assert mixin._line_round_dot_setting == line_round_dot_setting

        mixin._update_line_round_dot_setting_and_skip_appending_exp(value=None)
        assert mixin._line_round_dot_setting is None

        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin._update_line_round_dot_setting_and_skip_appending_exp,
            match=r"Not supported line_round_dot_setting type specified: ",
            value=10,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_round_dot_setting_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineRoundDotSettingMixIn = LineRoundDotSettingMixIn()
        mixin.variable_name = "test_line_round_dot_setting_mixin"
        line_round_dot_setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )
        mixin.line_round_dot_setting = line_round_dot_setting
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{mixin.variable_name}.css\("stroke-dasharray", '
                rf'"1 " \+ String\(.+? \+ .+?\)\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

        expression_data_util.empty_expression()
        mixin.line_round_dot_setting = None
        expression = expression_data_util.get_current_expression()
        expected: str = f"{mixin.variable_name}.css" f'("stroke-dasharray", "");'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: LineRoundDotSettingMixIn = LineRoundDotSettingMixIn()
        mixin.variable_name = "test_line_round_dot_setting_mixin"
        line_round_dot_setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )
        mixin.line_round_dot_setting = line_round_dot_setting
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert (
            mixin._line_round_dot_setting_snapshots[snapshot_name]
            == line_round_dot_setting
        )

        mixin.line_round_dot_setting = None
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert (
            mixin._line_round_dot_setting_snapshots[snapshot_name]
            == line_round_dot_setting
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: LineRoundDotSettingMixIn = LineRoundDotSettingMixIn()
        mixin.variable_name = "test_line_round_dot_setting_mixin"
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        line_round_dot_setting: ap.LineRoundDotSetting = ap.LineRoundDotSetting(
            round_size=10, space_size=5
        )
        mixin.line_round_dot_setting = line_round_dot_setting
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.line_round_dot_setting = None
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.line_round_dot_setting == line_round_dot_setting