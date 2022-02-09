# apysc._event.double_click_interface docstrings

## Module summary

Class implementation for double click interface.

### _initialize_dblclick_handlers_if_not_initialized method docstring

Initialize _dblclick_handlers attribute if it is not initialized yet.

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