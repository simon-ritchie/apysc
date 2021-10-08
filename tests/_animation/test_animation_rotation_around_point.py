from random import randint
from apysc._type.variable_name_interface import VariableNameInterface

from retrying import retry

import apysc as ap
from apysc._display.rotation_around_point_interface import \
    RotationAroundPointInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs, assert_raises


class TestAnimationRotationAroundPoint:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target_1: RotationAroundPointInterface = \
            RotationAroundPointInterface()
        target_1.variable_name = 'test_animation_rotation_around_point'
        animation: ap.AnimationRotationAroundPoint = \
            ap.AnimationRotationAroundPoint(
                target=target_1,
                rotation_around_point=100,
                x=200,
                y=300,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation.variable_name.startswith(
            f'{var_names.ANIMATION_ROTATION_AROUND_POINT}_')
        assert_attrs(
            expected_attrs={
                '_target': target_1,
                '_rotation_around_point': 100,
                '_x': 200,
                '_y': 300,
                '_before_rotation_around_point': 0,
                '_rotation_around_point_diff': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation)

        target_2: VariableNameInterface = VariableNameInterface()
        target_2.variable_name = 'test_animation_rotation_around_point'
        assert_raises(
            expected_error_class=TypeError,
            func_or_method=ap.AnimationRotationAroundPoint,
            kwargs={
                'target': target_2,
                'rotation_around_point': 100,
                'x': 200,
                'y': 300,
            },
            match='Specified `target` argument is not a '
                  'RotationAroundPointInterface')
