# `apysc._display.line_round_dot_setting` docstrings

## Module summary

This module is the round-dot settings' class implementation for a line.

## `LineRoundDotSetting` class docstring

Round dot setting class for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_round_dot_setting = ap.LineRoundDotSetting(
...     round_size=10, space_size=5
... )
>>> line.line_round_dot_setting.round_size
Int(10)

>>> line.line_round_dot_setting.space_size
Int(5)
```

<hr>

**[References]**

- [Graphics line_style interface](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)

### `__init__` method docstring

Round dot setting class for line.<hr>

**[Parameters]**

- `round_size`: int or Int
  - Dot round size.
- `space_size`: int or Int
  - Blank space size between dots.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_round_dot_setting = ap.LineRoundDotSetting(
...     round_size=10, space_size=5
... )
>>> line.line_round_dot_setting.round_size
Int(10)

>>> line.line_round_dot_setting.space_size
Int(5)
```

<hr>

**[References]**

- [Graphics line_style interface](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)