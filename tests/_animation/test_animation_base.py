import re
from random import randint
from typing import List
from typing import Match
from typing import Optional, Dict, Any

from retrying import retry

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._type.variable_name_interface import VariableNameInterface
from apysc._event.custom_event_type import CustomEventType


class _TestAnimation(AnimationBase):

    def __init__(self) -> None:
        """
        The class for the testing of the AnimationBase.
        """
        super(_TestAnimation, self).__init__(
            variable_name='test_animation_base')

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
    def test_start(self) -> None:
        expression_data_util.empty_expression()
        animation: _TestAnimation = _TestAnimation()
        instance: VariableNameInterface = VariableNameInterface()
        instance.variable_name = 'test_animation_base'
        animation._set_basic_animation_settings(
            instance=instance,
            duration=3000, delay=1000,
            easing=ap.Easing.EASE_OUT_QUINT)
        animation.start()
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            rf'{animation._instance.variable_name}',
            r'\n  \.animate\({',
            rf'\n    duration: {var_names.INT}_.+?,',
            rf'\n    delay: {var_names.INT}_.+?}}\)',
            r'\n  \.ease\(.+?\)',
            r'\n  \.move\(100, 200\);',
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern, string=expression,
                flags=re.MULTILINE | re.DOTALL)
            assert match is not None, f'{expected_pattern} \n\n{expression}'
        assert animation._started == True

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

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        assert animation.variable_name == 'test_animation_base'
        assert animation._started == False

    def on_animation_complete_1(
            self, e: ap.AnimationEvent, options: Dict[str, Any]) -> None:
        """
        The handler will be called when the animation is completed.

        Parameters
        ----------
        e : ap.AnimationEvent
            Event instance.
        options : dict
            Optional argument dictionary.
        """
        assert options['value'] == 10

    def on_animation_complete_2(
            self, e: ap.AnimationEvent, options: Dict[str, Any]) -> None:
        """
        The handler will be called when the animation is completed.

        Parameters
        ----------
        e : ap.AnimationEvent
            Event instance.
        options : dict
            Optional argument dictionary.
        """

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_animation_complete(self) -> None:
        expression_data_util.empty_expression()
        animation: _TestAnimation = _TestAnimation()
        handler_name: str = animation.animation_complete(
            handler=self.on_animation_complete_1,
            options={'value': 10})
        event_type: str = CustomEventType.ANIMATION_COMPLETE.value
        assert animation._custom_event_handlers[
            event_type][handler_name]['handler'] \
                == self.on_animation_complete_1
        assert animation._custom_event_handlers[
            event_type][handler_name]['options'] == {'value': 10}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_animation_complete_handler_expression(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        expression: str = \
            animation._get_animation_complete_handler_expression()
        assert expression == ''

        handler_name_1: str = animation.animation_complete(
            handler=self.on_animation_complete_1, options={'value': 10})
        handler_name_2: str = animation.animation_complete(
            handler=self.on_animation_complete_2)
        expression = animation._get_animation_complete_handler_expression()
        assert f'\n  .attr({handler_name_1})'
        assert f'\n  .attr({handler_name_2})'
