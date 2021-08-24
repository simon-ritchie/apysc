from random import randint

from retrying import retry

import apysc as ap
from apysc._display.fill_color_interface import FillColorInterface
from apysc._expression import expression_data_util


class TestFillColorInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_fill_color(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        string_1: ap.String = ap.String('#333')
        fill_color_interface.fill_color = string_1
        assert fill_color_interface.fill_color == '#333333'

        string_2: ap.String = fill_color_interface.fill_color
        assert string_1.variable_name != string_2.variable_name

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_fill_color_update_expression(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        expression_data_util.empty_expression()
        fill_color_interface.fill_color = ap.String('#666')
        expression: str = expression_data_util.get_current_expression()
        expected: str = 'test_fill_color_interface.fill("#666666");'
        assert expected in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__update_fill_color_and_skip_appending_exp(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        expression_data_util.empty_expression()
        fill_color_interface._update_fill_color_and_skip_appending_exp(
            value=ap.String('#333'))
        assert fill_color_interface.fill_color == '#333333'
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f'{fill_color_interface.variable_name}.fill(')
        assert expected not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_fill_color_if_not_initialized(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface._initialize_fill_color_if_not_initialized()
        assert fill_color_interface.fill_color == ''
        fill_color_interface.fill_color = ap.String('#333')
        fill_color_interface._initialize_fill_color_if_not_initialized()
        assert fill_color_interface.fill_color == '#333333'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface.fill_color = ap.String('#333333')
        snapshot_name: str = 'snapshot_1'
        fill_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            fill_color_interface._fill_color_snapshots[snapshot_name]
            == '#333333'
        )

        fill_color_interface.fill_color = ap.String('#222222')
        fill_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            fill_color_interface._fill_color_snapshots[snapshot_name]
            == '#333333'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface.fill_color = ap.String('#333333')
        snapshot_name: str = 'snapshot_1'
        fill_color_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        fill_color_interface.fill_color = ap.String('#222222')
        fill_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert fill_color_interface.fill_color == '#333333'

        fill_color_interface.fill_color = ap.String('#222222')
        fill_color_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert fill_color_interface.fill_color == '#222222'

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__set_initial_fill_color_if_not_blank(self) -> None:
        fill_color_interface: FillColorInterface = FillColorInterface()
        fill_color_interface.variable_name = 'test_fill_color_interface'
        fill_color_interface._set_initial_fill_color_if_not_blank(
            fill_color='')
        assert fill_color_interface.fill_color == ''
        fill_color_interface._set_initial_fill_color_if_not_blank(
            fill_color='0af')
        assert fill_color_interface.fill_color == '#00aaff'
