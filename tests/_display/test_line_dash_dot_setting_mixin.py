import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_dash_dot_setting_mixin import LineDashDotSettingMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestLineDashDotSettingMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_dot_setting_if_not_initialized(self) -> None:
        mixin: LineDashDotSettingMixIn = LineDashDotSettingMixIn()
        mixin._initialize_line_dash_dot_setting_if_not_initialized()
        assert mixin._line_dash_dot_setting is None

        mixin._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7
        )
        mixin._initialize_line_dash_dot_setting_if_not_initialized()
        assert isinstance(mixin._line_dash_dot_setting, ap.LineDashDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_dot_setting(self) -> None:
        mixin: LineDashDotSettingMixIn = LineDashDotSettingMixIn()
        mixin.variable_name = "test_line_dash_dot_setting_mixin"
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7
        )
        mixin._line_dash_dot_setting = line_dash_dot_setting
        assert mixin.line_dash_dot_setting == line_dash_dot_setting

        mixin.line_dash_dot_setting = None
        assert mixin.line_dash_dot_setting is None
        mixin.line_dash_dot_setting = line_dash_dot_setting
        assert mixin.line_dash_dot_setting == line_dash_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dash_dot_setting_and_skip_appending_exp(self) -> None:
        mixin: LineDashDotSettingMixIn = LineDashDotSettingMixIn()
        mixin._update_line_dash_dot_setting_and_skip_appending_exp(value=None)
        assert mixin._line_dash_dot_setting is None

        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7
        )
        mixin._update_line_dash_dot_setting_and_skip_appending_exp(
            value=line_dash_dot_setting
        )
        assert mixin._line_dash_dot_setting == line_dash_dot_setting

        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin._update_line_dash_dot_setting_and_skip_appending_exp,
            match="Not supported line_dash_dot_setting type specified: ",
            value=10,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dash_dot_setting_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineDashDotSettingMixIn = LineDashDotSettingMixIn()
        mixin.variable_name = "test_line_dash_dot_setting_mixin"
        mixin._initialize_line_dash_dot_setting_if_not_initialized()
        mixin._append_line_dash_dot_setting_update_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{mixin.variable_name}.css("stroke-dasharray", "");'
        assert expected in expression

        expression_data_util.empty_expression()
        mixin._line_dash_dot_setting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7
        )
        mixin._append_line_dash_dot_setting_update_expression()
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{mixin.variable_name}.css\("stroke-dasharray", '
                rf'String\(.*?\) \+ " " \+ '
                rf'String\(.+?\) \+ " " \+ '
                rf'String\(.+?\) \+ " " \+ '
                rf"String\(.+?\)\);"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: LineDashDotSettingMixIn = LineDashDotSettingMixIn()
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7
        )
        mixin._line_dash_dot_setting = line_dash_dot_setting
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._line_dash_dot_setting_snapshots == {
            snapshot_name: line_dash_dot_setting
        }

        mixin._line_dash_dot_setting = None
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._line_dash_dot_setting_snapshots == {
            snapshot_name: line_dash_dot_setting
        }

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: LineDashDotSettingMixIn = LineDashDotSettingMixIn()
        line_dash_dot_setting: ap.LineDashDotSetting = ap.LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7
        )
        mixin._line_dash_dot_setting = line_dash_dot_setting
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._line_dash_dot_setting = None
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._line_dash_dot_setting == line_dash_dot_setting
