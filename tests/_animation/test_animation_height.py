import apysc as ap
from apysc._display.height_mixin import HeightMixIn
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from apysc._type.variable_name_mixin import VariableNameMixIn


class TestAnimationHeight:
    @apply_test_settings()
    def test___init__(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_height"
        animation_height: ap.AnimationHeight = ap.AnimationHeight(
            target=target,
            height=100,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert animation_height.variable_name.startswith(
            f"{var_names.ANIMATION_HEIGHT}_"
        )
        assert_attrs(
            expected_attrs={
                "_target": target,
                "_height": 100,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_height,
        )

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        target: VariableNameMixIn = VariableNameMixIn()
        target.variable_name = "test_animation_height"
        animation_height: ap.AnimationHeight = ap.AnimationHeight(
            target=target, height=100
        )
        expression: str = animation_height._get_animation_func_expression()
        assert expression == (f"\n  .height({animation_height._height.variable_name});")

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        target: HeightMixIn = HeightMixIn()
        target.variable_name = "test_animation_height"
        animation_height: ap.AnimationHeight = ap.AnimationHeight(
            target=target, height=100
        )
        expression: str = (
            animation_height._get_complete_event_in_handler_head_expression()
        )
        assert expression == (
            f"{target._height.variable_name} = "
            f"{animation_height._height.variable_name};"
        )
