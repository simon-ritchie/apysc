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
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    with ap.If(rectangle.fill_color == ap.Color("#00aaff")):
        rectangle.fill_color = ap.Color("#f0a")
        ap.Return()

    with ap.If(rectangle.fill_color == ap.Color("#ff00aa")):
        rectangle.fill_color = ap.Color("#0af")
        ap.Return()


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(dest_dir_path="mouse_event_abstract_click/")
```

<iframe src="static/mouse_event_abstract_click/index.html" width="150" height="150"></iframe>

## See also

There are a lot of other mouse event binding interfaces, such as the mouse down, mouse over, and mouse move. For more details, please see the following:

- [Basic mouse event interfaces](mouse_event_basic.md)
- [click interface](click.md)
- [dblclick interface](dblclick.md)
- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [mousemove interface](mousemove.md)