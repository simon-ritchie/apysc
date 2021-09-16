from random import randint

from retrying import retry

import apysc as ap
from apysc._display.width_and_height_interfaces_for_ellipse import \
    WidthAndHeightInterfacesForEllipse
from apysc._expression import expression_data_util


class TestWidthAndHeightInterfacesForEllipse:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_width_and_height_if_not_initialized(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface._initialize_width_and_height_if_not_initialized()
        assert interface._width == 0
        assert interface._height == 0

        interface._width = ap.Int(10)
        interface._height = ap.Int(20)
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

        interface.width = ap.Int(10)
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

        interface.height = ap.Int(10)
        assert interface.height == 10

        interface.height = 20  # type: ignore
        assert interface.height == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_width_and_height_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        width: ap.Int = ap.Int(10)
        interface.width = width
        height: ap.Int = ap.Int(20)
        interface.height = height
        expression: str = expression_data_util.get_current_expression()
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
        interface.width = ap.Int(10)
        interface.height = ap.Int(20)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._width_snapshots[snapshot_name] == 10
        assert interface._height_snapshots[snapshot_name] == 20

        interface.width = ap.Int(30)
        interface.height = ap.Int(40)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._width_snapshots[snapshot_name] == 10
        assert interface._height_snapshots[snapshot_name] == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        interface.width = ap.Int(10)
        interface.height = ap.Int(20)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.width = ap.Int(30)
        interface.height = ap.Int(40)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.width == 10
        assert interface.height == 20

        interface.width = ap.Int(30)
        interface.height = ap.Int(40)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.width == 30
        assert interface.height == 40

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_width_attr_linking_setting(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        interface._initialize_width_and_height_if_not_initialized()
        assert interface._attr_linking_stack['width'] == [ap.Int(0)]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_height_attr_linking_setting(self) -> None:
        interface: WidthAndHeightInterfacesForEllipse = \
            WidthAndHeightInterfacesForEllipse()
        interface.variable_name = \
            'test_width_and_height_interfaces_for_ellipse'
        interface._initialize_width_and_height_if_not_initialized()
        assert interface._attr_linking_stack['height'] == [ap.Int(0)]
