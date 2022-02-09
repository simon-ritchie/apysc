# apysc._display.line_dash_dot_setting docstrings

## Module summary

Dash dot (1-dot chain) setting for line.

## LineDashDotSetting class docstring

Dash dot (1-dot chain) setting for a line.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dash_dot_setting = ap.LineDashDotSetting(
...     dot_size=2, dash_size=5, space_size=3)
>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics line_style interface document](https://simon-ritchie.github.io/apysc/graphics_line_style.html)

### __init__ method docstring

Dash dot (1-dot chain) setting for a line.<hr>

**[Parameters]**

- `dot_size`: int or Int
  - Dot size.
- `dash_size`: int or Int
  - Dash size.
- `space_size`: int or Int
  - Blank space size between dots and dashes.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dash_dot_setting = ap.LineDashDotSetting(
...     dot_size=2, dash_size=5, space_size=3)
>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics line_style interface document](https://simon-ritchie.github.io/apysc/graphics_line_style.html)