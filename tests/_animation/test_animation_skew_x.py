from random import randint

from retrying import retry

import apysc as ap
from apysc._display.skew_x_interface import SkewXInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs, assert_raises
from apysc._type.variable_name_interface import VariableNameInterface


class TestAnimationSkewX:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: SkewXInterface = SkewXInterface()
        target_1.variable_name = 'test_animation_skew_x'
        target_1._skew_x = ap.Int(10)
        animation_skew_x: ap.AnimationSkewX = ap.AnimationSkewX(
            target=target_1,
            skew_x=30,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_skew_x.variable_name.startswith(
            f'{var_names.ANIMATION_SKEW_X}_')
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_skew_x': 30,
                '_before_skew_x': 10,
                '_skew_x_diff': 20,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_skew_x,
        )

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_skew_x'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationSkewX,
            kwargs={
                'target': target_2,
                'skew_x': 50,
            },
            match='Specified `target` argument is not a SkewXInterface',
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: SkewXInterface = SkewXInterface()
        target.variable_name = 'test_animation_skew_x'
        target._skew_x = ap.Int(10)
        animation_skew_x: ap.AnimationSkewX = ap.AnimationSkewX(
            target=target,
            skew_x=30,
        )
        expression: str = animation_skew_x._get_animation_func_expression()
        assert expression == (
            f'\n  .skew({animation_skew_x._skew_x_diff.variable_name}, 0);'
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: SkewXInterface = SkewXInterface()
        target._skew_x = ap.Int(10)
        target.variable_name = 'test_animation_skew_x'
        animation_skew_x: ap.AnimationSkewX = ap.AnimationSkewX(
            target=target,
            skew_x=30,
        )
        expression: str = animation_skew_x.\
            _get_complete_event_in_handler_head_expression()
        assert expression == (
            f'{target._skew_x.variable_name} = '
            f'{animation_skew_x._skew_x.variable_name};'
        )
