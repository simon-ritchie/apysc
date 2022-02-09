# apysc._event.mouse_over_interface docstrings

## Module summary

Class implementation for mouse over interface.

### _initialize_mouse_over_handlers_if_not_initialized method docstring

Initialize _mouse_over_handlers attribute if it is not initialized yet.

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