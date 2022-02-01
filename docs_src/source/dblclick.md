# Double click interface

This page explains the `dblclick` (double-click) interface.

## What interface is this?

The `dblclick` interface binds the double-click event to any `DisplayObject` instance (e.g., `Sprite`\, `Rectangle`\, and so on). If you double-click on that instance, this interface calls the registered handler function.

## See also

The following page describes the basic mouse event interfaces.

- [Basic mouse event interfaces](mouse_event_basic.md)

## Basic usage of the dblclick interface

Each `DisplayObject` instance has the `dblclick` method, and you can bind handlers by that.

The following example binds the double-click event handler to the rectangle. If you double-click on that instance, the rectangle color changes from cyan to magenta.

```py
# runnable
import apysc as ap


def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when double-clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.dblclick(on_double_click)

ap.save_overall_html(
    dest_dir_path='./dblclick_basic_usage/')
```

<iframe src="static/dblclick_basic_usage/index.html" width="150" height="150"></iframe>

## Basic usage of the unbind_dblclick interfaces

The `unbind_dblclick` interface can remove the single binded double-click event from a `DisplayObject` instance. The `unbind_dblclick_all` interface removes all double-click events.

The following example removes the double click event by the `unbind_dblclick` method. If you double-click the rectangle, nothing happens.

```py
# runnable
import apysc as ap


def on_double_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when double-clicked.

    Parameters
    ----------
    e : ap.MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')


ap.Stage(
    stage_width=150, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.dblclick(on_double_click)
rectangle.unbind_dblclick(on_double_click)

ap.save_overall_html(
    dest_dir_path='./unbind_dblclick_basic_usage/')
```

<iframe src="static/unbind_dblclick_basic_usage/index.html" width="150" height="150"></iframe>


## dblclick API

<!-- Docstring: apysc._event.double_click_interface.DoubleClickInterface.dblclick -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `dblclick(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>

**[Interface summary]** Add double click event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when double-clicking this instance.
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
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

<hr>

**[References]**

- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## unbind_dblclick API

<!-- Docstring: apysc._event.double_click_interface.DoubleClickInterface.unbind_dblclick -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_dblclick(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[Interface summary]** Unbind a specified handler's double click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_dblclick(on_double_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```

## unbind_dblclick_all API

<!-- Docstring: apysc._event.double_click_interface.DoubleClickInterface.unbind_dblclick_all -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_dblclick_all(self) -> None`<hr>

**[Interface summary]** Unbind all double click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_double_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_dblclick_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.dblclick(on_double_click)
```