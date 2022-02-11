# `apysc._display.begin_fill_interface` docstrings

## Module summary

Class implementation for begin_fill method-related interface.

## `BeginFillInterface` class docstring

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

Revert values if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `begin_fill` method docstring

Set single color value for fill.<hr>

**[Parameters]**

- `color`: str or String
  - Hexadecimal color string. e.g., '#00aaff'
- `alpha`: float or Number, default 1.0
  - Color opacity (0.0 to 1.0).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics begin_fill interface document](https://simon-ritchie.github.io/apysc/graphics_begin_fill.html)