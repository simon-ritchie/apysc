from random import randint

from retrying import retry

import apysc as ap
from apysc._display.ellipse_height_interface import EllipseHeightInterface
from apysc._expression import expression_data_util


class TestEllipseHeightInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ellipse_height_if_not_initialized(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface._initialize_ellipse_height_if_not_initialized()
        assert interface._ellipse_height == 0

        interface._ellipse_height = ap.Int(10)
        interface._initialize_ellipse_height_if_not_initialized()
        assert interface._ellipse_height == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_ellipse_height(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface.variable_name = 'test_ellipse_height_interface'
        assert interface.ellipse_height == 0

        interface.ellipse_height = ap.Int(10)
        assert interface.ellipse_height == 10

        interface.ellipse_height = 20  # type: ignore
        assert interface.ellipse_height == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_height_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface.variable_name = 'test_ellipse_height_interface'
        ellipse_height: ap.Int = ap.Int(10)
        interface.ellipse_height = ellipse_height
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.radius(0, '
            f'{ellipse_height.variable_name});'
        )
        assert expected in expression

        expression_data_util.empty_expression()
        ellipse_width: ap.Int = ap.Int(20)
        setattr(interface, '_ellipse_width', ellipse_width)
        interface.ellipse_height = ellipse_height
        expression = expression_data_util.get_current_expression()
        expected = (
            f'{interface.variable_name}.radius('
            f'{ellipse_width.variable_name}, '
            f'{ellipse_height.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface.variable_name = 'test_ellipse_height_interface'
        interface.ellipse_height = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._ellipse_height_snapshots[snapshot_name] == 10

        interface.ellipse_height = ap.Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._ellipse_height_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface.variable_name = 'test_ellipse_height_interface'
        interface.ellipse_height = ap.Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.ellipse_height = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.ellipse_height == 10

        interface.ellipse_height = ap.Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.ellipse_height == 20

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_height_attr_linking_setting(self) -> None:
        interface: EllipseHeightInterface = EllipseHeightInterface()
        interface.variable_name = 'test_ellipse_height_interface'
        interface._initialize_ellipse_height_if_not_initialized()
        assert interface._attr_linking_stack['ellipse_height'] == [ap.Int(0)]
