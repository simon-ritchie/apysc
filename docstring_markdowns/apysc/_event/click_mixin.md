# `apysc._event.click_mixin` docstrings

## Module summary

Class implementation for click mix-in.

## `ClickMixIn` class docstring

### `_initialize_click_handlers_if_not_initialized` method docstring

Initialize the _click_handlers attribute if it hasn't been initialized yet.

### `click` method docstring

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
>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.x += 10
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface](https://simon-ritchie.github.io/apysc/en/click.html)
- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)

### `unbind_click` method docstring

Unbind specified handler's click event.<hr>

**[Parameters]**

- `handler`: _Handler
  - Unbinding target Callable.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
...     rectangle.unbind_click(on_click)
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface](https://simon-ritchie.github.io/apysc/en/click.html)

### `unbind_click_all` method docstring

Unbind all click events.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
...     rectangle.unbind_click_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Click interface](https://simon-ritchie.github.io/apysc/en/click.html)