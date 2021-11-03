# Animation interfaces abstract

This page will explain the animation interfaces abstract.

## What apysc can do in its animation interfaces

- You can animate each attribute, such as the coordinates, rotation, color, alpha (opacity), and so on.
- You can set the animation's duration in milliseconds.
- You can set the animation's delay in milliseconds.
- You can use lots of easing settings, such as the `EASE_IN_CUBIC`, `EASE_OUT_QUINT`, and `EASE_IN_OUT_BOUNCE`.
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

stage: ap.Stage = ap.Stage(
    stage_width=550, stage_height=550, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.line_style(color='#fff', thickness=1)

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_x_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the x animation is completed.

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
    The handler will be called when the x animation is completed.

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
    The handler will be called when the y animation is completed.

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
    The handler will be called when the y animation is completed.

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
    The handler will be called when the center-x animation
    is completed.

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
    The handler will be called when the center-x animation
    is completed.

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
    The handler will be called when the center-y animation
    is completed.

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
    The handler will be called when the center-y animation
    is completed.

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
    The handler will be called when the move animation is completed.

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
    The handler will be called when the move animation is completed.

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
    The handler will be called when the width animation is completed.

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
    The handler will be called when the width animation is completed.

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
    The handler will be called when the height animation is completed.

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
    The handler will be called when the width animation is completed.

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
    The handler will be called when the ellipse-width animation
    is completed.

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
    The handler will be called when the ellipse-width animation
    is completed.

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
    The handler will be called when the ellipse-height animation
    is completed.

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
    The handler will be called when the ellipse-height animation
    is completed.

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
    The handler will be called when the fill-color animation
    is completed.

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
    The handler will be called when the fill-color animation
    is completed.

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
    The handler will be called when the fill-alpha animation
    is completed.

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
    The handler will be called when the fill-alpha animation
    is completed.

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
    The handler will be called when the line-color animation
    is completed.

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
    The handler will be called when the line-color animation
    is completed.

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
    The handler will be called when the line-alpha animation
    is completed.

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
    The handler will be called when the line-alpha animation
    is completed.

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
    The handler will be called when the line-thickness animation
    is completed.

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
    The handler will be called when the line-thickness animation
    is completed.

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
    The handler will be called when the radius animation is completed.

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
    The handler will be called when the radius animation is completed.

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
    The handler will be called when the rotation around the
    center point animation is completed.

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
    The handler will be called when the rotation around the
    center point animation is completed.

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
    The handler will be called when the rotation around the
    specified point animation is completed.

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
    The handler will be called when the rotation around the
    specified point animation is completed.

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
    The handler will be called when the scale-x from the center
    point animation is completed.

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
    The handler will be called when the scale-x from the center
    point animation is completed.

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
    The handler will be called when the scale-y from the center
    point animation is completed.

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
    The handler will be called when the scale-y from the center
    point animation is completed.

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
    The handler will be called when the scale-x from the
    specified point animation is completed.

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
    The handler will be called when the scale-x from the
    specified point animation is completed.

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
    The handler will be called when the scale-y from the
    specified point animation is completed.

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
    The handler will be called when the scale-y from the
    specified point animation is completed.

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
    The handler will be called when the skew-x animation is completed.

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
    The handler will be called when the skew-x animation is completed.

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

## x animation

The `animation_x` interface sets the x-coordinate animation. For more details: [animation_x interface document](animation_x.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

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
    The handler will be called when the animation is completed.

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

## y animation


The `animation_y` interface sets the y-coordinate animation. For more details: [animation_y interface document](animation_y.md)

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')

DURATION: int = 1000
DELAY: int = 500
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

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
    The handler will be called when the animation is completed.

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
