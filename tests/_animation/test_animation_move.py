import apysc as ap
from apysc._display.x_mixin import XMixIn
from apysc._display.y_mixin import YMixIn
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.variable_name_mixin import VariableNameMixIn


class _TestInterface(XMixIn, YMixIn):
    pass


class TestAnimationMove:
    @apply_test_settings()
    def test___init__(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_move_interface"
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target,
            x=100,
            y=200,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_move._x == 100
        assert isinstance(animation_move._x, ap.Number)
        assert animation_move._y == 200
        assert isinstance(animation_move._y, ap.Number)

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_move_interface"
        animation_move: ap.AnimationMove = ap.AnimationMove(
            target=target, x=100, y=200, duration=1000
        )
        expression: str = animation_move._get_animation_func_expression()
        expected: str = (
            f"\n  .move({animation_move._x.variable_name}, "
            f"{animation_move._y.variable_name});"
        )
        assert expression == expected

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: _TestInterface = _TestInterface()
        target.variable_name = "test_animation_move_interface"
        animation_move: ap.AnimationMove = ap.AnimationMove(target=target, x=100, y=200)
        expression: str = (
            animation_move._get_complete_event_in_handler_head_expression()
        )
        assert expression == (
            f"{target._x.variable_name} = "
            f"{animation_move._x.variable_name};"
            f"\n{target._y.variable_name} = "
            f"{animation_move._y.variable_name};"
        )
