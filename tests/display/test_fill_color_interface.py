from random import randint

from retrying import retry

from apysc.display.fill_color_interface import FillColorInterface
from apysc.expression import expression_file_util
from apysc.type import String


class TestFillColorInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_fill_color(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        string_1: String = String('#333')
        fill_color_interface.fill_color = string_1
        assert fill_color_interface.fill_color == '#333333'

        string_2: String = fill_color_interface.fill_color
        assert string_1.variable_name != string_2.variable_name

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_fill_color_update_expression(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        expression_file_util.remove_expression_file()
        fill_color_interface.fill_color = String('#666')
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_fill_color_interface.fill("#666666");'
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_update_fill_color_and_skip_appending_exp(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        expression_file_util.remove_expression_file()
        fill_color_interface.update_fill_color_and_skip_appending_exp(
            value=String('#333'))
        assert fill_color_interface.fill_color == '#333333'
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{fill_color_interface.variable_name}.fill(')
        assert expected not in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_fill_color_if_not_initialized(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface._initialize_fill_color_if_not_initialized()
        assert fill_color_interface.fill_color == ''
        fill_color_interface.fill_color = String('#333')
        fill_color_interface._initialize_fill_color_if_not_initialized()
        assert fill_color_interface.fill_color == '#333333'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface.fill_color = String('#333333')
        snapshot_name: str = 'snapshot_1'
        fill_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            fill_color_interface._fill_color_snapshots[snapshot_name]
            == '#333333'
        )

        fill_color_interface.fill_color = String('#222222')
        fill_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            fill_color_interface._fill_color_snapshots[snapshot_name]
            == '#333333'
        )

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface.fill_color = String('#333333')
        snapshot_name: str = 'snapshot_1'
        fill_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        fill_color_interface.fill_color = String('#222222')
        fill_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert fill_color_interface.fill_color == '#333333'

        fill_color_interface.fill_color = String('#222222')
        fill_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert fill_color_interface.fill_color == '#222222'
