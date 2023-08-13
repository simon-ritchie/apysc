# `apysc._display.line_dot_setting` docstrings

## Module summary

Dot setting class implementation for a line.

## `LineDotSetting` class docstring

Dot setting class for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
>>> line.line_dot_setting.dot_size
Int(5)
```

<hr>

**[References]**

- [Graphics line_style interface](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)

### `__init__` method docstring

Dot setting class for a line.<hr>

**[Parameters]**

- `dot_size`: int or Int
  - Dot size.
- `variable_name_suffix`: str, default ''
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
>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
>>> line.line_dot_setting.dot_size
Int(5)
```

<hr>

**[References]**

- [Graphics line_style interface](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)