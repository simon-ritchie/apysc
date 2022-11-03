import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display.line_joints_mixin import LineJointsMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import assert_raises


class TestLineJointsMixIn:
    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_joints_if_not_initialized(self) -> None:
        mixin: LineJointsMixIn = LineJointsMixIn()
        mixin._initialize_line_joints_if_not_initialized()
        assert mixin._line_joints == ap.LineJoints.MITER.value

        mixin._line_joints = ap.String(ap.LineJoints.BEVEL.value)
        mixin._initialize_line_joints_if_not_initialized()
        assert mixin._line_joints == ap.LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_joints(self) -> None:
        mixin: LineJointsMixIn = LineJointsMixIn()
        mixin.variable_name = "test_line_joints_mixin"
        mixin._initialize_line_joints_if_not_initialized()
        assert mixin.line_joints == ap.LineJoints.MITER.value

        mixin.line_joints = ap.LineJoints.BEVEL
        assert mixin.line_joints == ap.LineJoints.BEVEL.value  # type: ignore # noqa

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_joints_and_skip_appending_exp(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineJointsMixIn = LineJointsMixIn()
        mixin.variable_name = "test_line_joints_mixin"
        assert_raises(
            expected_error_class=TypeError,
            callable_=mixin._update_line_joints_and_skip_appending_exp,
            match=r"Not supported line_joints type specified: ",
            value="miter",
        )

        mixin._update_line_joints_and_skip_appending_exp(
            value=ap.String(ap.LineJoints.BEVEL.value)
        )
        assert mixin.line_joints == ap.LineJoints.BEVEL.value
        expression: str = expression_data_util.get_current_expression()
        assert ".attr" not in expression

        mixin._update_line_joints_and_skip_appending_exp(value=ap.LineJoints.MITER)
        assert mixin.line_joints == ap.LineJoints.MITER.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_joints_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: LineJointsMixIn = LineJointsMixIn()
        mixin.variable_name = "test_line_joints_mixin"
        mixin.line_joints = ap.LineJoints.BEVEL
        mixin._append_line_joints_update_expression()
        expression: str = expression_data_util.get_current_expression()
        match: Optional[Match] = re.search(
            pattern=(
                rf"{mixin.variable_name}.attr" rf'\({{"stroke-linejoin": .+?}}\);'
            ),
            string=expression,
            flags=re.MULTILINE,
        )
        assert match is not None

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        mixin: LineJointsMixIn = LineJointsMixIn()
        mixin.variable_name = "test_line_joints_mixin"
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._line_joints_snapshots == {
            snapshot_name: ap.LineJoints.MITER.value
        }

        mixin.line_joints = ap.LineJoints.BEVEL
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._line_joints_snapshots == {
            snapshot_name: ap.LineJoints.MITER.value
        }

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        mixin: LineJointsMixIn = LineJointsMixIn()
        mixin.variable_name = "test_line_joints_mixin"
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.line_joints = ap.LineJoints.BEVEL
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.line_joints == ap.LineJoints.MITER.value  # type: ignore # noqa

        mixin.line_joints = ap.LineJoints.BEVEL
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin.line_joints == ap.LineJoints.BEVEL.value  # type: ignore # noqa
