import re
from random import randint
from typing import Match, Optional

from retrying import retry

from apysc import LineDashDotSetting
from apysc.display.line_dash_dot_setting_interface import \
    LineDashDotSettingInterface
from apysc.expression import expression_file_util


class TestLineDashDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dash_dot_setting_if_not_initialized(
            self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        assert interface._line_dash_dot_setting is None

        interface._line_dash_dot_setting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        assert isinstance(
            interface._line_dash_dot_setting, LineDashDotSetting)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dash_dot_setting(self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        line_dash_dot_setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._line_dash_dot_setting = line_dash_dot_setting
        assert interface.line_dash_dot_setting == line_dash_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dash_dot_setting_and_skip_appending_exp(
            self) -> None:
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface._update_line_dash_dot_setting_and_skip_appending_exp(
            value=None)
        assert interface._line_dash_dot_setting is None

        line_dash_dot_setting: LineDashDotSetting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._update_line_dash_dot_setting_and_skip_appending_exp(
            value=line_dash_dot_setting)
        assert interface._line_dash_dot_setting == line_dash_dot_setting

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dash_dot_setting_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineDashDotSettingInterface = LineDashDotSettingInterface()
        interface.variable_name = 'test_line_dash_dot_setting_interface'
        interface._initialize_line_dash_dot_setting_if_not_initialized()
        interface._append_line_dash_dot_setting_update_expression()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.css("stroke-dasharray", "");'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        interface._line_dash_dot_setting = LineDashDotSetting(
            dot_size=5, dash_size=10, space_size=7)
        interface._append_line_dash_dot_setting_update_expression()
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'String\(.*?\) \+ " " \+ '
                rf'String\(.+?\) \+ " " \+ '
                rf'String\(.+?\) \+ " " \+ '
                rf'String\(.+?\)\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None
