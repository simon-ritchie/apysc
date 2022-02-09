# `apysc._event.mouse_event` docstrings

## Module summary

Class implementation for the mouse event.

## `MouseEvent` class docstring

Mouse event class.<hr>

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

- [Basic mouse event interfaces](https://simon-ritchie.github.io/apysc/mouse_event_basic.html)

### `__init__` method docstring

Mouse event class.<hr>

**[Parameters]**

- `this`: VariableNameInterface
  - Instance that listening event (e.g., Sprite).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> e: ap.MouseEvent = ap.MouseEvent(this=rectangle)
```

<hr>

**[References]**

- [Basic mouse event interfaces](https://simon-ritchie.github.io/apysc/mouse_event_basic.html)

### `_append_local_x_getter_expression` method docstring

Append local_x getter property expression.<hr>

**[Parameters]**

- `x`: Int
  - Target x-coordinate value.

### `_append_local_y_getter_expression` method docstring

Append local_y getter property expression.<hr>

**[Parameters]**

- `y`: Int
  - Target y-coordinate value.

### `_append_stage_x_getter_expression` method docstring

Append stage_x getter property expression.<hr>

**[Parameters]**

- `x`: Int
  - Target x-coordinate value.

### `_append_stage_y_getter_expression` method docstring

Append stage_y getter property expression.<hr>

**[Parameters]**

- `y`: Int
  - Target y-coordinate value.