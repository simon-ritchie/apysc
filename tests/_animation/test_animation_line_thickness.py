from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from tests.testing_helper import assert_attrs
from apysc._display.line_thickness_interface import LineThicknessInterface


class TestAnimationLineThickness:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        target: LineThicknessInterface = LineThicknessInterface()
        target.variable_name = 'test_line_thickness_interface'
        animation_line_thickness: ap.AnimationLineThickness = \
            ap.AnimationLineThickness(
                target=target, thickness=3, duration=1000, delay=500,
                easing=ap.Easing.EASE_OUT_QUINT)
        assert animation_line_thickness.variable_name.startswith(
            f'{var_names.ANIMATION_LINE_THICKNESS}_')
        assert_attrs(
            expected_attrs={
                '_target': target,
                '_line_thickness': 3,
                '_duration': 1000,
                '_delay': 500,
                '_easing': ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_line_thickness)
