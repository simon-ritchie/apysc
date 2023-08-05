import apysc as ap
from apysc._display.line_color_mixin import LineColorMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs


class TestAnimationLineColor:
    @apply_test_settings()
    def test___init__(self) -> None:
        target: LineColorMixIn = LineColorMixIn()
        target.variable_name = "test_animation_line_color"
        animation: ap.AnimationLineColor = ap.AnimationLineColor(
            target=target,
            line_color=ap.Color("0af"),
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation.variable_name.startswith(f"{var_names.ANIMATION_LINE_COLOR}_")
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_line_color": ap.Color("#00aaff"),
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation,
        )

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        target: LineColorMixIn = LineColorMixIn()
        target.variable_name = "test_animation_line_color"
        animation: ap.AnimationLineColor = ap.AnimationLineColor(
            target=target,
            line_color=ap.Color("0af"),
        )
        expression: str = animation._get_animation_func_expression()
        assert expression == (
            f"\n  .stroke({animation._line_color._value.variable_name});"
        )

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: LineColorMixIn = LineColorMixIn()
        target.variable_name = "test_animation_line_color"
        animation: ap.AnimationLineColor = ap.AnimationLineColor(
            target=target,
            line_color=ap.Color("0af"),
        )
        expression: str = animation._get_complete_event_in_handler_head_expression()
        assert expression == (
            f"{target._line_color._value.variable_name} = "
            f"{animation._line_color._value.variable_name};"
        )
