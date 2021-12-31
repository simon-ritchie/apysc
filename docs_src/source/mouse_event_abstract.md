# MouseEvent interfaces abstract

This page explains the MouseEvent interfaces abstract.

## What apysc can do in its interfaces

- You can set the `MouseEvent` handlers, such as the click, mouse down, mouse over, and so on, to each graphic instance.
- You can pass the optional arguments to the handler.

## Example of the click event

To bind MouseEvent, defining the handler function (or method) would be necessary (e.g., `on_click`).

These handlers can bind with the click interface.

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
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
    with ap.If(rectangle.fill_color == '#00aaff'):
        rectangle.fill_color = ap.String('#f0a')
        ap.Return()

    with ap.If(rectangle.fill_color == '#ff00aa'):
        rectangle.fill_color = ap.String('#0af')
        ap.Return()


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
    dest_dir_path='mouse_event_abstract_click/')
```

<iframe src="static/mouse_event_abstract_click/index.html" width="150" height="150"></iframe>

## See also

There are a lot of other mouse event binding interfaces, such as the mouse down, mouse over, and mouse move. For more details, please see the following:

- [Common mouse event interfaces](mouse_event_common.md)
- [Click interface](click.md)
- [Double click interface](dblclick.md)
- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [Mousemove interface](mousemove.md)
