from random import randint

from retrying import retry

from apysc.display.line_joints_interface import LineJointsInterface
from apysc import LineJoints, String
from tests.testing_helper import assert_raises
from apysc.expression import expression_file_util


class TestLineJointsInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_joints_if_not_initialized(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface._initialize_line_joints_if_not_initialized()
        assert interface._line_joints == LineJoints.MITER.value

        interface._line_joints = String(LineJoints.BEVEL.value)
        interface._initialize_line_joints_if_not_initialized()
        assert interface._line_joints == LineJoints.BEVEL.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_joints(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        interface._initialize_line_joints_if_not_initialized()
        assert interface.line_joints == LineJoints.MITER.value

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_joints_and_skip_appending_exp(self) -> None:
        expression_file_util.remove_expression_file()
        interface: LineJointsInterface = LineJointsInterface()
        interface.variable_name = 'test_line_joints_interface'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=interface._update_line_joints_and_skip_appending_exp,
            kwargs={'value': 'miter'},
            match=r'Not supported line_joints type specified: ')

        interface._update_line_joints_and_skip_appending_exp(
            value=String(LineJoints.BEVEL.value))
        assert interface.line_joints == LineJoints.BEVEL.value
        expression: str = expression_file_util.get_current_expression()
        assert '.attr' not in expression

        interface._update_line_joints_and_skip_appending_exp(
            value=LineJoints.MITER)
        assert interface.line_joints == LineJoints.MITER.value
