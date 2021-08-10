from apysc._display.scale_x_from_point_interface import \
    ScaleXFromPointInterface


class _TestInterface(ScaleXFromPointInterface):

    def __init__(self) -> None:
        """
        The class for the testing for the `ScaleXFromPointInterface`
        class.
        """
        self.variable_name = 'scale_x_from_point_interface'


class TestScaleXFromPointInterface:

    def test__initialize_scale_x_from_points_if_not_initialized(self) -> None:
        interface: _TestInterface = _TestInterface()
        interface._initialize_scale_x_from_points_if_not_initialized()
        assert interface._scale_x_from_points == {}
        interface._scale_x_from_points['a'] = 10
        interface._initialize_scale_x_from_points_if_not_initialized()
        assert interface._scale_x_from_points == {'a': 10}
