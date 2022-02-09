# `apysc._event.mouse_move_interface` docstrings

## Module summary

Class implementation for mouse move interface.

### `_initialize_mouse_move_handlers_if_not_initialized` method docstring

Initialize _mouse_move_handlers attribute if it is not initialized yet.

### `mousemove` method docstring

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

### `unbind_mousemove` method docstring

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

### `unbind_mousemove_all` method docstring

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