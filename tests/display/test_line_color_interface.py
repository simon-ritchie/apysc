from random import randint

from retrying import retry

from apysc.display.line_color_interface import LineColorInterface
from apysc.expression import expression_file_util
from apysc.type import String


class TestLineColorInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_line_color(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        string_1: String = String('#555')
        line_color_interface.line_color = string_1
        assert line_color_interface.line_color == '#555555'

        string_2: String = line_color_interface.line_color
        string_2.value = String('#666')
        assert line_color_interface.line_color != string_2
        assert (
            line_color_interface.line_color.variable_name
            != string_2.variable_name)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_line_color_update_expression(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        expression_file_util.remove_expression_file()
        line_color_interface.line_color = String('#333')
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_line_color_interface.stroke("#333333");'
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_update_line_color_and_skip_appending_exp(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        expression_file_util.remove_expression_file()
        line_color_interface.update_line_color_and_skip_appending_exp(
            value=String('#777'))
        assert line_color_interface.line_color == '#777777'
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{line_color_interface.variable_name}.stroke('
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_line_color_if_not_initialized(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface._initialize_line_color_if_not_initialized()
        assert line_color_interface.line_color == ''
        line_color_interface.line_color = String('#333')
        line_color_interface._initialize_line_color_if_not_initialized()
        assert line_color_interface.line_color == '#333333'

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface.line_color = String('#333')
        snapshot_name: str = 'snapshot_1'
        line_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            line_color_interface._line_color_snapshots[snapshot_name]
            == '#333333')

        line_color_interface.line_color = String('#222')
        line_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            line_color_interface._line_color_snapshots[snapshot_name]
            == '#333333')

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface.line_color = String('#333')
        snapshot_name: str = 'snapshot_1'
        line_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        line_color_interface.line_color = String('#222')
        line_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert line_color_interface.line_color == '#333333'
        assert snapshot_name not in line_color_interface._line_color_snapshots

        line_color_interface.line_color = String('#222')
        line_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert line_color_interface.line_color == '#222222'
