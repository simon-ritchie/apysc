import apysc as ap
from apysc._display.fill_alpha_mixin import FillAlphaMixIn
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import value_util


class TestFillAlphaMixIn:
    @apply_test_settings()
    def test_fill_alpha(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        fill_alpha_interface.fill_alpha = ap.Number(0.5)
        assert fill_alpha_interface.fill_alpha == 0.5

        fill_alpha: ap.Number = fill_alpha_interface.fill_alpha
        fill_alpha_name: str = fill_alpha.variable_name
        assert fill_alpha_name != fill_alpha_interface._fill_alpha.variable_name

    @apply_test_settings()
    def test__append_fill_alpha_update_expression(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        expression_data_util.empty_expression()
        fill_alpha_interface.fill_alpha = ap.Number(0.3)
        expression: str = expression_data_util.get_current_expression()
        value_str: str = value_util.get_value_str_for_expression(
            value=fill_alpha_interface._fill_alpha
        )
        expected: str = (
            f"{fill_alpha_interface.variable_name}" f".fill({{opacity: {value_str}}});"
        )
        assert expected in expression

    @apply_test_settings()
    def test__update_fill_alpha_and_skip_appending_exp(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        expression_data_util.empty_expression()
        fill_alpha_interface._update_fill_alpha_and_skip_appending_exp(value=0.25)
        assert fill_alpha_interface.fill_alpha == 0.25
        expression: str = expression_data_util.get_current_expression()
        assert "fill" not in expression

        fill_alpha_interface._update_fill_alpha_and_skip_appending_exp(
            value=ap.Number(value=0.5)
        )
        assert fill_alpha_interface.fill_alpha == 0.5

    @apply_test_settings()
    def test__initialize_fill_alpha_if_not_initialized(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        fill_alpha_interface._initialize_fill_alpha_if_not_initialized()
        assert fill_alpha_interface.fill_alpha == 1.0

        fill_alpha_interface.fill_alpha = ap.Number(0.5)
        fill_alpha_interface._initialize_fill_alpha_if_not_initialized()
        assert fill_alpha_interface.fill_alpha == 0.5

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        fill_alpha_interface.fill_alpha = ap.Number(0.5)
        snapshot_name: str = "snapshot_1"
        fill_alpha_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if fill_alpha_interface._fill_alpha_snapshots is None:
            raise AssertionError()
        assert fill_alpha_interface._fill_alpha_snapshots[snapshot_name] == 0.5

        fill_alpha_interface.fill_alpha = ap.Number(0.3)
        fill_alpha_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert fill_alpha_interface._fill_alpha_snapshots[snapshot_name] == 0.5

    @apply_test_settings()
    def test__revert(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        fill_alpha_interface.fill_alpha = ap.Number(0.5)
        snapshot_name: str = "snapshot_1"
        fill_alpha_interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        fill_alpha_interface._fill_alpha = ap.Number(0.3)
        fill_alpha_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert fill_alpha_interface.fill_alpha == 0.5

        fill_alpha_interface._fill_alpha = ap.Number(0.3)
        fill_alpha_interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert fill_alpha_interface.fill_alpha == 0.3

    @apply_test_settings()
    def test__append_fill_alpha_attr_linking_setting(self) -> None:
        fill_alpha_interface: FillAlphaMixIn = FillAlphaMixIn()
        fill_alpha_interface.variable_name = "test_fill_alpha_interface"
        fill_alpha_interface._initialize_fill_alpha_if_not_initialized()
        assert fill_alpha_interface._attr_linking_stack["fill_alpha"] == [
            ap.Number(1.0)
        ]
