import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_joints_interface import LineJointsInterface
from apysc._expression import expression_file_util
from tests.testing_helper import assert_raises


class TestLineJointsInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_joints_if_not_initialized(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface._initialize_line_joints_if_not_initialized()
        assert interface._line_joints == ap.LineJoints.MITER.value

        interface._line_joints = ap.String(ap.LineJoints.BEVEL.value)
        interface._initialize_line_joints_if_not_initialized()
        assert interface._line_joints == ap.LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_joints(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        interface._initialize_line_joints_if_not_initialized()
        assert interface.line_joints == ap.LineJoints.MITER.value

        interface.line_joints = ap.LineJoints.BEVEL
        assert interface.line_joints == ap.LineJoints.BEVEL.value  # type: ignore # noqa

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_joints_and_skip_appending_exp(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface.
            _update_line_joints_and_skip_appending_exp,
            kwargs={'value': 'miter'},
            match=r'Not supported line_joints type specified: ')

        interface._update_line_joints_and_skip_appending_exp(
            value=ap.String(ap.LineJoints.BEVEL.value))
        assert interface.line_joints == ap.LineJoints.BEVEL.value
        expression: str = expression_file_util.get_current_expression()
        assert '.attr' not in expression

        interface._update_line_joints_and_skip_appending_exp(
            value=ap.LineJoints.MITER)
        assert interface.line_joints == ap.LineJoints.MITER.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_joints_update_expression(self) -> None:
        expression_file_util.empty_expression_dir()
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        interface.line_joints = ap.LineJoints.BEVEL
        interface._append_line_joints_update_expression()
        expression: str = expression_file_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf'{interface.variable_name}.attr'
                rf'\({{"stroke-linejoin": .+?}}\);'
            ),
            string=expression,
            flags=re.MULTILINE)
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_joints_snapshots == {
            snapshot_name: ap.LineJoints.MITER.value}

        interface.line_joints = ap.LineJoints.BEVEL
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._line_joints_snapshots == {
            snapshot_name: ap.LineJoints.MITER.value}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.line_joints = ap.LineJoints.BEVEL
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_joints == ap.LineJoints.MITER.value  # type: ignore # noqa

        interface.line_joints = ap.LineJoints.BEVEL
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.line_joints == ap.LineJoints.BEVEL.value  # type: ignore # noqa
