# Graphics draw_circle interface

This page explains the `Graphics` class `draw_circle` method interface.

## What interface is this?

`draw_circle` interface draws the vector circle graphics.

## Basic usage

The `draw_circle` interface has the `x`\, `y`\, and `radius` arguments.

The `x` and `y` arguments are the circle center coordinates, and the radius argument determines the circle size. The width and height become twice the `radius` value.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=350,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

# Set the cyan color and draw the circle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_circle(x=100, y=100, radius=50)

# Set the dotted-line style and draw the circle.
sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(
    color='#fff', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))
sprite.graphics.draw_circle(x=250, y=100, radius=50)

# Draw the inner circle.
sprite.graphics.draw_circle(x=250, y=100, radius=25)

ap.save_overall_html(
    dest_dir_path='graphics_draw_circle_basic_usage/')
```

<iframe src="static/graphics_draw_circle_basic_usage/index.html" width="350" height="200"></iframe>

## Return value

The return value of the `draw_circle` interface is the instance of the `Circle` class.

It has the `radius` attribute or other basic interfaces and you can change these settings.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=400,
    stage_height=400,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

# Draw the small radius circle.
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=200, y=200, radius=25)

# Update circle radius to become the bigger one.
circle.radius = ap.Int(100)

ap.save_overall_html(
    dest_dir_path='graphics_draw_circle_return_value/')
```

<iframe src="static/graphics_draw_circle_return_value/index.html" width="400" height="400"></iframe>


## draw_circle API

<!-- Docstring: apysc._display.graphics.Graphics.draw_circle -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_circle(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], radius:Union[int, apysc._type.int.Int]) -> '_circle.Circle'`<hr>

**[Interface summary]** Draw a circle vector graphics.<hr>

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