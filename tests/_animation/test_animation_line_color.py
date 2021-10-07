from random import randint

from retrying import retry

import apysc as ap
from apysc._display.line_color_interface import LineColorInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationLineColor:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: LineColorInterface = LineColorInterface()
        target.variable_name = 'test_animation_line_color'
        animation: ap.AnimationLineColor = ap.AnimationLineColor(
            target=target,
            line_color='0af',
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation.variable_name.startswith(
            f'{var_names.ANIMATION_LINE_COLOR}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_line_color': '#00aaff',
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: LineColorInterface = LineColorInterface()
        target.variable_name = 'test_animation_line_color'
        animation: ap.AnimationLineColor = ap.AnimationLineColor(
            target=target,
            line_color='0af',
        )
        expression: str = animation._get_animation_func_expression()
        assert expression == (
            f'\n  .stroke({animation._line_color.variable_name});'
        )
