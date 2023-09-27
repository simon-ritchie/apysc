# `apysc._display.line_dash_setting` docstrings

## Module summary

Dash setting class implementation for a line.

## `LineDashSetting` class docstring

Dash setting class for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50
... )
>>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```

<hr>

**[References]**

- [Graphics line_style interface](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)

### `__init__` method docstring

Dash setting class for a line.<hr>

**[Parameters]**

- `dash_size`: int or Int
  - Dash size.
- `space_size`: int or Int
  - Blank space size between dashes.
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
>>> line.line_dash_setting = ap.LineDashSetting(dash_size=5, space_size=2)
>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```

<hr>

**[References]**

- [Graphics line_style interface](https://simon-ritchie.github.io/apysc/en/graphics_line_style.html)