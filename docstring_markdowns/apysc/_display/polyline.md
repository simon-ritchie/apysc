# apysc._display.polyline docstrings

## Module summary

Implementations of Polyline class.

## Polyline class docstring

The polyline vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> _ = sprite.graphics.move_to(x=50, y=50)
>>> polyline: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> polyline.line_color
String('#ffffff')

>>> polyline.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics move_to and line_to interfaces document](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html)

### __init__ method docstring

Create a polyline vector graphic.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.
- `points`: Array of Point2D
  - List of line points.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> _ = sprite.graphics.move_to(x=50, y=50)
>>> polyline: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> polyline.line_color
String('#ffffff')

>>> polyline.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics move_to and line_to interfaces document](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Polyline('<variable_name>')`).

### _append_constructor_expression method docstring

Append constructor expression.