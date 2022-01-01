# Animation interfaces abstract

This page explains the animation interfaces' abstract.

## What apysc can do in its animation interfaces

- You can animate each attribute, such as the coordinates, rotation, color, alpha (opacity), scale.
- You can set the animation's duration in milliseconds.
- You can set the animation's delay in milliseconds.
- You can use many easing settings, such as the `EASE_IN_CUBIC`\, `EASE_OUT_QUINT`\, and `EASE_IN_OUT_BOUNCE`\.
- You can control the target instance's animation with the pause, play, reset, finish, reverse, time interfaces.
- You can set the parallel animation or sequential animation.
- Animation complete event is supported.

## Examples of each attribute animation

This section will show each attribute animation example:

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=550, stage_height=550, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.line_style(color='#fff', thickness=1)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_x_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the x-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_x_animation_complete_2).start()


def on_x_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the x-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_x_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_x_animation_complete_1).start()


def on_y_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the y-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_y_animation_complete_2).start()


def on_y_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the y-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_y_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50,
).animation_y(
    y=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_y_animation_complete_1).start()


def on_cx_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=275, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cx_animation_complete_2).start()


def on_cx_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=325, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cx_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=275, y=75, radius=25,
).animation_x(
    x=325, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_cx_animation_complete_1).start()


def on_cy_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-y animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=75, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cy_animation_complete_2).start()


def on_cy_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the center-y animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=25, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_cy_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=375, y=75, radius=25,
).animation_y(
    y=25, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_cy_animation_complete_1).start()


def on_move_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that move-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=450, y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_move_animation_complete_2).start()


def on_move_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that move-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=500, y=0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_move_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=450, y=50, width=50, height=50,
).animation_move(
    x=500, y=0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_move_animation_complete_1).start()


def on_width_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_width_animation_complete_2).start()


def on_width_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_width_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50,
).animation_width(
    width=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_width_animation_complete_1).start()


def on_height_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_height_animation_complete_2).start()


def on_height_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_height_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=150, y=150, width=50, height=50,
).animation_height(
    height=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_height_animation_complete_1).start()


def on_ellipse_width_animation_complete_1(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_width_animation_complete_2).start()


def on_ellipse_width_animation_complete_2(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-width animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_width_animation_complete_1).start()


sprite.graphics.draw_ellipse(
    x=275, y=175, width=50, height=50,
).animation_width(
    width=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_ellipse_width_animation_complete_1).start()


def on_ellipse_height_animation_complete_1(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_height_animation_complete_2).start()


def on_ellipse_height_animation_complete_2(
        e: ap.AnimationEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse-height animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_ellipse_height_animation_complete_1).start()


sprite.graphics.draw_ellipse(
    x=375, y=175, width=50, height=50,
).animation_height(
    height=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_ellipse_height_animation_complete_1).start()


def on_fill_color_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#0af', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_color_animation_complete_2).start()


def on_fill_color_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_color_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=450, y=150, width=50, height=50,
).animation_fill_color(
    fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_fill_color_animation_complete_1).start()


def on_fill_alpha_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_alpha_animation_complete_2).start()


def on_fill_alpha_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the fill-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_fill_alpha_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50,
).animation_fill_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_fill_alpha_animation_complete_1).start()


def on_line_color_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#fff', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_color_animation_complete_2).start()


def on_line_color_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-color animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#666', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_color_animation_complete_1).start()


sprite.graphics.line_style(color='#fff', thickness=5)
sprite.graphics.draw_rect(
    x=150, y=250, width=50, height=50,
).animation_line_color(
    line_color='#666', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_line_color_animation_complete_1).start()


def on_line_alpha_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_alpha_animation_complete_2).start()


def on_line_alpha_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-alpha animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_alpha_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=250, y=250, width=50, height=50,
).animation_line_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_line_alpha_animation_complete_1).start()
sprite.graphics.line_style(color='#fff', thickness=1)


def on_line_thickness_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-thickness animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=1, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_thickness_animation_complete_2).start()


