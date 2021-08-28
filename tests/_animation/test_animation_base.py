from apysc._type.variable_name_interface import VariableNameInterface
from apysc._expression import expression_data_util
from random import randint
from typing import List, Match, Optional, Union
import re

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._animation.animation_base import AnimationBase


class _TestAnimation(AnimationBase):

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
    def test__set_basic_animation_settings(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_animation_base'
        animation._set_basic_animation_settings(
            instance=instance,
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        assert animation._duration == 3000
        assert isinstance(animation._duration, ap.Int)
        assert animation._delay == 1000
        assert isinstance(animation._delay, ap.Int)
        assert animation._easing == ap.Easing.EASE_OUT_QUINT

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__append_animation_start_expression(self) -> None:
        expression_data_util.empty_expression()
        animation: _TestAnimation = _TestAnimation()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_animation_base'
        animation._set_basic_animation_settings(
            instance=instance,
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        animation._append_animation_start_expression()
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            rf'{animation._instance.variable_name}',
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

        expression_data_util.empty_expression()
        animation = _TestAnimation()
        animation._set_basic_animation_settings(
            instance=instance,
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        expression = expression_data_util.get_current_expression()
        assert '.ease(' not in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_animation_base'
        animation._set_basic_animation_settings(
            instance=instance,
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        snapshot_name: str = animation._get_next_snapshot_name()
        animation._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert animation._instance_snapshots[snapshot_name] == instance
        assert animation._duration_snapshots[snapshot_name] == 3000
        assert animation._delay_snapshots[snapshot_name] == 1000
        assert animation._easing_snapshots[snapshot_name] == \
            ap.Easing.EASE_OUT_QUINT

        animation._duration = ap.Int(5000)
        animation._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert animation._duration_snapshots[snapshot_name] == 3000

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        instance_1: VariableNameInterface = VariableNameInterface()
        instance_1.variable_name = 'test_animation_base_1'
        animation._set_basic_animation_settings(
            instance=instance_1,
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        snapshot_name: str = animation._get_next_snapshot_name()
        instance_2: VariableNameInterface = VariableNameInterface()
        instance_2.variable_name = 'test_animation_base_2'
        animation._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        animation._instance = instance_2
        animation._duration = ap.Int(5000)
        animation._delay = ap.Int(1500)
        animation._easing = None
        animation._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation._instance == instance_1
        assert animation._duration == 3000
        assert animation._delay == 1000
        assert animation._easing == ap.Easing.EASE_OUT_QUINT

        animation._instance = instance_2
        animation._duration = ap.Int(5000)
        animation._delay = ap.Int(1500)
        animation._easing = None
        animation._run_all_revert_methods(snapshot_name=snapshot_name)
        assert animation._instance == instance_2
        assert animation._duration == 5000
        assert animation._delay == 1500
        assert animation._easing is None
