# Return

This page explains the `Return` class.

Before reading on, maybe it is helpful to read the following page (the apysc uses the `Return` class for the same reason of each apysc data type):

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)

## What is the Return class?

The `Return` class behaves to append the `return;` JavaScript code. Therefore, this class can be used only in an event handler (function or method) scope.

## Basic usage

The `Return` class constructor accepts no arguments. You can use this interface with the branch condition, for example, the `ap.If` class.

The following example changes the rectangle fill color when you click it. Each `ap.If` branch instantiate `Return` class, so the code applies the changing of fill color one by one:

```py
# runnable
import apysc as ap


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    fill_color: ap.String = rectangle.fill_color
    with ap.If(fill_color == '#00aaff'):
        rectangle.fill_color = ap.String('#ff00aa')
        ap.Return()
    with ap.If(fill_color == '#ff00aa'):
        rectangle.fill_color = ap.String('#00ffaa')
        ap.Return()
    with ap.If(fill_color == '#00ffaa'):
        rectangle.fill_color = ap.String('#00aaff')
        ap.Return()


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='return_basic_usage/')
```

<iframe src="static/return_basic_usage/index.html" width="150" height="150"></iframe>