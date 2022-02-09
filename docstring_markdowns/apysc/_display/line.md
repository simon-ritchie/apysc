# apysc._display.line docstrings

## Module summary

Implementations of the Line class.

## Line class docstring

The line vector graphics class.

The line vector graphics class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics draw_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_line.html)
- [Graphics draw_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dotted_line.html)
- [Graphics draw_dashed_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dashed_line.html)
- [Graphics draw_round_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_round_dotted_line.html)
- [Graphics draw_dash_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html)

### __init__ method docstring

Create a line vector graphics.<hr>

**[Parameters]**

- `parent`: Graphics
  - Graphics instance to link this graphic.
- `start_point`: Points2D
  - Line start point.
- `end_point`: Points2D
  - Line end point.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics draw_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_line.html)
- [Graphics draw_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dotted_line.html)
- [Graphics draw_dashed_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dashed_line.html)
- [Graphics draw_round_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_round_dotted_line.html)
- [Graphics draw_dash_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html)

### __repr__ method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Line('<variable_name>')`).

### _append_constructor_expression method docstring

Append a constructor expression.

### _make_points_expression method docstring

Make line start and end expression str.<hr>

**[Returns]**

- `expression`: str
  - Each points expression.