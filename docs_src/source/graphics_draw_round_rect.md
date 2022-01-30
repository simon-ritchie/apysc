# Graphics draw_round_rect interface

This page explains the `Graphics` class `draw_round_rect` method interface.

## What interface is this?

`draw_round_rect` interface draws vector rounded rectangle graphics.

## Basic usage

`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates setting, and `width` and `height` will determine rectangle size.

This interface also has `ellipse_width` and `ellipse_height` arguments to set the round size to the rectangle corners.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

# Set 10-pixel ellipse size and draw the rectangle.
sprite.graphics.draw_round_rect(
    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)

# Set 20-pixel ellipse size and draw the rectangle.
sprite.graphics.draw_round_rect(
    x=150, y=50, width=50, height=50, ellipse_width=20, ellipse_height=20)

# Set 5-pixel ellipse width and 20-pixel ellipse height and
# draw the rectangle.
sprite.graphics.draw_round_rect(
    x=250, y=50, width=50, height=50, ellipse_width=5, ellipse_height=20)

ap.save_overall_html(
    dest_dir_path='graphics_draw_round_rect_basic_usage/')
```

<iframe src="static/graphics_draw_round_rect_basic_usage/index.html" width="350" height="150"></iframe>

## Return value

`draw_round_rect` interface will return the `Rectangle` instance, same as the `draw_rect` interface.

The `Rectangle` instance has the `ellipse_width` attribute and `ellipse_height` to change the rectangle round size.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle: ap.Rectangle = sprite.graphics.draw_round_rect(
    x=50, y=50, width=50, height=50, ellipse_width=10, ellipse_height=10)

# You can update the ellipse_width and ellipse_height
# attributes dynamically.
rectangle.ellipse_width = ap.Int(20)

ap.save_overall_html(
    dest_dir_path='graphics_draw_round_rect_return_value/')
```

<iframe src="static/graphics_draw_round_rect_return_value/index.html" width="150" height="150"></iframe>


## draw_round_rect API

<!-- Docstring: apysc._display.graphics.Graphics.draw_round_rect -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `draw_round_rect(self, x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], width:Union[int, apysc._type.int.Int], height:Union[int, apysc._type.int.Int], ellipse_width:Union[int, apysc._type.int.Int], ellipse_height:Union[int, apysc._type.int.Int]) -> apysc._display.rectangle.Rectangle`<hr>

**[Interface summary]** Draw a rounded rectangle vector graphics.<hr>

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