def on_line_thickness_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the line-thickness animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_line_thickness_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=350, y=250, width=50, height=50,
).animation_line_thickness(
    thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_line_thickness_animation_complete_1).start()


def on_radius_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the radius-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=25, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_radius_animation_complete_2).start()


def on_radius_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the radius-animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_radius_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=475, y=275, radius=25,
).animation_radius(
    radius=50, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_radius_animation_complete_1).start()


def on_rotation_around_center_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(
        on_rotation_around_center_animation_complete_2,
    ).start()


def on_rotation_around_center_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=90, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(
        on_rotation_around_center_animation_complete_1,
    ).start()


sprite.graphics.draw_rect(
    x=50, y=350, width=50, height=50,
).animation_rotation_around_center(
    rotation_around_center=90, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_rotation_around_center_animation_complete_1).start()


def on_rotation_around_point_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=0,
        x=200, y=400, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(
        on_rotation_around_point_animation_complete_2,
    ).start()


def on_rotation_around_point_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rotation around the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=90,
        x=200, y=400, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(
        on_rotation_around_point_animation_complete_1,
    ).start()


sprite.graphics.draw_rect(
    x=150, y=350, width=50, height=50,
).animation_rotation_around_point(
    rotation_around_point=90,
    x=200, y=400, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_rotation_around_point_animation_complete_1).start()


def on_scale_x_from_center_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_center_animation_complete_2).start()


def on_scale_x_from_center_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the center point animation
    calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_center_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=250, y=350, width=50, height=50,
).animation_scale_x_from_center(
    scale_x_from_center=0.5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_scale_x_from_center_animation_complete_1).start()


def on_scale_y_from_center_animation_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the center point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_center_animation_2).start()


def on_scale_y_from_center_animation_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the center point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_center_animation_1).start()


sprite.graphics.draw_rect(
    x=350, y=350, width=50, height=50,
).animation_scale_y_from_center(
    scale_y_from_center=0.5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_scale_y_from_center_animation_1).start()


def on_scale_x_from_point_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=1.0, x=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_point_animation_complete_2).start()


def on_scale_x_from_point_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-x from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=0.5, x=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_x_from_point_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=450, y=350, width=50, height=50,
).animation_scale_x_from_point(
    scale_x_from_point=0.5, x=500, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_scale_x_from_point_animation_complete_1).start()


def on_scale_y_from_point_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=1.0, y=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_point_animation_complete_2).start()


def on_scale_y_from_point_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the scale-y from the specified point
    animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=0.5, y=500, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_scale_y_from_point_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=450, width=50, height=50,
).animation_scale_y_from_point(
    scale_y_from_point=0.5, y=500, duration=DURATION, delay=DELAY,
).animation_complete(on_scale_y_from_point_animation_complete_1).start()


def on_skew_x_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the skew-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_skew_x_animation_complete_2).start()


def on_skew_x_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the skew-x animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=30, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_skew_x_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=150, y=450, width=50, height=50,
).animation_skew_x(
    skew_x=30, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_skew_x_animation_complete_1).start()


ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_each_attr/')
```

</details>

<iframe src="static/animation_interfaces_abstract_each_attr/index.html" width="550" height="550"></iframe>

## Easing

The easing setting can be set with the `easing` argument of each animation interface. For more details: [Easing enum document](easing_enum.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap

ap.Stage(
    stage_width=200, stage_height=350, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500


class EasingOptions(TypedDict):
    easing: ap.Easing


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: EasingOptions) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=50, duration=DURATION, delay=DELAY,
        easing=options['easing'],
    ).animation_complete(
        on_animation_complete_2, options=options,
    ).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: EasingOptions) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=100, duration=DURATION, delay=DELAY,
        easing=options['easing'],
    ).animation_complete(
        on_animation_complete_1, options=options,
    ).start()


options: EasingOptions = {'easing': ap.Easing.EASE_IN_QUINT}
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY,
    easing=options['easing'],
).animation_complete(
    on_animation_complete_1, options=options,
).start()

options = {'easing': ap.Easing.EASE_OUT_QUINT}
sprite.graphics.draw_rect(
    x=50, y=150, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY,
    easing=options['easing'],
).animation_complete(
    on_animation_complete_1, options=options,
).start()

options = {'easing': ap.Easing.EASE_IN_OUT_QUINT}
sprite.graphics.draw_rect(
    x=50, y=250, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY,
    easing=options['easing'],
).animation_complete(
    on_animation_complete_1, options=options,
).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_easing/')
```

