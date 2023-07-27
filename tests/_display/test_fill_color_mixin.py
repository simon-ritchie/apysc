import apysc as ap
from apysc._display.fill_color_mixin import FillColorMixIn
from apysc._expression import expression_data_util, var_names
from apysc._testing.testing_helper import apply_test_settings


class TestFillColorMixIn:
    @apply_test_settings()
    def test_fill_color(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        color_1: ap.Color = ap.Color("#333")
        fill_color_mixin.fill_color = color_1
        assert fill_color_mixin.fill_color._value == ap.String("#333333")

        color_2: ap.Color = fill_color_mixin.fill_color
        assert color_1._value.variable_name != color_2._value.variable_name

    @apply_test_settings()
    def test__append_fill_color_update_expression(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        color: ap.Color = ap.Color("#333")
        fill_color_mixin.fill_color = color
        expression: str = expression_data_util.get_current_expression()
        expected: str = f'test_fill_color_mixin.fill({var_names.STRING}_'
        assert expected in expression

    @apply_test_settings()
    def test__update_fill_color_and_skip_appending_exp(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        color: ap.Color = ap.Color("#333")
        fill_color_mixin._update_fill_color_and_skip_appending_exp(
            value=color
        )
        assert fill_color_mixin.fill_color._value == ap.String("#333333")
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"{fill_color_mixin.variable_name}.fill("
        assert expected not in expression

    @apply_test_settings()
    def test__initialize_fill_color_if_not_initialized(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        fill_color_mixin._initialize_fill_color_if_not_initialized()
        assert fill_color_mixin.fill_color == ap.COLORLESS
        fill_color_mixin.fill_color = ap.Color("333")
        fill_color_mixin._initialize_fill_color_if_not_initialized()
        assert fill_color_mixin.fill_color._value == ap.String("#333333")

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        fill_color_mixin.fill_color = ap.Color("#333333")
        snapshot_name: str = "snapshot_1"
        fill_color_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if fill_color_mixin._fill_color_snapshots is None:
            raise AssertionError()
        assert fill_color_mixin._fill_color_snapshots[snapshot_name] == "#333333"

        fill_color_mixin.fill_color = ap.Color("#222222")
        fill_color_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert fill_color_mixin._fill_color_snapshots[snapshot_name] == "#333333"

    @apply_test_settings()
    def test__revert(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        fill_color_mixin.fill_color = ap.Color("#333333")
        snapshot_name: str = "snapshot_1"
        fill_color_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        fill_color_mixin.fill_color = ap.Color("#222222")
        fill_color_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert fill_color_mixin.fill_color._value == ap.String("#333333")

        fill_color_mixin.fill_color = ap.Color("#222222")
        fill_color_mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert fill_color_mixin.fill_color._value == ap.String("#222222")

    @apply_test_settings()
    def test__set_initial_fill_color_if_not_blank(self) -> None:
        fill_color_mixin: FillColorMixIn = FillColorMixIn()
        fill_color_mixin.variable_name = "test_fill_color_mixin"
        fill_color_mixin._set_initial_fill_color_if_not_blank(fill_color=ap.COLORLESS)
        assert fill_color_mixin.fill_color == ap.COLORLESS
        fill_color_mixin._set_initial_fill_color_if_not_blank(fill_color=ap.Color("#0af"))
        assert fill_color_mixin.fill_color._value == ap.String("#00aaff")
