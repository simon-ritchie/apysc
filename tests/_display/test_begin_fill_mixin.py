import apysc as ap
from apysc._display.begin_fill_mixin import BeginFillMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestBeginFillMixIn:
    @apply_test_settings()
    def test_begin_fill(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin._fill_color = ap.COLORLESS
        begin_fill_mixin._fill_alpha = ap.Number(1.0)
        begin_fill_mixin.begin_fill(color=ap.Color("#333"))
        assert begin_fill_mixin.fill_color == ap.Color("#333333")
        assert begin_fill_mixin.fill_alpha == 1.0

        begin_fill_mixin.begin_fill(color=ap.Color("#333"), alpha=0.5)
        assert begin_fill_mixin.fill_alpha == 0.5

        begin_fill_mixin.begin_fill(color=ap.Color("#333"), alpha=ap.Number(value=0.3))
        assert begin_fill_mixin.fill_color == ap.Color("#333333")
        assert begin_fill_mixin.fill_alpha == 0.3

        begin_fill_mixin.begin_fill(color=ap.COLORLESS)
        assert begin_fill_mixin.fill_color == ap.COLORLESS

    @apply_test_settings()
    def test_fill_color(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin._fill_color = ap.COLORLESS
        begin_fill_mixin._fill_alpha = ap.Number(1.0)
        begin_fill_mixin.begin_fill(color=ap.Color("#333"))
        assert begin_fill_mixin.fill_color._value == ap.Color("#333333")

        fill_color_1: ap.Color = begin_fill_mixin.fill_color
        assert (
            fill_color_1._value.variable_name
            != begin_fill_mixin.fill_color._value.variable_name
        )

    @apply_test_settings()
    def test_fill_alpha(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin._fill_color = ap.COLORLESS
        begin_fill_mixin._fill_alpha = ap.Number(1.0)
        begin_fill_mixin.begin_fill(color=ap.Color("#333"), alpha=0.2)
        assert begin_fill_mixin.fill_alpha == 0.2

        fill_alpha_1: ap.Number = begin_fill_mixin.fill_alpha
        assert fill_alpha_1.variable_name != begin_fill_mixin.fill_alpha.variable_name

    @apply_test_settings()
    def test__initialize_fill_color_if_not_initialized(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin._initialize_fill_color_if_not_initialized()
        assert begin_fill_mixin.fill_color == ap.COLORLESS

        begin_fill_mixin._fill_color = ap.Color("#333333")
        begin_fill_mixin._initialize_fill_color_if_not_initialized()
        assert begin_fill_mixin.fill_color == ap.Color("#333333")

    @apply_test_settings()
    def test__initialize_fill_alpha_if_not_initialized(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin._initialize_fill_alpha_if_not_initialized()
        assert begin_fill_mixin.fill_alpha == 1.0

        begin_fill_mixin._fill_alpha = ap.Number(0.5)
        begin_fill_mixin._initialize_fill_alpha_if_not_initialized()
        assert begin_fill_mixin.fill_alpha == 0.5

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin.begin_fill(color=ap.Color("#333333"), alpha=0.5)
        snapshot_name_1: str = begin_fill_mixin._get_next_snapshot_name()
        begin_fill_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name_1)
        if begin_fill_mixin._fill_color_snapshots is None:
            raise AssertionError()
        assert begin_fill_mixin._fill_color_snapshots[snapshot_name_1] == "#333333"
        if begin_fill_mixin._fill_alpha_snapshots is None:
            raise AssertionError()
        assert begin_fill_mixin._fill_alpha_snapshots[snapshot_name_1] == 0.5
        assert begin_fill_mixin._snapshot_exists(snapshot_name=snapshot_name_1)

        begin_fill_mixin._fill_color._value._value = "#222222"
        begin_fill_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name_1)
        assert begin_fill_mixin._fill_color_snapshots[snapshot_name_1] == "#333333"

    @apply_test_settings()
    def test__revert(self) -> None:
        begin_fill_mixin: BeginFillMixIn = BeginFillMixIn()
        begin_fill_mixin.begin_fill(color=ap.Color("#333333"), alpha=0.5)
        snapshot_name_1: str = begin_fill_mixin._get_next_snapshot_name()
        begin_fill_mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name_1)
        begin_fill_mixin.begin_fill(color=ap.Color("#222222"), alpha=0.3)
        begin_fill_mixin._run_all_revert_methods(snapshot_name=snapshot_name_1)
        assert begin_fill_mixin.fill_color == ap.Color("#333333")
        assert begin_fill_mixin.fill_alpha == 0.5

        begin_fill_mixin.begin_fill(color=ap.Color("#222222"), alpha=0.3)
        begin_fill_mixin._run_all_revert_methods(snapshot_name=snapshot_name_1)
        assert begin_fill_mixin.fill_color == ap.Color("#222222")
