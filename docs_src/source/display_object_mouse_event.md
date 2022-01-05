# Display object mouse event binding interfaces

This page explains the `DisplayObject` class mouse event binding interfaces.

## What interfaces are these?

Each `DisplayObject` instance has the mouse event binding interfaces, like the click, mouse over, mouse move.

These interfaces can bind the mouse event to a `DisplayObject` instance. So, for instance, you can assign any function to handle when a `DisplayObject` instance click.

## Basic usage

You can bind event handler (callable) with each interface, like the `click`\, `mouseover`\.

The following example binds the click event handler, and if you click the rectangle, the fill color is changed.

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='display_object_mouse_event_basic_usage/')
```

<iframe src="static/display_object_mouse_event_basic_usage/index.html" width="150" height="150"></iframe>

## See also

For more details, please see the following pages:

- [Basic mouse event interfaces](mouse_event_basic.md)
- [Click interface](click.md)
- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [Mousemove interface](mousemove.md)
