from random import randint

from retrying import retry

import apysc as ap
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import var_names
from tests.testing_helper import assert_attrs


class TestAnimationEllipseWidth:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: VariableNameInterface = VariableNameInterface()
        target.variable_name = 'test_animation_ellipse_width'
        animation_ellipse_width: ap.AnimationEllipseWidth = \
            ap.AnimationEllipseWidth(
                target=target,
                ellipse_width=100,
                duration=1000,
                delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_ellipse_width.variable_name.startswith(
            f'{var_names.ANIMATION_ELLIPSE_WIDTH}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_ellipse_width': 100,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_ellipse_width,
        )
