from random import randint

from retrying import retry

from apysc.display.fill_alpha_interface import FillAlphaInterface
from apysc.expression import expression_file_util
from apysc.type import Number
from apysc.type import value_util


class TestFillAlphaInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_fill_alpha(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        fill_alpha_interface.fill_alpha = Number(0.5)
        assert fill_alpha_interface.fill_alpha == 0.5

        fill_alpha: Number = fill_alpha_interface.fill_alpha
        fill_alpha_name: str = fill_alpha.variable_name
        assert (
            fill_alpha_name != fill_alpha_interface._fill_alpha.variable_name)

        fill_alpha_interface.fill_alpha = 0.25  # type: ignore
        assert fill_alpha_interface.fill_alpha == 0.25

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_fill_alpha_update_expression(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        expression_file_util.remove_expression_file()
        fill_alpha_interface.fill_alpha = Number(0.3)
        expression: str = expression_file_util.get_current_expression()
        value_str: str = value_util.get_value_str_for_expression(
            value=fill_alpha_interface._fill_alpha)
        expected: str = (
            f'{fill_alpha_interface.variable_name}'
            f'.fill({{opacity: {value_str}}});')
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_update_fill_alpha_and_skip_appending_exp(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        expression_file_util.remove_expression_file()
        fill_alpha_interface.update_fill_alpha_and_skip_appending_exp(
            value=0.25)
        assert fill_alpha_interface.fill_alpha == 0.25
        expression: str = expression_file_util.get_current_expression()
        assert 'fill' not in expression

        fill_alpha_interface.update_fill_alpha_and_skip_appending_exp(
            value=Number(value=0.5))
        assert fill_alpha_interface.fill_alpha == 0.5

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_fill_alpha_if_not_initialized(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        fill_alpha_interface._initialize_fill_alpha_if_not_initialized()
        assert fill_alpha_interface.fill_alpha == 1.0

        fill_alpha_interface.fill_alpha = Number(0.5)
        fill_alpha_interface._initialize_fill_alpha_if_not_initialized()
        assert fill_alpha_interface.fill_alpha == 0.5

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        fill_alpha_interface.fill_alpha = Number(0.5)
        snapshot_name: str = 'snapshot_1'
        fill_alpha_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            fill_alpha_interface._fill_alpha_snapshots[snapshot_name]
            == 0.5)

        fill_alpha_interface.fill_alpha = Number(0.3)
        fill_alpha_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert (
            fill_alpha_interface._fill_alpha_snapshots[snapshot_name]
            == 0.5)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        fill_alpha_interface: FillAlphaInterface = FillAlphaInterface()
        fill_alpha_interface.variable_name = 'test_fill_alpha_interface'
        fill_alpha_interface.fill_alpha = Number(0.5)
        snapshot_name: str = 'snapshot_1'
        fill_alpha_interface._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        fill_alpha_interface._fill_alpha = Number(0.3)
        fill_alpha_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert fill_alpha_interface.fill_alpha == 0.5
        assert (
            snapshot_name
            not in fill_alpha_interface._fill_alpha_snapshots)

        fill_alpha_interface._fill_alpha = Number(0.3)
        fill_alpha_interface._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert fill_alpha_interface.fill_alpha == 0.3
