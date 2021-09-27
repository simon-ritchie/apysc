from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationHeightForEllipse:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_height_for_ellipse'
        animation_height_for_ellipse: ap.AnimationHeightForEllipse = \
            ap.AnimationHeightForEllipse(
                target=target,
                height=100, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_height_for_ellipse.variable_name.startswith(
            f'{var_names.ANIMATION_HEIGHT_FOR_ELLIPSE}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_height': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_height_for_ellipse)

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_height_for_ellipse'
        animation_height_for_ellipse: ap.AnimationHeightForEllipse = \
            ap.AnimationHeightForEllipse(target=target, height=100)
        expression: str = animation_height_for_ellipse.\
            _get_animation_func_expression()
        assert expression == (
            '\n  .attr({ry: parseInt'
            f'({animation_height_for_ellipse._height.variable_name} / 2)}});')
