# Click interface

This page will explain the `click` interface.

## What interface is this?

The `click` interface will bind the click event to any `DisplayObject` instance (e.g., `Sprite`, `Rectangle`, and so on). If you mouse down on that instance and also mouse up, the registered handler function will be called.

Conversely, the `unbind_click` interface will unbind the click event from the `DisplayObject` instance.

## See also

Common mouse event interfaces are described by the following page.

- [Common mouse event interfaces](mouse_event_common.md)

## Basic usage of the click interface

Each `DisplayObject` instance has the `click` method, and you can bind handlers by that.

The following example will bind the click event handler to the rectangle.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)

ap.save_overall_html(
    dest_dir_path='click_basic_usage_of_the_click_interface/')
```

If you click the following rectangle, the rectangle color will become the magenta color.

<iframe src="static/click_basic_usage_of_the_click_interface/index.html" width="150" height="150"></iframe>


## Basic usage of the unbind_click interface

The `unbind_click` interface can remove the binded click event from a `DisplayObject` instance.

The following example is removing the click event by the `unbind_click` method and if you click the rectangle, nothing will happen.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.
    the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)
rectangle.unbind_click(handler=on_click)

ap.save_overall_html(
    dest_dir_path='click_basic_usage_of_the_unbind_click_interface/')
```

<iframe src="static/click_basic_usage_of_the_unbind_click_interface/index.html" width="150" height="150"></iframe>


## Unbind all the click event handlers

`unbind_click_all` interface can unbind all the click event handlers from the `DisplayObject` instance.

The following example is removing all the click events by the `unbind_click_all` method (if you click the rectangle, nothing will happen).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')


def on_click(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the rectangle is clicked.
    the rectangle.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(handler=on_click)
rectangle.unbind_click_all()

ap.save_overall_html(
    dest_dir_path='click_unbind_all_the_click_event_handlers/')
```

<iframe src="static/click_unbind_all_the_click_event_handlers/index.html" width="150" height="150"></iframe>
