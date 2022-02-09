# apysc._event.mouse_down_interface docstrings

## Module summary

Class implementation for mouse down interface.

## MouseDownInterface class docstring



### _initialize_mouse_down_handlers_if_not_initialized method docstring

Initialize _mouse_down_handlers attribute if it is not initialized yet.

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