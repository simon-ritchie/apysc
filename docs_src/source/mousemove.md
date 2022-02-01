# Mousemove interface

This page explains the `mousemove` interface.

## What interface is this?

The `mousemove` interface binds the mouse moving event handler to any `DisplayObject` instance. If you move the mouse cursor on that instance, the interface calls the registered handler.

## See also

The following page describes the basic mouse event interfaces.

- [Basic mouse event interfaces](mouse_event_basic.md)

## Basic usage

Each `DisplayObject` instance has the `mousemove` method, and you can bind handlers by that.

The following example binds the mouse move event handler to the circle. So if you move a mouse cursor on that, the circle follows the cursor position.

```py
# runnable
import apysc as ap


def on_mousemove(
        e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the circle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)

ap.save_overall_html(
    dest_dir_path='mousemove_basic_usage/')
```

<iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

## Unbind interfaces

`unbind_mousemove` interface can remove the binding of the mouse move event from the `DisplayObject`\.

In the following example, the interface removes the mouse move event handler if you click the circle.

```py
# runnable
import apysc as ap


def on_mousemove(
        e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the circle calls when mousemove.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.x = e.stage_x
    circle.y = e.stage_y


def on_click(e: ap.MouseEvent[ap.Circle], options: dict) -> None:
    """
    The handler that the circle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    circle: ap.Circle = e.this
    circle.unbind_mousemove(handler=on_mousemove)


ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)
circle.mousemove(on_mousemove)
circle.click(on_click)

ap.save_overall_html(
    dest_dir_path='mousemove_unbind_interface/')
```

<iframe src="static/mousemove_unbind_interface/index.html" width="200" height="200"></iframe>

There are also existing the `unbind_mousemove_all` interface. This interface unbinds all the handlers from the target `DisplayObject` instance.


## mousemove API

<!-- Docstring: apysc._event.mouse_move_interface.MouseMoveInterface.mousemove -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `mousemove(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>

**[Interface summary]** Add mouse move event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mousemove on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
```

<hr>

**[References]**

- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## unbind_mousemove API

<!-- Docstring: apysc._event.mouse_move_interface.MouseMoveInterface.unbind_mousemove -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_mousemove(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[Interface summary]** Unbind a specified handler's mouse move event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove(on_mousemove)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```

## unbind_mousemove_all API

<!-- Docstring: apysc._event.mouse_move_interface.MouseMoveInterface.unbind_mousemove_all -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_mousemove_all(self) -> None`<hr>

**[Interface summary]** Unbind all mouse move events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousemove(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     stage_x: ap.Int = e.stage_x
...     ap.trace('stage_x:', stage_x)
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.unbind_mousemove_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousemove(on_mousemove)
>>> _ = rectangle.click(on_click)
```