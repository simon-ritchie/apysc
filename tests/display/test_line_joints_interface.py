from random import randint

from retrying import retry

from apysc.display.line_joints_interface import LineJointsInterface
from apysc import LineJoints, String


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
