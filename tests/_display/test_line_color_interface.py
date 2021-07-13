from random import randint

from retrying import retry

import apysc as ap
from apysc._display.line_color_interface import LineColorInterface
from apysc._expression import expression_file_util


class TestLineColorInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_line_color(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        string_1: ap.String = ap.String('#555')
        line_color_interface.line_color = string_1
        assert line_color_interface.line_color == '#555555'

        string_2: ap.String = line_color_interface.line_color
        string_2.value = ap.String('#666')
        assert line_color_interface.line_color != string_2
        assert (
            line_color_interface.line_color.variable_name
            != string_2.variable_name)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_line_color_update_expression(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        expression_file_util.remove_expression_file()
        line_color_interface.line_color = ap.String('#333')
        expression: str = expression_file_util.get_current_expression()
        expected: str = 'test_line_color_interface.stroke("#333333");'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_line_color_and_skip_appending_exp(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        expression_file_util.remove_expression_file()
        line_color_interface._update_line_color_and_skip_appending_exp(
            value=ap.String('#777'))
        assert line_color_interface.line_color == '#777777'
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{line_color_interface.variable_name}.stroke('
        )
        assert expected not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_line_color_if_not_initialized(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface._initialize_line_color_if_not_initialized()
        assert line_color_interface.line_color == ''
        line_color_interface.line_color = ap.String('#333')
        line_color_interface._initialize_line_color_if_not_initialized()
        assert line_color_interface.line_color == '#333333'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface.line_color = ap.String('#333')
        snapshot_name: str = 'snapshot_1'
        line_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            line_color_interface._line_color_snapshots[snapshot_name]
            == '#333333')

        line_color_interface.line_color = ap.String('#222')
        line_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            line_color_interface._line_color_snapshots[snapshot_name]
            == '#333333')

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface.line_color = ap.String('#333')
        snapshot_name: str = 'snapshot_1'
        line_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        line_color_interface.line_color = ap.String('#222')
        line_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert line_color_interface.line_color == '#333333'

        line_color_interface.line_color = ap.String('#222')
        line_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert line_color_interface.line_color == '#222222'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_initial_line_color_if_not_blank(self) -> None:
        line_color_interface: LineColorInterface = LineColorInterface()
        line_color_interface.variable_name = 'test_line_color_interface'
        line_color_interface._set_initial_line_color_if_not_blank(
            line_color='')
        assert line_color_interface.line_color == ''

        line_color_interface._set_initial_line_color_if_not_blank(
            line_color='0af')
        assert line_color_interface.line_color == '#00aaff'
