import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_dot_setting_mixin import LineDotSettingMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import assert_raises
from apysc._testing.testing_helper import apply_test_settings


class TestLineDotSettingMixIn:
    @apply_test_settings()
    def test__initialize_line_dot_setting_if_not_initialized(self) -> None:
        mixin: LineDotSettingMixIn = LineDotSettingMixIn()
        mixin._initialize_line_dot_setting_if_not_initialized()
        assert mixin._line_dot_setting is None

        mixin._line_dot_setting = ap.LineDotSetting(dot_size=10)
        mixin._initialize_line_dot_setting_if_not_initialized()
        assert mixin._line_dot_setting.dot_size == 10

    @apply_test_settings()
    def test_line_dot_setting(self) -> None:
        mixin: LineDotSettingMixIn = LineDotSettingMixIn()
        mixin.variable_name = "test_line_dot_setting_mixin"
        line_dot_setting: Optional[ap.LineDotSetting] = mixin.line_dot_setting
        assert line_dot_setting is None

        mixin._line_dot_setting = ap.LineDotSetting(dot_size=10)
        line_dot_setting = mixin.line_dot_setting
        assert line_dot_setting.dot_size == 10  # type: ignore

        mixin.line_dot_setting = None
        line_dot_setting = mixin.line_dot_setting
        assert line_dot_setting is None

        mixin.line_dot_setting = ap.LineDotSetting(dot_size=20)
        line_dot_setting = mixin.line_dot_setting
        assert line_dot_setting.dot_size == 20

    @apply_test_settings()
    def test__append_line_dot_setting_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineDotSettingMixIn = LineDotSettingMixIn()
        mixin.variable_name = "test_line_dot_setting_mixin"
        mixin._initialize_line_dot_setting_if_not_initialized()
        mixin._append_line_dot_setting_update_expression()
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'{mixin.variable_name}.css("stroke-dasharray", "");'
        assert expected in expression

        expression_data_util.empty_expression()
        mixin._line_dot_setting = ap.LineDotSetting(dot_size=10)
        mixin._append_line_dot_setting_update_expression()
        expression = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{mixin.variable_name}.css\("stroke-dasharray", '
                rf"{var_names.INT}_.+\);"
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @apply_test_settings()
    def test__update_line_dot_setting_and_skip_appending_exp(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineDotSettingMixIn = LineDotSettingMixIn()
        mixin._update_line_dot_setting_and_skip_appending_exp(value=None)
        line_dot_setting: Optional[ap.LineDotSetting] = mixin.line_dot_setting
        assert line_dot_setting is None
        expression: str = expression_data_util.get_current_expression()
        assert ".css" not in expression

        mixin._update_line_dot_setting_and_skip_appending_exp(
            value=ap.LineDotSetting(dot_size=10)
        )
        line_dot_setting = mixin.line_dot_setting
        assert line_dot_setting.dot_size == 10  # type: ignore

        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin._update_line_dot_setting_and_skip_appending_exp,
            match="Not supported line_dot_setting type specified: ",
            value=10,
        )

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: LineDotSettingMixIn = LineDotSettingMixIn()
        mixin.variable_name = "test_line_dot_setting_mixin"
        mixin.line_dot_setting = ap.LineDotSetting(dot_size=10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            mixin._line_dot_setting_snapshots[snapshot_name], ap.LineDotSetting
        )

        mixin.line_dot_setting = None
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert isinstance(
            mixin._line_dot_setting_snapshots[snapshot_name], ap.LineDotSetting
        )

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: LineDotSettingMixIn = LineDotSettingMixIn()
        mixin.variable_name = "test_line_dot_setting_mixin"
        mixin.line_dot_setting = ap.LineDotSetting(dot_size=10)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.line_dot_setting = None
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert isinstance(mixin.line_dot_setting, ap.LineDotSetting)

        mixin.line_dot_setting = None
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.line_dot_setting is None
