# append_js_expression interface

This page will explain the `append_js_expression` function interface.

## What interface is this?

The `append_js_expression` function interface will append any JavaScript to the exported HTML at any position. This interface may be useful if you need to use the apysc not supported interfaces or irregular JavaScript implementation, like the Django template tags or parameters (e.g., `{% if ... %}`).

## Basic usage

The `append_js_expression` function requires JavaScript string at the argument.

The following example will append the `console.log` JavaScript calling at the rectangle click handler:

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.append_js_expression(
        expression='console.log("The rectangle is clicked!");')


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='append_js_expression_basic_usage/')
```

If you click the following rectangle, the `The rectangle is clicked!` message will be displayed on the browser console (please press the F12 key).

<iframe src="static/append_js_expression_basic_usage/index.html" width="150" height="150"></iframe>
