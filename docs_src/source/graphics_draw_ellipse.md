# Graphics draw_ellipse interface

This page explains the `Graphics` class `draw_ellipse` method interface.

## What interface is this?

The `draw_ellipse` interface draws the vector ellipse graphics.

## Basic usage

The `draw_ellipse` interface has the `x`\, `y`\, `width`\, and `height` arguments. The `x` and `y` arguments are the ellipse center coordinates. The `width` and `height` arguments are the ellipse size. These sizes are twice the size of the radius.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=325,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

# Set the cyan fill color and draw the ellipse.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)

# Set the only dotted-line style and draw the ellipse.
sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(
    color='#fff', thickness=3, dot_setting=ap.LineDotSetting(dot_size=3))
sprite.graphics.draw_ellipse(x=200, y=100, width=150, height=100)

ap.save_overall_html(
    dest_dir_path='graphics_draw_ellipse_basic_usage/')
```

<iframe src="static/graphics_draw_ellipse_basic_usage/index.html" width="325" height="200"></iframe>

## Return value

The return value of the `draw_ellipse` interface is the instance of the `Ellipse` class.

It has the basic interfaces (like the `x` or the `width` attributes) similar to the other graphics classes.

The following code example binds the click event handler. If you click the ellipse, the width and height become wider.

```py
# runnable
import apysc as ap


def on_ellipse_click(
        e: ap.MouseEvent[ap.Ellipse], options: dict) -> None:
    """
    The handler that the ellipse calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ellipse: ap.Ellipse = e.this
    ellipse.width += 15
    ellipse.height += 10


ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#0af')
ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
    x=125, y=100, width=150, height=100)
ellipse.click(on_ellipse_click)

ap.save_overall_html(
    dest_dir_path='graphics_draw_ellipse_return_value/')
```

<iframe src="static/graphics_draw_ellipse_return_value/index.html" width="250" height="200"></iframe>


## draw_ellipse API

<!-- Docstring: apysc._display.graphics.Graphics.draw_ellipse -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_ellipse(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], width:Union[int, apysc._type.int.Int], height:Union[int, apysc._type.int.Int]) -> '_ellipse.Ellipse'`<hr>

**[Interface summary]** Draw a ellipse vector graphics.<hr>

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