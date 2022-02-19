# Mouseover and mouseout interfaces

This page explains the `mouseover` and `mouseout` interfaces.

## What interfaces are these?

The `mouseover` interface binds the event handler. Moreover, this interface calls the handler when a mouse cursor is over on a `DisplayObject` instance. Conversely, the `mouseout` interface also binds and calls the handler when a cursor is out from the `DisplayObject` one.

## See also

The following page describes the basic mouse event interfaces.

- [Basic mouse event interfaces](mouse_event_basic.md)

## Basic usage of the mouseover and mouseout interfaces

Each `DisplayObject` instance has the `mouseover` and `mouseout` interfaces, and you can bind handlers by these.

The following example binds the mouse over and handler and mouse out one to the rectangle. The rectangle color changes when your cursor is over the rectangle. Also, it reverts to the original one when your cursor is outed from the rectangle.

```py
# runnable
import apysc as ap


def on_mouseover(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseover.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this

    # Change the rectangle fill color to magenta.
    rectangle.fill_color = ap.String('#f0a')


def on_mouseout(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseout.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this

    # Revert the rectangle fill color.
    rectangle.fill_color = ap.String('#0af')


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Bind the mouse over and mouse out event handlers to the rectangle.
rectangle.mouseover(on_mouseover)
rectangle.mouseout(on_mouseout)

ap.save_overall_html(
    dest_dir_path='mouseover_and_mouseout_basic_usage/')
```

<iframe src="static/mouseover_and_mouseout_basic_usage/index.html" width="150" height="150"></iframe>

## Unbind Interfaces

The `unbind_mouseover` and `unbind_mouseout` interfaces unbind each registered handler from the `DisplayObject`\.

The following example unbind handlers in the `on_mouseover` and `on_mouseout` functions so that the interface calls these handlers only once.

```py
# runnable
import apysc as ap


def on_mouseover(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseover.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#f0a')

    # Unbind the mouseover handler.
    rectangle.unbind_mouseover(handler=on_mouseover)


def on_mouseout(
        e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when mouseout.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.fill_color = ap.String('#0af')

    rectangle.unbind_mouseout(handler=on_mouseout)


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle.mouseover(on_mouseover)
rectangle.mouseout(on_mouseout)

ap.save_overall_html(
    dest_dir_path='mouseover_and_mouseout_unbind_interfaces/')
```

<iframe src="static/mouseover_and_mouseout_unbind_interfaces/index.html" width="150" height="150"></iframe>

There are also existing the `unbind_mouseover_all` and `unbind_mouseover_all` interfaces. These interfaces unbind all the handlers from the target `DisplayObject` instance.


## mouseover API

<!-- Docstring: apysc._event.mouse_over_interface.MouseOverInterface.mouseover -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `mouseover(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>

**[Interface summary]** Add mouse over event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse over on this instance.
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
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

<hr>

**[References]**

- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## unbind_mouseover API

<!-- Docstring: apysc._event.mouse_over_interface.MouseOverInterface.unbind_mouseover -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_mouseover(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[Interface summary]** Unbind a specified handler's mouseover event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseover(on_mouseover)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

## unbind_mouseover_all API

<!-- Docstring: apysc._event.mouse_over_interface.MouseOverInterface.unbind_mouseover_all -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_mouseover_all(self) -> None`<hr>

**[Interface summary]** Unbind all mouseover events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseover(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseover_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseover)
```

## mouseout API

<!-- Docstring: apysc._event.mouse_out_interface.MouseOutInterface.mouseout -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `mouseout(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType], *, options:Union[~_O, NoneType]=None) -> str`<hr>

**[Interface summary]** Add mouse out event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse out on this instance.
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
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

<hr>

**[References]**

- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## unbind_mouseout API

<!-- Docstring: apysc._event.mouse_out_interface.MouseOutInterface.unbind_mouseout -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_mouseout(self, handler:Callable[[apysc._event.mouse_event.MouseEvent, ~_O], NoneType]) -> None`<hr>

**[Interface summary]** Unbind a specified handler's mouse-out event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseout(on_mouseout)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```

## unbind_mouseout_all API

<!-- Docstring: apysc._event.mouse_out_interface.MouseOutInterface.unbind_mouseout_all -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `unbind_mouseout_all(self) -> None`<hr>

**[Interface summary]** Unbind all mouse out events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseout(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseout_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseout(on_mouseout)
```