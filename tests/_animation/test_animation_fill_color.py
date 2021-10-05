from random import randint

from retrying import retry

import apysc as ap
from apysc._display.fill_color_interface import FillColorInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationFillColor:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: FillColorInterface = FillColorInterface()
        target.variable_name = 'test_animation_fill_color'
        animation_fill_color: ap.AnimationFillColor = ap.AnimationFillColor(
            target=target,
            fill_color='0af',
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_fill_color.variable_name.startswith(
            f'{var_names.ANIMATION_FILL_COLOR}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_fill_color': '#00aaff',
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_fill_color)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: FillColorInterface = FillColorInterface()
        target.variable_name = 'test_animation_fill_color'
        animation_fill_color: ap.AnimationFillColor = ap.AnimationFillColor(
            target=target, fill_color='0af')
        expression: str = animation_fill_color.\
            _get_animation_func_expression()
        assert expression == (
            '\n  .attr({fill: '
            f'{animation_fill_color._fill_color.variable_name}}});'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: FillColorInterface = FillColorInterface()
        target.variable_name = 'test_animation_fill_color'
        animation_fill_color: ap.AnimationFillColor = ap.AnimationFillColor(
            target=target, fill_color='0af')
        expression: str = animation_fill_color.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._fill_color.variable_name} = '
            f'{animation_fill_color._fill_color.variable_name};'
        )
