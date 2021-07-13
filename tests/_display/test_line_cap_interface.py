import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_cap_interface import LineCapInterface
from apysc._expression import expression_file_util
from apysc._expression import var_names
from tests.testing_helper import assert_raises


class TestLineCapInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_cap_if_not_initialized(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == ap.LineCaps.BUTT.value

        interface._line_cap = ap.String(ap.LineCaps.ROUND.value)
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == ap.LineCaps.ROUND.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_cap(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        assert interface.line_cap == ap.LineCaps.BUTT.value

        interface.line_cap = ap.LineCaps.ROUND
        assert interface.line_cap == ap.LineCaps.ROUND.value  # type: ignore

        interface.line_cap = ap.String(ap.LineCaps.BUTT.value)
        assert interface.line_cap == ap.LineCaps.BUTT.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_cap_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        interface.line_cap = ap.LineCaps.ROUND
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.attr\({{'
                rf'"stroke-linecap": {var_names.STRING}\_.+?}}\);'
            ),
            string=expression, flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        interface.line_cap = ap.LineCaps.ROUND
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_cap_snapshots == {
            snapshot_name: ap.LineCaps.ROUND.value}

        interface.line_cap = ap.LineCaps.BUTT
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_cap_snapshots == {
            snapshot_name: ap.LineCaps.ROUND.value}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        interface.line_cap = ap.LineCaps.ROUND
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_cap = ap.LineCaps.BUTT
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_cap == ap.LineCaps.ROUND.value  # type: ignore

        interface.line_cap = ap.LineCaps.BUTT
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_cap == ap.LineCaps.BUTT.value  # type: ignore

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_cap_and_skip_appending_exp(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        interface._update_line_cap_and_skip_appending_exp(
            value=ap.LineCaps.ROUND)
        assert interface.line_cap == ap.LineCaps.ROUND.value
        interface._update_line_cap_and_skip_appending_exp(
            value=ap.String(ap.LineCaps.BUTT.value))
        assert interface.line_cap == ap.LineCaps.BUTT.value
        expression: str = expression_file_util.get_current_expression()
        assert f'{interface.variable_name}.attr' not in expression

        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface._update_line_cap_and_skip_appending_exp,
            kwargs={'value': 'round'},
            match=r'Not supported line_cap type specified: ')
