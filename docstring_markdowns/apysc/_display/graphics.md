# `apysc._display.graphics` docstrings

## Module summary

Implementations for Graphics class.

## `Graphics` class docstring

Create an object that has each vector graphics interface.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.x
Int(50)

>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> circle.x
Int(100)
```

<hr>

**[References]**

- [Graphics document](https://simon-ritchie.github.io/apysc/graphics.html)

### `__init__` method docstring

Create an object that has each vector graphics interface.<hr>

**[Parameters]**

- `parent`: Sprite
  - A parent instance.
- `variable_name`: str or None, default None
  - Variable name to set. Specified only when a subclass instantiation.

<hr>

**[References]**

- [Graphics document](https://simon-ritchie.github.io/apysc/graphics.html)

### `__repr__` method docstring

Get a string representation of this instance (for the sake of debugging).<hr>

**[Returns]**

- `repr_str`: str
  - Type name and variable name will be set (e.g., `Graphics('<variable_name>')`).

### `_append_constructor_expression` method docstring

Append constructor expression.

### `_reset_each_line_settings` method docstring

Reset each line settings (e.g., LineDotSetting, LineDashSetting, and so on).<hr>

**[Notes]**

This interface does not append an expression.

### `draw_circle` method docstring

Draw a circle vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate of the circle center.
- `y`: Int or int
  - Y-coordinate of the circle center.
- `radius`: Int or int
  - Circle radius.

<hr>

**[Returns]**

- `circle`: Circle
  - Created circle graphics instance.

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

### `draw_dash_dotted_line` method docstring

Draw a dash-dotted (1-dot chain) line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `dot_size`: Int or int
  - Dot size.
- `dash_size`: Int or int
  - Dash size.
- `space_size`: Int or int
  - Blank space size between dots and dashes.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dash_dotted_line(
...    x_start=50, y_start=50, x_end=150, y_end=50,
...    dot_size=2, dash_size=5, space_size=3)
>>> line.line_color
String('#ffffff')

>>> line.line_dash_dot_setting.dot_size
Int(2)

>>> line.line_dash_dot_setting.dash_size
Int(5)

>>> line.line_dash_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics draw_dash_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dash_dotted_line.html)

### `draw_dashed_line` method docstring

Draw a dashed line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `dash_size`: Int or int
  - Dash size.
- `space_size`: Int or int
  - Blank space size between dashes.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDotSetting`, except `LineDashSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dashed_line(
...     x_start=50, y_start=50, x_end=150, y_end=50,
...     dash_size=5, space_size=2)
>>> line.line_color
String('#ffffff')

>>> line.line_dash_setting.dash_size
Int(5)

>>> line.line_dash_setting.space_size
Int(2)
```

<hr>

**[References]**

- [Graphics draw_dashed_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dashed_line.html)

### `draw_dotted_line` method docstring

Draw a dotted line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `dot_size`: Int or int
  - Dot size.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDashSetting`, except `LineDotSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_dotted_line(
...     x_start=50, y_start=50, x_end=150, y_end=50, dot_size=5)
>>> line.line_color
String('#ffffff')

>>> line.line_thickness
Int(5)

>>> line.line_dot_setting.dot_size
Int(5)
```

<hr>

**[References]**

- [Graphics draw_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_dotted_line.html)

### `draw_ellipse` method docstring

Draw an ellipse vector graphic.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate of the ellipse center.
- `y`: Int or int
  - Y-coordinate of the ellipse center.
- `width`: Int or int
  - Ellipse width.
- `height`: Int or int
  - Ellipse height.

<hr>

**[Returns]**

- `ellipse`: Ellipse
  - Created ellipse graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=100, y=100, width=100, height=50)
>>> ellipse.x
Int(100)

>>> ellipse.y
Int(100)

>>> ellipse.width
Int(100)

>>> ellipse.height
Int(50)

>>> ellipse.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_ellipse interface](https://simon-ritchie.github.io/apysc/graphics_draw_ellipse.html)

### `draw_line` method docstring

Draw a normal line vector graphic.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

 ・This interface ignores line settings, like the `LineDotSetting`, `LineDashSetting`.<hr>

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

### `draw_path` method docstring

Draw a path vector graphics.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.

<hr>

**[Returns]**

- `path`: Path
  - Created path graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...     ])
```

### `draw_polygon` method docstring

Draw a polygon vector graphic. This interface is similar to the Polyline class (created by `move_to` or `line_to`). But unlike that, this interface connects the last point and the start point.<hr>

**[Parameters]**

