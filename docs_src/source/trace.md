# Trace interface

This page explains the `trace` function interface.

## What interface is this?

The `trace` function interface displays any message on the browser console. This interface behaves like the JavaScript `console.log` function.

## Basic usage

The `trace` function can accept any number of arguments and various value types.

The following example draws the rectangle. When clicking the rectangle, the handler displays the message on the browser console (please press the F12 key).

```py
# runnable
import apysc as ap


def on_rectangle_click(
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
    ap.trace('Hello apysc!', 'Rectangle width:', e.this.width)


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_rectangle_click)

ap.save_overall_html(
    dest_dir_path='trace_basic_usage/')
```

<iframe src="static/trace_basic_usage/index.html" width="150" height="150"></iframe>
