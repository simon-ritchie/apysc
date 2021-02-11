from apyscript.display.point_interface import PointInterface


class TestPointInterface:

    def test_x(self) -> None:
        point_interface: PointInterface = PointInterface()
        point_interface.x = 100
        assert point_interface.x == 100

    def test_y(self) -> None:
        point_interface: PointInterface = PointInterface()
        point_interface.y = 200
        assert point_interface.y == 200