</details>

<iframe src="static/animation_interfaces_abstract_easing/index.html" width="200" height="350"></iframe>

## X animation

The `animation_x` interface sets the x-coordinate animation. For more details: [animation_x interface document](animation_x.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_x(
        x=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_x(
    x=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_x/')
```

</details>

<iframe src="static/animation_interfaces_abstract_x/index.html" width="200" height="150"></iframe>

## Y animation


The `animation_y` interface sets the y-coordinate animation. For more details: [animation_y interface document](animation_y.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_y(
        y=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_y(
    y=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_y/')
```

</details>

<iframe src="static/animation_interfaces_abstract_y/index.html" width="150" height="200"></iframe>

## Move animation

The `animation_move` interface sets the x- and y-coordinates animation. For more details: [animation_move interface document](animation_move.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=50, y=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_move(
        x=100, y=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_move(
    x=100, y=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_move/')
```

</details>

<iframe src="static/animation_interfaces_abstract_move/index.html" width="200" height="200"></iframe>

## Width animation

The `animation_width` interface sets the width animation. For more details: [animation_width and animation_height interfaces document](animation_width_and_height.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_width(
        width=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_width(
    width=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_width/')
```

</details>

<iframe src="static/animation_interfaces_abstract_width/index.html" width="200" height="150"></iframe>

## Height animation

The `animation_height` interface sets the height animation. For more details: [animation_width and animation_height interfaces document](animation_width_and_height.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_height(
        height=100, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_height(
    height=100, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_height/')
```

</details>

<iframe src="static/animation_interfaces_abstract_height/index.html" width="150" height="200"></iframe>

## Fill color animation

The `animation_fill_color` interface sets the fill color animation. For more details: [animation_fill_color interface document](animation_fill_color.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#0af', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_color(
        fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_fill_color(
    fill_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_fill_color/')
```

</details>

<iframe src="static/animation_interfaces_abstract_fill_color/index.html" width="150" height="150"></iframe>

## Fill alpha animation

The `animation_fill_alpha` interface sets the alpha (opacity) animation. For more details: [animation_fill_alpha interface document](animation_fill_alpha.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_fill_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_fill_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_fill_alpha/')
```

</details>

<iframe src="static/animation_interfaces_abstract_fill_alpha/index.html" width="150" height="150"></iframe>

## Line-color animation

The `animation_line_color` interface sets the line color animation. For more details: [animation_line_color interface document](animation_line_color.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=5)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#0af', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_color(
        line_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_line_color(
    line_color='#f0a', duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_line_color/')
```

</details>

<iframe src="static/animation_interfaces_abstract_line_color/index.html" width="150" height="150"></iframe>

## Line alpha animation

The `animation_line_alpha` interface sets the line alpha (opacity) animation. For more details: [animation_line_alpha interface document](animation_line_alpha.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=5)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=1.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_alpha(
        alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_line_alpha(
    alpha=0.0, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_line_alpha/')
```

</details>

<iframe src="static/animation_interfaces_abstract_line_alpha/index.html" width="150" height="150"></iframe>

## Line thickness animation

The `animation_line_thickness` interface sets the line thickness (stroke width) animation. For more details: [animation_line_thickness interface document](animation_line_thickness.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#fff', thickness=1)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=1, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_line_thickness(
        thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_line_thickness(
    thickness=5, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_line_thickness/')
```

</details>

<iframe src="static/animation_interfaces_abstract_line_thickness/index.html" width="150" height="150"></iframe>

## Radius animation

The `animation_radius` interface sets the radius (for instance, circle's radius) animation. For more details: [animation_radius interface document](animation_radius.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=25, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_radius(
        radius=50, duration=DURATION, delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_circle(
    x=75, y=75, radius=25,
).animation_radius(
    radius=50, duration=DURATION, delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_radius/')
```

</details>

<iframe src="static/animation_interfaces_abstract_radius/index.html" width="150" height="150"></iframe>

## Rotation animation around the center point

The `animation_rotation_around_center` interface sets the rotation animation around the center point. For more details: [animation_rotation_around_center interface document](animation_rotation_around_center.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_center(
        rotation_around_center=90, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_rotation_around_center(
    rotation_around_center=90, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_rotation_around_center/')
```

</details>

<iframe src="static/animation_interfaces_abstract_rotation_around_center/index.html" width="150" height="150"></iframe>

## Rotation animation around the specified point

The `animation_rotation_around_point` interface sets the rotation animation around the specified point. For more details: [animation_rotation_around_point interface document](animation_rotation_around_point.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=0, x=100, y=100, duration=DURATION,
        delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_rotation_around_point(
        rotation_around_point=90, x=100, y=100, duration=DURATION,
        delay=DELAY, easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_rotation_around_point(
    rotation_around_point=90, x=100, y=100, duration=DURATION,
    delay=DELAY, easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_rotation_around_point/')
```

</details>

<iframe src="static/animation_interfaces_abstract_rotation_around_point/index.html" width="200" height="150"></iframe>

## Scale-x animation from the center point

The `animation_scale_x_from_center` interface sets the scale-x animation from the center point. For more details: [animation_scale_x_from_center and animation_scale_x_from_center interfaces document](animation_scale_x_and_y_from_center.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_center(
        scale_x_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_x_from_center(
    scale_x_from_center=0.5, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_x_from_center/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_x_from_center/index.html" width="150" height="150"></iframe>

## Scale-y animation from the center point

The `animation_scale_y_from_center` interface sets the scale-y animation from the center point. For more details: [animation_scale_x_from_center and animation_scale_x_from_center interfaces document](animation_scale_x_and_y_from_center.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=1.0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_center(
        scale_y_from_center=0.5, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_y_from_center(
    scale_y_from_center=0.5, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_y_from_center/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_y_from_center/index.html" width="150" height="150"></iframe>

## Scale-x animation from the specified point

The `animation_scale_x_from_point` interface sets the scale-x animation from the specified point. For more details: [animation_scale_x_from_point and animation_scale_y_from_point interfaces document](animation_scale_x_and_y_from_point.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=1.0, x=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_x_from_point(
        scale_x_from_point=0.5, x=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_x_from_point(
    scale_x_from_point=0.5, x=100, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_x_from_point/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_x_from_point/index.html" width="150" height="150"></iframe>

## Scale-y animation from the specified point

The `animation_scale_y_from_point` interface sets the scale-y animation from the specified point. For more details: [animation_scale_x_from_point and animation_scale_y_from_point interfaces document](animation_scale_x_and_y_from_point.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=1.0, y=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_scale_y_from_point(
        scale_y_from_point=0.5, y=100, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_scale_y_from_point(
    scale_y_from_point=0.5, y=100, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_scale_y_from_point/')
```

</details>

<iframe src="static/animation_interfaces_abstract_scale_y_from_point/index.html" width="150" height="150"></iframe>

## Skew-x animation

The `animation_skew_x` interface sets the skew-x animation. For more details: [animation_skew_x interface document](animation_skew_x.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=0, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    e.this.target.animation_skew_x(
        skew_x=50, duration=DURATION, delay=DELAY,
        easing=EASING,
    ).animation_complete(on_animation_complete_1).start()


sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50,
).animation_skew_x(
    skew_x=50, duration=DURATION, delay=DELAY,
    easing=EASING,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='animation_interfaces_abstract_skew_x/')
```

</details>

<iframe src="static/animation_interfaces_abstract_skew_x/index.html" width="150" height="150"></iframe>
