from random import randint

from retrying import retry

import apysc as ap
from apysc._expression import var_names
from apysc._type.variable_name_mixin import VariableNameMixIn
from apysc._testing.testing_helper import apply_test_settings


class TestAnimationEvent:
    @apply_test_settings()
    def test___init__(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_event"
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target, x=50, y=100, duration=1000
        )
        animation_event: ap.AnimationEvent = ap.AnimationEvent(this=animation_move)
        assert animation_event._this == animation_move
        assert animation_event.variable_name.startswith(f"{var_names.ANIMATION_EVENT}_")

    @apply_test_settings()
    def test_this(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_event"
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target, x=50, y=100, duration=1000
        )
        animation_event: ap.AnimationEvent = ap.AnimationEvent(this=animation_move)
        assert animation_event.this == animation_move
