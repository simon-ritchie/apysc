# Return

This page will explain the `Return` class.

Before reading on, maybe it is useful to read the following page (the `Return` class will be used for the same reason of each apysc data type):

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)

## What is the Return class?

The `Return` class will be used to append the `return;` JavaScript code. This class can be used only in an event handler (function or method) scope.

## Basic usage

The `Return` class constructor accepts no arguments. This interface will be used with the branch condition, like the `ap.If` class.

The following example will change the rectangle fill color when you click it. Each `ap.If` branch instantiate `Return` class so the changing of fill color will be applied one by one:

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


stage: ap.Stage = ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='return_basic_usage/')
```

<iframe src="static/return_basic_usage/index.html" width="150" height="150"></iframe>
