# Click interface

This page explains the `click` interface.

## What interface is this?

The `click` interface binds the click event to any `DisplayObject` instance (e.g., `Sprite`\, `Rectangle`\, and so on). These interfaces call the registered handler function if you mouse down on that instance and mouse up.

Conversely, the `unbind_click` interface unbinds the click event from the `DisplayObject` instance.

## See also

The following page describes basic mouse event interfaces.

- [Basic mouse event interfaces](mouse_event_basic.md)

## Basic usage of the click interface

Each `DisplayObject` instance has the `click` method, and you can bind handlers by that.

The following example binds the click event handler to the rectangle.

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
    The handler that the rectangle calls when clicked.

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

If you click the following rectangle, the rectangle color becomes the magenta color.

<iframe src="static/click_basic_usage_of_the_click_interface/index.html" width="150" height="150"></iframe>


## Basic usage of the unbind_click interface

The `unbind_click` interface can remove the binded click event from a `DisplayObject` instance.

The following example removes the click event by the `unbind_click` method, and nothing happens if you click the rectangle.

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
    The handler that the rectangle calls when clicked.

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

The following example removes all the click events by the `unbind_click_all` method (if you click the rectangle, nothing happens).

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
    The handler that the rectangle calls when clicked.

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


## click API

<!-- Docstring: apysc._event.click_interface.ClickInterface.click -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `click(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>

**[Interface summary]** Add a click event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable would be called when clicking this instance.
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
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.x += 10
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## unbind_click API

<!-- Docstring: apysc._event.click_interface.ClickInterface.unbind_click -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_click(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[Interface summary]** Unbind specified handler's click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click(on_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

## unbind_click_all API

<!-- Docstring: apysc._event.click_interface.ClickInterface.unbind_click_all -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_click_all(self) -> None`<hr>

**[Interface summary]** Unbind all click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_click_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```