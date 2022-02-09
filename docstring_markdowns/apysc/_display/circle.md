# apysc._display.circle docstrings

## Module summary

Implementations of Circle class.

## Circle class docstring

The circle vector graphics class.

The circle vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> circle.x
Int(100)

>>> circle.y
Int(100)

>>> circle.radius
Int(50)

>>> circle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_circle interface document](https://simon-ritchie.github.io/apysc/graphics_draw_circle.html)

### __init__ method docstring

Create a circle vector graphics.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphics.
- `x`: int or Int
  - X-coordinate of the circle center.
- `y`: int or Int
  - Y-coordinate of the circle center.
- `radius`: int or Int
  - Circle radius.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> circle.x
Int(100)

>>> circle.y
Int(100)

>>> circle.radius
Int(50)

>>> circle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_circle interface document](https://simon-ritchie.github.io/apysc/graphics_draw_circle.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Circle('<variable_name>')`).

### _append_constructor_expression method docstring

Append a construcor expression.

### _set_center_coordinates method docstring

Set a center x-coordinate and a center y-coordinate.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the circle center.
- `y`: int or Int
  - Y-coordinate of the circle center.