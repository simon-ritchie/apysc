import re
from typing import Any
from typing import Dict
from typing import List
from typing import Match
from typing import Optional

import apysc as ap
from apysc._animation.animation_base import AnimationBase
from apysc._event.custom_event_type import CustomEventType
from apysc._event.handler import get_handler_name
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestAnimation(AnimationBase):
    def __init__(self) -> None:
        """
        The class for the testing of the AnimationBase.
        """
        super(_TestAnimation, self).__init__(variable_name="test_animation_base")

    def _get_animation_func_expression(self) -> str:
        """
        Get a animation function expression.

        Returns
        -------
        expression : str
            Animation function expression.
        """
        return "\n  .move(100, 200);"

    def _get_complete_event_in_handler_head_expression(self) -> str:
        """
        Get an expression to be inserted into the complete event
        handler's head.

        Returns
        -------
        expression : str
            An expression to be inserted into the complete event
            handler's head.
        """
        return ""


class TestAnimationBase:
    @apply_test_settings()
    def test__set_basic_animation_settings(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_base"
        animation._set_basic_animation_settings(
            target=target, duration=3000, delay=1000, easing=ap.Easing.EASE_OUT_QUINT
        )
        assert animation._duration == 3000
        assert isinstance(animation._duration, ap.Int)
        assert animation._delay == 1000
        assert isinstance(animation._delay, ap.Int)
        assert animation._easing == ap.Easing.EASE_OUT_QUINT

    @apply_test_settings()
    def test_start(self) -> None:
        ap.Stage()
        animation: _TestAnimation = _TestAnimation()
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_base"
        animation._set_basic_animation_settings(
            target=target, duration=3000, delay=1000, easing=ap.Easing.EASE_OUT_QUINT
        )
        self_instance: ap.AnimationBase = animation.start()
        assert isinstance(self_instance, _TestAnimation)
        expression: str = expression_data_util.get_current_expression()
        expected_patterns: List[str] = [
            rf"{animation._target.variable_name}",
            r"\n  \.animate\({",
            rf"\n    duration: {var_names.INT}_.+?,",
            rf"\n    delay: {var_names.INT}_.+?}}\)",
            r"\n  \.ease\(.+?\)",
            r"\n  \.move\(100, 200\);",
        ]
        for expected_pattern in expected_patterns:
            match: Optional[Match] = re.search(
                pattern=expected_pattern,
                string=expression,
                flags=re.MULTILINE | re.DOTALL,
            )
            assert match is not None, f"{expected_pattern} \n\n{expression}"
        assert animation._started

        ap.Stage()
        animation = _TestAnimation()
        animation._set_basic_animation_settings(
            target=target, duration=3000, delay=1000, easing=ap.Easing.EASE_OUT_QUINT
        )
        expression = expression_data_util.get_current_expression()
        assert ".ease(" not in expression

    @apply_test_settings()
    def test___init__(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        assert animation.variable_name == "test_animation_base"
        assert not animation._started

    def on_animation_complete_1(
        self, e: ap.AnimationEvent, options: Dict[str, Any]
    ) -> None:
        """
        The handler will be called when the animation is completed.

        Parameters
        ----------
        e : ap.AnimationEvent
            Event instance.
        options : dict
            Optional argument dictionary.
        """
        assert options["value"] == 10

    def on_animation_complete_2(
        self, e: ap.AnimationEvent, options: Dict[str, Any]
    ) -> None:
        """
        The handler will be called when the animation is completed.

        Parameters
        ----------
        e : ap.AnimationEvent
            Event instance.
        options : dict
            Optional argument dictionary.
        """

    @apply_test_settings()
    def test_animation_complete(self) -> None:
        ap.Stage()
        animation: _TestAnimation = _TestAnimation()
        self_instance: AnimationBase = animation.animation_complete(
            handler=self.on_animation_complete_1, options={"value": 10}
        )
        assert isinstance(self_instance, _TestAnimation)
        handler_name: str = get_handler_name(
            handler=self.on_animation_complete_1, instance=animation
        )
        event_type: str = CustomEventType.ANIMATION_COMPLETE.value
        assert (
            animation._custom_event_handlers[event_type][handler_name].handler
            == self.on_animation_complete_1
        )
        assert animation._custom_event_handlers[event_type][handler_name].options == {
            "value": 10
        }

        animation.animation_complete(
            self.on_animation_complete_1, options={"value": 10}
        )

    @apply_test_settings()
    def test__get_animation_complete_handler_expression(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        expression: str = animation._get_animation_complete_handler_expression()
        assert expression == ""

        _ = animation.animation_complete(
            handler=self.on_animation_complete_1, options={"value": 10}
        )
        _ = animation.animation_complete(handler=self.on_animation_complete_2)
        handler_name_1: str = get_handler_name(
            handler=self.on_animation_complete_1, instance=animation
        )
        handler_name_2: str = get_handler_name(
            handler=self.on_animation_complete_2, instance=animation
        )
        expression = animation._get_animation_complete_handler_expression()
        assert f"\n  .after({handler_name_1})"
        assert f"\n  .after({handler_name_2})"

    @apply_test_settings()
    def test__validate_animation_not_started(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        target_1: VariableNameMixIn = VariableNameMixIn()
        target_1.variable_name = "test_animation_base_1"
        animation._set_basic_animation_settings(target=target_1, duration=1000)
        animation.animation_complete(handler=self.on_animation_complete_2)

        animation.start()
        assert_raises(
            expected_error_class=Exception,
            callable_=animation.animation_complete,
            kwargs={"handler": self.on_animation_complete_2},
        )

    @apply_test_settings()
    def test_target(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_base_1"
        animation._set_basic_animation_settings(target=target, duration=1000)
        assert animation.target == target

    @apply_test_settings()
    def test__get_animation_basic_expression(self) -> None:
        animation: _TestAnimation = _TestAnimation()
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_base"
        animation._target = target
        animation._duration = ap.Int(1000)
        animation._delay = ap.Int(0)
        animation._easing = ap.Easing.EASE_OUT_QUINT
        animation.animation_complete(self.on_animation_complete_2)
        expression: str = animation._get_animation_basic_expression()
        expected_strs: List[str] = [
            f"{target.variable_name}",
            "\n  .animate({",
            f"\n    duration: {animation._duration.variable_name},",
            f"\n    delay: {animation._delay.variable_name}}})"
            f"\n  .ease({animation._easing.value})"
            "\n  .after(",
        ]
        for expected in expected_strs:
            assert expected in expression
