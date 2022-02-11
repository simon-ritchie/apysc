# Trace interface

This page explains the `trace` function interface.

## What interface is this?

The `trace` function interface displays any message on the browser console. This interface behaves like the JavaScript `console.log` function.

## Basic usage

The `trace` function can accept any number of arguments and various value types.

The following example draws the rectangle. Then, the handler displays the message on the browser console when you click it(please press the F12 key).

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


## trace API

<!-- Docstring: apysc._console._trace.trace -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `trace(*args:Any) -> None`<hr>

**[Interface summary]** Display arguments information to console. This function saves a JavaScript `console.log` expression.<hr>

**[Parameters]**

- `*args`: list
  - Any arguments to display to console.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.trace('Int value is:', int_val)
```