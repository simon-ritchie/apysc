# Graphics line_thickness interface

This page explains the `Graphics` class `line_thickness` property interface.

## What interface is this?

The `line_thickness` property interface updates or get the instance's line thickness (line width).

## Basic usage

The getter or setter interface value becomes (or requires) the `Int` value.

The following example sets the 5-pixel line thickness to the first rectangle and the 10-pixel line thickness to the second one:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=1)

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle_1.line_thickness = ap.Int(5)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.line_thickness = ap.Int(10)

ap.save_overall_html(
    dest_dir_path='./graphics_line_thickness_basic_usage/')
```

<iframe src="static/graphics_line_thickness_basic_usage/index.html" width="250" height="150"></iframe>


## line_thickness property API

<!-- Docstring: apysc._display.line_thickness_interface.LineThicknessInterface.line_thickness -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get this instance's line thickness.<hr>

**[Returns]**

- `line_thickness`: Int
  - Current line thickness.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(
...     color='#fff', thickness=5)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_thickness
Int(5)
```