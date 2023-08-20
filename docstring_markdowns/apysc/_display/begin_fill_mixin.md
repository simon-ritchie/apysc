# `apysc._display.begin_fill_mixin` docstrings

## Module summary

Class implementation for begin_fill method-related mix-in.

## `BeginFillMixIn` class docstring

### `_initialize_fill_alpha_if_not_initialized` method docstring

Initialize the fill_alpha attribute if this interface does not initialize it yet.

### `_initialize_fill_color_if_not_initialized` method docstring

Initialize the fill_color attribute if this interface does not initialize it yet.

### `_make_snapshot` method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `begin_fill` method docstring

Set single color value for fill.<hr>

**[Parameters]**

- `color`: Color
  - A color setting.
- `alpha`: float or Number, default 1.0
  - Color opacity (0.0 to 1.0).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage(
...     stage_width=150,
...     stage_height=150,
...     background_color=ap.Color("#333"),
...     stage_elem_id="stage",
... )
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(
...     color=ap.Color("#0af"),
...     alpha=0.5,
... )
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> rectangle.fill_color
Color("#00aaff")

>>> rectangle.fill_alpha
Number(0.5)
```

<hr>

**[References]**

- [Graphics begin_fill interface](https://simon-ritchie.github.io/apysc/en/graphics_begin_fill.html)