- `points`: list of Point2D or Array.
  - Polygon vertex points.

<hr>

**[Returns]**

- `polygon`: Polygon
  - Created polygon graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> polygon: ap.Polygon = sprite.graphics.draw_polygon(
...     points=[
...         ap.Point2D(x=25, y=0),
...         ap.Point2D(x=0, y=50),
...         ap.Point2D(x=50, y=50),
...     ])
>>> polygon.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_polygon interface document](https://simon-ritchie.github.io/apysc/graphics_draw_polygon.html)

### `draw_rect` method docstring

Draw a rectangle vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X position to start drawing.
- `y`: Int or int
  - Y position to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.

<hr>

**[Returns]**

- `rectangle`: Rectangle
  - Created rectangle.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.x
Int(50)

>>> rectangle.width
Int(50)

>>> rectangle.fill_color
String('#00aaff')
```

<hr>

**[References]**

- [Graphics draw_rect interface document](https://simon-ritchie.github.io/apysc/graphics_draw_rect.html)

### `draw_round_dotted_line` method docstring

Draw a round-dotted line vector graphics.<hr>

**[Parameters]**

- `x_start`: Int or int
  - Line start x-coordinate.
- `y_start`: Int or int
  - Line start y-coordinate.
- `x_end`: Int or int
  - Line end x-coordinate.
- `y_end`: Int or int
  - Line end y-coordinate.
- `round_size`: Int or int
  - Dot round size.
- `space_size`: Int or int
  - Blank space size between dots.

<hr>

**[Returns]**

- `line`: Line
  - Created line graphics instance.

<hr>

**[Notes]**

This interface ignores line settings, like the `LineDotSetting`, except `LineRoundDotSetting`.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_round_dotted_line(
...    x_start=50, y_start=50, x_end=150, y_end=50,
...    round_size=6, space_size=3)
>>> line.line_color
String('#ffffff')

>>> line.line_round_dot_setting.round_size
Int(6)

>>> line.line_round_dot_setting.space_size
Int(3)
```

<hr>

**[References]**

- [Graphics draw_round_dotted_line interface document](https://simon-ritchie.github.io/apysc/graphics_draw_round_dotted_line.html)

### `draw_round_rect` method docstring

Draw a rounded rectangle vector graphics.<hr>

**[Parameters]**

- `x`: Int or int
  - X-coordinate to start drawing.
- `y`: Int or int
  - Y-coordinate to start drawing.
- `width`: Int or int
  - Rectangle width.
- `height`: Int or int
  - Rectangle height.
- `ellipse_width`: Int or int
  - Ellipse width of the rectangle corner.
- `ellipse_height`: Int or int
  - Ellipse height of the rectangle corner.

<hr>

**[Returns]**

- `rectangle`: Rectangle
  - Created rectangle.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> round_rect: ap.Rectangle = sprite.graphics.draw_round_rect(
...     x=50, y=50, width=50, height=50,
...     ellipse_width=10, ellipse_height=15)
>>> round_rect.ellipse_width
Int(10)

>>> round_rect.ellipse_height
Int(15)
```

<hr>

**[References]**

- [Graphics draw_round_rect interface document](https://simon-ritchie.github.io/apysc/graphics_draw_round_rect.html)

### `line_to` method docstring

Draw a line from previous point to specified point (initial point is x = 0, y = 0).<hr>

**[Parameters]**

- `x`: Int or int
  - X destination point to draw a line.
- `y`: Int or int
  - Y destination point to draw a line.

<hr>

**[Returns]**

- `line`: Polyline
  - Line graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> line_3: ap.Polyline = sprite.graphics.line_to(x=50, y=150)
>>> line_1 == line_2 == line_3
True

>>> line_1.line_color
String('#ffffff')

>>> line_1.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics move_to and line_to interfaces document](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html)

### `move_to` method docstring

Move a line position to a specified point.<hr>

**[Parameters]**

- `x`: Int or int
  - X destination point to move.
- `y`: Int or int
  - Y destination point to move.

<hr>

**[Returns]**

- `line`: Polyline
  - Line graphics instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=5)
>>> line_1: ap.Polyline = sprite.graphics.move_to(x=50, y=50)
>>> line_2: ap.Polyline = sprite.graphics.line_to(x=150, y=50)
>>> line_1 == line_2
True

>>> line_1.line_color
String('#ffffff')

>>> line_1.line_thickness
Int(5)
```

<hr>

**[References]**

- [Graphics move_to and line_to interfaces document](https://simon-ritchie.github.io/apysc/graphics_move_to_and_line_to.html)