from apysc._display.scale_x_from_center_interface import \
    ScaleXFromCenterInterface


class _TestInterface(ScaleXFromCenterInterface):

    def __init__(self) -> None:
        """
        The class for the testing of the ScaleXFromCenterInterface.
        """
        self.variable_name = 'scale_x_from_center_interface'


class TestScaleXFromCenterInterface:

    def test__initialize_scale_x_from_center_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_x_from_center_if_not_initialized()
        assert interface._scale_x_from_center == 1.0
        interface._scale_x_from_center._value = 0.5
        assert interface._scale_x_from_center == 0.5
