from apysc._expression import expression_data_util
from random import randint
from typing import List, Match, Optional, Union
import re

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._animation.animation_base import AnimationBase


class _TestAnimation(AnimationBase):

    def __init__(
            self,
            duration: Union[int, ap.Int],
            delay: Union[int, ap.Int] = 0,
            easing: Optional[ap.Easing] = None) -> None:
        """
        Class for the testing of the AnimationBase.

        Parameters
        ----------
        duration : int or Int
            Milliseconds before an animation ends.
        delay : int or Int, default 0
            Milliseconds before an animation starts.
        easing : Easing or None, default None
            Easing setting. If None, Linear calculation is used.
        """
        self.variable_name = 'test_animation_base'
        super(_TestAnimation, self).__init__(
            duration=duration, delay=delay, easing=easing,
        )

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        return '\n  .move(100, 200);'


class TestAnimationBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        animation: _TestAnimation = _TestAnimation(
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation._duration == 3000
        assert isinstance(animation._duration, ap.Int)
        assert animation._delay == 1000
        assert isinstance(animation._delay, ap.Int)
        assert animation._easing == ap.Easing.EASE_OUT_QUINT

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_start(self) -> None:
        expression_data_util.empty_expression()
        animation: _TestAnimation = _TestAnimation(
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        animation.start()
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            rf'{animation.variable_name}',
            r'\n  \.animate\({',
            rf'\n    duration: {var_names.INT}_.+?,',
            rf'\n    delay: {var_names.INT}_.+?}}\)',
            rf'\n  \.ease\(.+?\)',
            rf'\n  \.move\(100, 200\);',
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern, string=expression,
                flags=re.MULTILINE | re.DOTALL)
            assert match is not None, f'{expected_pattern} \n\n{expression}'
