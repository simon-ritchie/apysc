from typing import List

import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_attrs
from apysc._testing.testing_helper import assert_raises


class TestAnimationParallel:
    @apply_test_settings()
    def test___init__(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
            rectangle.animation_y(y=100),
        ]
        animation_parallel: ap.AnimationParallel = rectangle.animation_parallel(
            animations=animations,
            duration=1000,
            delay=500,
            easing=ap.Easing.EASE_OUT_QUINT,
        )
        assert_attrs(
            expected_attrs={
                "_target": rectangle,
                "_animations": animations,
                "_duration": 1000,
                "_delay": 500,
                "_easing": ap.Easing.EASE_OUT_QUINT,
            },
            any_obj=animation_parallel,
        )
        assert animation_parallel.variable_name.startswith(
            f"{var_names.ANIMATION_PARALLEL}_"
        )

    @apply_test_settings()
    def test__get_animation_func_expression(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animation_x: ap.AnimationX = rectangle.animation_x(x=100)
        animation_y: ap.AnimationY = rectangle.animation_y(y=100)
        animation_fill_color: ap.AnimationFillColor = rectangle.animation_fill_color(
            fill_color="#0af"
        )
        animations: List[ap.AnimationBase] = [
            animation_x,
            animation_y,
            animation_fill_color,
        ]
        animation_parallel: ap.AnimationParallel = rectangle.animation_parallel(
            animations=animations
        )
        expression: str = animation_parallel._get_animation_func_expression()
        expected: str = (
            f"\n  .x({animation_x._x.variable_name})"
            f"\n  .y({animation_y._y.variable_name})"
            "\n  .attr({\n    "
            f"fill: {animation_fill_color._fill_color.variable_name}\n  }});"
        )
        assert expression == expected

    @apply_test_settings()
    def test__get_complete_event_in_handler_head_expression(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
            rectangle.animation_y(y=100),
        ]
        animation_parallel: ap.AnimationParallel = rectangle.animation_parallel(
            animations=animations
        )
        expression: str = (
            animation_parallel._get_complete_event_in_handler_head_expression()
        )
        expected_strs: List[str] = [
            f"{rectangle._x.variable_name} = ",
            f"{rectangle._y.variable_name} = ",
        ]
        for expected in expected_strs:
            assert expected in expression

    @apply_test_settings()
    def test__validate_animation_targets_are_unified(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations: List[ap.AnimationBase] = [
            rectangle_1.animation_x(x=100),
            rectangle_1.animation_y(y=100),
        ]
        rectangle_1.animation_parallel(animations=animations)

        rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations = [
            rectangle_1.animation_x(x=100),
            rectangle_2.animation_y(y=100),
        ]
        assert_raises(
            expected_error_class=ValueError,
            callable_=rectangle_1.animation_parallel,
            match="There is not unified animation target instance:",
            animations=animations,
        )

    @apply_test_settings()
    def test__validate_animations_duration_are_default_vals(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
        ]
        rectangle.animation_parallel(animations=animations)

        animations = [
            rectangle.animation_x(x=100, duration=3200),
        ]
        assert_raises(
            expected_error_class=ValueError,
            callable_=rectangle.animation_parallel,
            match=("There is an animation target that is changed " "duration setting:"),
            animations=animations,
        )

    @apply_test_settings()
    def test__validate_animations_delay_are_default_vals(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
        ]
        rectangle.animation_parallel(animations=animations)

        animations = [
            rectangle.animation_x(x=100, delay=500),
        ]
        assert_raises(
            expected_error_class=ValueError,
            callable_=rectangle.animation_parallel,
            match=("There is an animation target that is changed " "delay setting:"),
            animations=animations,
        )

    @apply_test_settings()
    def test__validate_animations_easing_are_default_vals(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animations: List[ap.AnimationBase] = [
            rectangle.animation_x(x=100),
        ]
        rectangle.animation_parallel(animations=animations)

        animations = [
            rectangle.animation_x(x=100, easing=ap.Easing.EASE_OUT_QUINT),
        ]
        assert_raises(
            expected_error_class=ValueError,
            callable_=rectangle.animation_parallel,
            match=("There is an animation target that is changed " "easing setting:"),
            animations=animations,
        )

    @apply_test_settings()
    def test__make_animation_attr_exp(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        rectangle: ap.Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=50, height=50
        )
        animation_fill_color: ap.AnimationFillColor = rectangle.animation_fill_color(
            fill_color="#0af"
        )
        animation_line_thickness: ap.AnimationLineThickness = (
            rectangle.animation_line_thickness(thickness=5)
        )
        animations: List[ap.AnimationBase] = [
            animation_fill_color,
            animation_line_thickness,
        ]
        animation_parallel: ap.AnimationParallel = rectangle.animation_parallel(
            animations=animations
        )
        expression: str = animation_parallel._get_animation_func_expression()
        assert expression == (
            "\n  .attr({"
            f"\n    fill: {animation_fill_color._fill_color.variable_name},"
            '\n    "stroke-width": '
            f"{animation_line_thickness._line_thickness.variable_name}"
            "\n  });"
        )
