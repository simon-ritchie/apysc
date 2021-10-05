from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_x_interface import SkewXInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationSkewX:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: SkewXInterface = SkewXInterface()
        target.variable_name = 'test_animation_skew_x'
        animation_skew_x: ap.AnimationSkewX = ap.AnimationSkewX(
            target=target,
            skew_x=30,
            before_skew_x=ap.Int(10),
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_skew_x.variable_name.startswith(
            f'{var_names.ANIMATION_SKEW_X}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_skew_x': 30,
                '_before_skew_x': 10,
                '_skew_x_diff': 20,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_skew_x,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: SkewXInterface = SkewXInterface()
        target.variable_name = 'test_animation_skew_x'
        animation_skew_x: ap.AnimationSkewX = ap.AnimationSkewX(
            target=target,
            skew_x=30,
            before_skew_x=ap.Int(10),
        )
        expression: str = animation_skew_x._get_animation_func_expression()
        assert expression == (
            '\n  .attr({"skewX": '
            f'{animation_skew_x._skew_x_diff.variable_name}}});'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: SkewXInterface = SkewXInterface()
        target.variable_name = 'test_animation_skew_x'
        animation_skew_x: ap.AnimationSkewX = ap.AnimationSkewX(
            target=target,
            skew_x=30,
            before_skew_x=ap.Int(10),
        )
        expression: str = animation_skew_x.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._skew_x.variable_name} = '
            f'{animation_skew_x._skew_x.variable_name};'
        )
