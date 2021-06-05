from random import randint

from retrying import retry

from apysc import Int
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc.display.ellipse_size_interface import EllipseSizeInterface
from apysc.expression import expression_file_util


class TestEllipseSizeInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ellipse_size_if_not_initialized(self) -> None:
        interface: EllipseSizeInterface = EllipseSizeInterface()
        interface._initialize_ellipse_size_if_not_initialized()
        assert interface._ellipse_size == 0

        interface._ellipse_size.value = 10
        interface._initialize_ellipse_size_if_not_initialized()
        assert interface._ellipse_size == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_ellipse_size(self) -> None:
        interface: EllipseSizeInterface = EllipseSizeInterface()
        interface.variable_name = 'test_ellipse_size_interface'
        assert interface.ellipse_size == 0

        interface.ellipse_size = Int(10)
        assert interface.ellipse_size == 10

        interface.ellipse_size = 20  # type: ignore
        assert interface.ellipse_size == 20

        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        rectangle: Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50)
        rectangle.ellipse_size = Int(10)
        assert rectangle.ellipse_width == Int(10)
        assert rectangle.ellipse_height == Int(10)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_ellipse_size_update_expression(self) -> None:
        expression_file_util.remove_expression_file()
        interface: EllipseSizeInterface = EllipseSizeInterface()
        interface.variable_name = 'test_ellipse_size_interface'
        ellipse_size: Int = Int(10)
        interface.ellipse_size = ellipse_size
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{interface.variable_name}.radius({ellipse_size.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: EllipseSizeInterface = EllipseSizeInterface()
        interface.variable_name = 'test_ellipse_size_interface'
        interface.ellipse_size = Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._ellipse_size_snapshots[snapshot_name] == 10

        interface.ellipse_size = Int(20)
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._ellipse_size_snapshots[snapshot_name] == 10

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: EllipseSizeInterface = EllipseSizeInterface()
        interface.variable_name = 'test_ellipse_size_interface'
        interface.ellipse_size = Int(10)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.ellipse_size = Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.ellipse_size == 10

        interface.ellipse_size = Int(20)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.ellipse_size == 20
