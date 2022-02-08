# apysc._event.mouse_event_interfaces docstrings

## Module summary

Class implementation for inheritance of each mouse event interfaces.

## ClickInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_click_handlers_if_not_initialized method docstring

Initialize _click_handlers attribute if it hasn't been initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### click method docstring

Add a click event listener setting.<hr>

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

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_click method docstring

Unbind specified handler's click event.<hr>

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

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_click_all method docstring

Unbind all click events.<hr>

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

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

## DoubleClickInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### dblclick method docstring

Add double click event listener setting.<hr>

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

- [Double click interface document](https://simon-ritchie.github.io/apysc/dblclick.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_dblclick method docstring

Unbind a specified handler's double click event.<hr>

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

### unbind_dblclick_all method docstring

Unbind all double click events.<hr>

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

## MouseDownInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_mouse_down_handlers_if_not_initialized method docstring

Initialize _mouse_down_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### mousedown method docstring

Add mouse down event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse down on this instance.
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
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_mousedown method docstring

Unbind a specified handler's mouse down event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown(on_mousedown)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousedown_all method docstring

Unbind all mouse down events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

## MouseEventInterfaces class docstring

Class implementation for inheritance of each mouse event interfaces.

Class implementation for inheritance of each mouse event interfaces.

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_click_handlers_if_not_initialized method docstring

Initialize _click_handlers attribute if it hasn't been initialized yet.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

### _initialize_mouse_down_handlers_if_not_initialized method docstring

Initialize _mouse_down_handlers attribute if it is not initialized yet.

### _initialize_mouse_move_handlers_if_not_initialized method docstring

Initialize _mouse_move_handlers attribute if it is not initialized yet.

### _initialize_mouse_out_handlers_if_not_initialized method docstring

Initialize _mouse_out_handlers attribute if it is not initialized yet.

### _initialize_mouse_over_handlers_if_not_initialized method docstring

Initialize _mouse_over_handlers attribute if it is not initialized yet.

### _initialize_mouse_up_handlers_if_not_initialized method docstring

Initialize _mouse_up_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### click method docstring

Add a click event listener setting.<hr>

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

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### dblclick method docstring

Add double click event listener setting.<hr>

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

- [Double click interface document](https://simon-ritchie.github.io/apysc/dblclick.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mousedown method docstring

Add mouse down event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse down on this instance.
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
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mousemove method docstring

Add mouse move event listener setting.<hr>

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

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseout method docstring

Add mouse out event listener setting.<hr>

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

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseover method docstring

Add mouse over event listener setting.<hr>

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

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### mouseup method docstring

Add mouse up event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse-up on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_click method docstring

Unbind specified handler's click event.<hr>

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

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_click_all method docstring

Unbind all click events.<hr>

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

<hr>

**[References]**

- [Click interface document](https://simon-ritchie.github.io/apysc/click.html)

### unbind_dblclick method docstring

Unbind a specified handler's double click event.<hr>

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

### unbind_dblclick_all method docstring

Unbind all double click events.<hr>

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

### unbind_mousedown method docstring

Unbind a specified handler's mouse down event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown(on_mousedown)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousedown_all method docstring

Unbind all mouse down events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mousedown(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mousedown_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mousedown(on_mousedown)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mousemove method docstring

Unbind a specified handler's mouse move event.<hr>

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

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mousemove_all method docstring

Unbind all mouse move events.<hr>

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

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mouseout method docstring

Unbind a specified handler's mouse out event.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseout_all method docstring

Unbind all mouse out events.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover method docstring

Unbind a specified handler's mouseover event.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover_all method docstring

Unbind all mouseover events.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseup method docstring

Unbind a specified handler's mouse-up event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup(on_mouseup)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mouseup_all method docstring

Unbind all mouse up events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

## MouseMoveInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_mouse_move_handlers_if_not_initialized method docstring

Initialize _mouse_move_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### mousemove method docstring

Add mouse move event listener setting.<hr>

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

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_mousemove method docstring

Unbind a specified handler's mouse move event.<hr>

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

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

### unbind_mousemove_all method docstring

Unbind all mouse move events.<hr>

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

<hr>

**[References]**

- [Mousemove interface document](https://simon-ritchie.github.io/apysc/mousemove.html)

## MouseOutInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_mouse_out_handlers_if_not_initialized method docstring

Initialize _mouse_out_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### mouseout method docstring

Add mouse out event listener setting.<hr>

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

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_mouseout method docstring

Unbind a specified handler's mouse out event.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseout_all method docstring

Unbind all mouse out events.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

## MouseOverInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_mouse_over_handlers_if_not_initialized method docstring

Initialize _mouse_over_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### mouseover method docstring

Add mouse over event listener setting.<hr>

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

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)
- [About the handler options' type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_mouseover method docstring

Unbind a specified handler's mouseover event.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

### unbind_mouseover_all method docstring

Unbind all mouseover events.<hr>

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

<hr>

**[References]**

- [Mouseover and mouseout interfaces](https://simon-ritchie.github.io/apysc/mouseover_and_mouseout.html)

## MouseUpInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _append_mouse_event_binding_expression method docstring

Append a mouse event binding expression.<hr>

**[Parameters]**

- `name`: str
  - Handler's name.
- `mouse_event_type`: MouseEventType
  - Event type to bind.

### _initialize_mouse_up_handlers_if_not_initialized method docstring

Initialize _mouse_up_handlers attribute if it is not initialized yet.

### _set_mouse_event_handler_data method docstring

Set a handler's data to the given dictionary.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable would be called when event is dispatched.
- `handlers_dict`: dict
  - Dictionary to be set handler's data.
- `options`: dict or None
  - Optional arguments dictionary to be passed to handler.

### _unbind_all_mouse_events method docstring

Unbind specified all mouse event type's event.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### _unbind_mouse_event method docstring

Unbind specified handler's mouse event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.
- `mouse_event_type`: MouseEventType
  - Event type to unbind.
- `handlers_dict`: dict
  - Dictionary that has handler's data.

### mouseup method docstring

Add mouse up event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that would be called when mouse-up on this instance.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)
- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

### unbind_mouseup method docstring

Unbind a specified handler's mouse-up event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup(on_mouseup)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)

### unbind_mouseup_all method docstring

Unbind all mouse up events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_mouseup(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.mouseup(on_mouseup)
```

<hr>

**[References]**

- [Mousedown and mouseup interfaces document](https://simon-ritchie.github.io/apysc/mousedown_and_mouseup.html)