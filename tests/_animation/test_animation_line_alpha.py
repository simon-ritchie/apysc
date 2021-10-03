from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._animation.animation_line_alpha import AnimationLineAlpha
from apysc._display.line_alpha_interface import LineAlphaInterface
from tests.testing_helper import assert_attrs


class TestAnimationLineAlpha:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: LineAlphaInterface = LineAlphaInterface()
        target.variable_name = 'test_line_alpha_interface'
        animation_line_alpha: ap.AnimationLineAlpha = ap.AnimationLineAlpha(
            target=target, alpha=0.5, duration=1000, delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_line_alpha.variable_name.startswith(
            f'{var_names.ANIMATION_LINE_ALPHA}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_line_alpha': 0.5,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_alpha)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: LineAlphaInterface = LineAlphaInterface()
        target.variable_name = 'test_line_alpha_interface'
        animation_line_alpha: ap.AnimationLineAlpha = ap.AnimationLineAlpha(
            target=target, alpha=0.5)
        expression: str = animation_line_alpha.\
            _get_animation_func_expression()
        assert expression == (
            '\n  .attr({"stroke-opacity": '
            f'{animation_line_alpha._line_alpha.variable_name}}});'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: LineAlphaInterface = LineAlphaInterface()
        target.variable_name = 'test_line_alpha_interface'
        animation_line_alpha: ap.AnimationLineAlpha = ap.AnimationLineAlpha(
            target=target, alpha=0.5)
        expression: str = animation_line_alpha.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._line_alpha.variable_name} = '
            f'{animation_line_alpha._line_alpha.variable_name};'
        )
