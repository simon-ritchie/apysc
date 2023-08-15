# What apysc can do in its current implementation

This page explains the current apysc implementation and functionality summary.

## Write with the Python and export HTML or use it on the Jupyter

The apysc library can write the front-end with the Python language and export the HTML or use it on the Jupyter notebook, JupyterLab, and the Google Colaboratory!

See also:

- [save_overall_html interface](save_overall_html.md)
- [display_on_jupyter interface](display_on_jupyter.md)
- [display_on_colaboratory interface](display_on_colaboratory.md)

## Draw the many types of the vector graphics

The apysc library can draw many vector graphics types, like the rectangle, circle, line.

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=650,
    stage_height=210,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

sprite.graphics.draw_round_rect(
    x=150, y=50, width=50, height=50, ellipse_width=12, ellipse_height=12
)

sprite.graphics.draw_circle(x=275, y=75, radius=25)

sprite.graphics.draw_ellipse(x=375, y=75, width=50, height=30)

sprite.graphics.draw_polygon(
    points=[
        ap.Point2D(x=475, y=50),
        ap.Point2D(x=450, y=100),
        ap.Point2D(x=500, y=100),
    ]
)

sprite.graphics.begin_fill(color=ap.COLORLESS)
sprite.graphics.line_style(color=ap.Color("#eee"), thickness=3)
sprite.graphics.move_to(x=550, y=50)
sprite.graphics.line_to(x=600, y=50)
sprite.graphics.line_to(x=550, y=100)
sprite.graphics.line_to(x=600, y=100)

sprite.graphics.draw_line(x_start=50, y_start=130, x_end=600, y_end=130)
sprite.graphics.draw_dotted_line(
    x_start=50, y_start=145, x_end=600, y_end=145, dot_size=2
)
sprite.graphics.draw_round_dotted_line(
    x_start=53, y_start=160, x_end=600, y_end=160, round_size=6, space_size=6
)

ap.save_overall_html(dest_dir_path="what_apysc_can_do_draw_vector_graphics/")
```

</details>

<iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>

See also:

- [Graphics class](graphics.md)
- [Graphics class begin_fill interface](graphics_begin_fill.md)
- [Graphics class line_style interface](graphics_line_style.md)
- [Graphics class draw_rect interface](graphics_draw_rect.md)
- [Graphics class draw_round_rect interface](graphics_draw_round_rect.md)
- [Graphics class draw_circle interface](graphics_draw_circle.md)
- [Graphics class draw_ellipse interface](graphics_draw_ellipse.md)
- [Graphics class move_to and line_to interfaces](graphics_move_to_and_line_to.md)
- [Graphics class draw_line interface](graphics_draw_line.md)
- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)
- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)
- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)
- [Graphics class draw_polygon interface](graphics_draw_polygon.md)

## Set each mouse event

The apysc library supports each mouse event, like the click, mouse down, mouse over, mouse move.

The click event example (please click the following rectangle):

<details>
<summary>Display the code block:</summary>

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    color: ap.Color = e.this.fill_color
    condition: ap.Boolean = color == ap.Color("#00aaff")
    with ap.If(condition):
        e.this.fill_color = ap.Color("#f0a")
    with ap.Else():
        e.this.fill_color = ap.Color("#0af")


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="what_apysc_can_do_mouse_event_click/")
```

</details>

<iframe src="static/what_apysc_can_do_mouse_event_click/index.html" width="150" height="150"></iframe>

See also:

- [Basic mouse event interfaces](mouse_event_basic.md)
- [click interface](click.md)
- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [mousemove interface](mousemove.md)

## The timer interface and animation

You can use the timer-related interfaces and animate with them.

<details>
<summary>Display the code block:</summary>

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _Options(TypedDict):
    rectangle: ap.Rectangle
    alpha_direction: ap.Int


def on_timer(e: ap.TimerEvent, options: _Options) -> None:
    """
    The handler that the timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = options["rectangle"]
    alpha_direction: ap.Int = options["alpha_direction"]
    current_alpha: ap.Number = rectangle.fill_alpha
    condition_1: ap.Boolean = current_alpha < 0.0
    condition_2: ap.Boolean = current_alpha > 1.0
    with ap.If(condition_1):
        alpha_direction.value = 1
    with ap.Elif(condition_2):
        alpha_direction.value = -1
    rectangle.fill_alpha += alpha_direction * 0.03
    rectangle.rotation_around_center += 1


ap.Stage(
    stage_width=150,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color=ap.Color("#0af"))
alpha_direction: ap.Int = ap.Int(1)
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
options: _Options = {"rectangle": rectangle, "alpha_direction": alpha_direction}
timer: ap.Timer = ap.Timer(on_timer, delay=ap.FPS.FPS_60, options=options)
timer.start()

ap.save_overall_html(dest_dir_path="what_apysc_can_do_timer_animation/")
```

</details>

<iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>

See also:

- [Timer class](timer.md)
- [TimerEvent class](timer_event.md)
- [Timer class delay setting](timer_delay.md)
- [FPS enum](fps.md)
- [Timer class repeat_count setting](timer_repeat_count.md)
- [Timer class start and stop interfaces](timer_start_and_stop.md)
- [Timer class timer_complete interface](timer_complete.md)
- [Timer class reset interface](timer_reset.md)

## Animate properties with each animation interface

You can use each animation (tween) interface and animate with them.

<iframe src="static/animation_interfaces_abstract_each_attr/index.html" width="550" height="550"></iframe>

See also:

- [Animation interfaces abstract](animation_interfaces_abstract.md)