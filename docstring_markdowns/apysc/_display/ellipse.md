# `apysc._display.ellipse` docstrings

## Module summary

Implementation of the Ellipse class.

## `Ellipse` class docstring

The ellipse vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=100, y=100, width=80, height=50)
>>> ellipse.x
Int(100)

>>> ellipse.y
Int(100)

>>> ellipse.width
Int(80)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_ellipse interface](https://simon-ritchie.github.io/apysc/graphics_draw_ellipse.html)

### `__init__` method docstring

Create an ellipse vector graphic.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.
- `x`: Int or int
  - X-coordinate of the ellipse center.
- `y`: Int or int
  - Y-coordinate of the ellipse center.
- `width`: Int or int
  - Ellipse width.
- `height`: Int or int
  - Ellipse height.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=100, y=100, width=80, height=50)
>>> ellipse.x
Int(100)

>>> ellipse.y
Int(100)

>>> ellipse.width
Int(80)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_ellipse interface](https://simon-ritchie.github.io/apysc/graphics_draw_ellipse.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Ellipse('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append a constructor expression.