from random import randint

from retrying import retry

from apysc import Int
from apysc._display.width_and_height_interfaces_for_ellipse import \
    WidthAndHeightInterfacesForEllipse
from apysc.expression import expression_file_util


class TestWidthAndHeightInterfacesForEllipse:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_width(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        assert interface.width == 0

        interface.width = Int(10)
        assert interface.width == 10

        interface.width = 20  # type: ignore
        assert interface.width == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_height(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        assert interface.height == 0

        interface.height = Int(10)
        assert interface.height == 10

        interface.height = 20  # type: ignore
        assert interface.height == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_width_and_height_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        width: Int = Int(10)
        interface.width = width
        height: Int = Int(20)
        interface.height = height
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.radius('
            f'parseInt({width.variable_name} / 2), '
            f'parseInt({height.variable_name}) / 2);'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        interface.width = Int(10)
        interface.height = Int(20)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._width_snapshots[snapshot_name] == 10
        assert interface._height_snapshots[snapshot_name] == 20

        interface.width = Int(30)
        interface.height = Int(40)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._width_snapshots[snapshot_name] == 10
        assert interface._height_snapshots[snapshot_name] == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        interface.width = Int(10)
        interface.height = Int(20)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.width = Int(30)
        interface.height = Int(40)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.width == 10
        assert interface.height == 20

        interface.width = Int(30)
        interface.height = Int(40)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.width == 30
        assert interface.height == 40
