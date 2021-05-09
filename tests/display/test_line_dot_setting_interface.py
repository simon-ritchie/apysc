from random import randint
import re
from typing import Match, Optional

from retrying import retry

from apysc.display.line_dot_setting_interface import LineDotSettingInterface
from apysc.expression import expression_file_util, var_names
from apysc import LineDotSetting
from tests.testing_helper import assert_raises


class TestLineDotSettingInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_dot_setting_if_not_initialized(self) -> None:
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface._initialize_line_dot_setting_if_not_initialized()
        assert interface._line_dot_setting is None

        interface._line_dot_setting = LineDotSetting(dot_size=10)
        interface._initialize_line_dot_setting_if_not_initialized()
        assert interface._line_dot_setting.dot_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_dot_setting(self) -> None:
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface.variable_name = 'test_line_dot_setting_interface'
        line_dot_setting: Optional[LineDotSetting] = \
            interface.line_dot_setting
        assert line_dot_setting is None

        interface._line_dot_setting = LineDotSetting(dot_size=10)
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting.dot_size == 10

        interface.line_dot_setting = None
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting is None

        interface.line_dot_setting = LineDotSetting(dot_size=20)
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting.dot_size == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_dot_setting_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface.variable_name = 'test_line_dot_setting_interface'
        interface._initialize_line_dot_setting_if_not_initialized()
        interface._append_line_dot_setting_update_expression()
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.css("stroke-dasharray", "");'
        )
        assert expected in expression

        expression_file_util.remove_expression_file()
        interface._line_dot_setting = LineDotSetting(dot_size=10)
        interface._append_line_dot_setting_update_expression()
        expression = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.css\("stroke-dasharray", '
                rf'{var_names.INT}_.+\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_dot_setting_and_skip_appending_exp(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineDotSettingInterface = LineDotSettingInterface()
        interface._update_line_dot_setting_and_skip_appending_exp(
            value=None)
        line_dot_setting: Optional[LineDotSetting] = \
            interface.line_dot_setting
        assert line_dot_setting is None
        expression: str = expression_file_util.get_current_expression()
        assert '.css' not in expression

        interface._update_line_dot_setting_and_skip_appending_exp(
            value=LineDotSetting(dot_size=10))
        line_dot_setting = interface.line_dot_setting
        assert line_dot_setting.dot_size == 10

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface.
            _update_line_dot_setting_and_skip_appending_exp,
            kwargs={'value': 10},
            match='Not supported line_dot_setting type specified: ')
