# `apysc._display.rectangle` docstrings

## Module summary

Implementations of the Rectangle class.

## `Rectangle` class docstring

The rectangle vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=100, height=75)
>>> rectangle.x
Int(50)

>>> rectangle.y
Int(50)

>>> rectangle.width
Int(100)

>>> rectangle.height
Int(75)

>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_rect interface document](https://simon-ritchie.github.io/apysc/graphics_draw_rect.html)

### `__init__` method docstring

Create a rectangle vector graphic.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this instance.
- `x`: Int or int
  - X-coordinate to start drawing.
- `y`: Int or int
  - Y-coordinate to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=100, height=75)
>>> rectangle.x
Int(50)

>>> rectangle.y
Int(50)

>>> rectangle.width
Int(100)

>>> rectangle.height
Int(75)

>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_rect interface document](https://simon-ritchie.github.io/apysc/graphics_draw_rect.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Rectangle('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_make_rect_attrs_expression` method docstring

Make rectangle attributes expression string.<hr>

**[Returns]**

- `rect_attrs_expression`: str
  - Rectangle attributes expression string.