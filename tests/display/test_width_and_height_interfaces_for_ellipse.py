from apysc.display.width_and_height_interfaces_for_ellipse import \
    WidthAndHeightInterfacesForEllipse
from apysc import Int


class TestWidthAndHeightInterfacesForEllipse:

    def test__initialize_width_and_height_if_not_initialized(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface._initialize_width_and_height_if_not_initialized()
        assert interface._width == 0
        assert interface._height == 0

        interface._width = Int(10)
        interface._height = Int(20)
        interface._initialize_width_and_height_if_not_initialized()
        assert interface._width == 10
        assert interface._height == 20
