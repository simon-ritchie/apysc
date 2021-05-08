from random import randint
from typing import Match, Optional
import re

from retrying import retry

from apysc.display.line_cap_interface import LineCapInterface
from apysc import LineCaps, String
from apysc.expression import expression_file_util, var_names


class TestLineCapInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_cap_if_not_initialized(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == LineCaps.BUTT.value

        interface._line_cap = String(LineCaps.ROUND.value)
        interface._initialize_line_cap_if_not_initialized()
        assert interface._line_cap == LineCaps.ROUND.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_cap(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        assert interface.line_cap == LineCaps.BUTT.value

        interface.line_cap = LineCaps.ROUND
        assert interface.line_cap == LineCaps.ROUND.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_cap_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        interface.line_cap = LineCaps.ROUND
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
        interface.line_cap = LineCaps.ROUND
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_cap_snapshots == {
            snapshot_name: LineCaps.ROUND.value}

        interface.line_cap = LineCaps.BUTT
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_cap_snapshots == {
            snapshot_name: LineCaps.ROUND.value}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineCapInterface = LineCapInterface()
        interface.variable_name = 'test_line_color_interface'
        interface.line_cap = LineCaps.ROUND
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_cap = LineCaps.BUTT
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_cap == LineCaps.ROUND.value

        interface.line_cap = LineCaps.BUTT
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_cap == LineCaps.BUTT.value
