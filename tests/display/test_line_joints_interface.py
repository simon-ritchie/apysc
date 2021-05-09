from apysc.display.line_joints_interface import LineJointsInterface
from apysc import LineJoints, String


class TestLineJointsInterface:

    def test__initialize_line_joints_if_not_initialized(self) -> None:
        interface: LineJointsInterface = LineJointsInterface()
        interface._initialize_line_joints_if_not_initialized()
        assert interface._line_joints == LineJoints.MITER.value

        interface._line_joints = String(LineJoints.BEVEL.value)
        interface._initialize_line_joints_if_not_initialized()
        assert interface._line_joints == LineJoints.BEVEL.value
