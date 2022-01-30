# Graphics fill_alpha interface

This page explains the `Graphics` class `fill_alpha` property interface.

## What interface is this?

The `fill_alpha` property interface updates or get the instance's fill alpha (opacity).

## Basic usage

The getter or setter interface value becomes (or require) the `Number` value (0.0 to 1.0).

The following example sets the 0.5 fill alpha to the second rectangle and 0.25 to the third rectangle:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=350, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')

rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
rectangle_2.fill_alpha = ap.Number(0.5)

rectangle_3: ap.Rectangle = sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)
rectangle_3.fill_alpha = ap.Number(0.25)

ap.save_overall_html(
    dest_dir_path='./graphics_fill_alpha_basic_usage/')
```

<iframe src="static/graphics_fill_alpha_basic_usage/index.html" width="350" height="150"></iframe>


## fill_alpha property API

<!-- Docstring: apysc._display.fill_alpha_interface.FillAlphaInterface.fill_alpha -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get this instance's fill opacity.<hr>

**[Returns]**

- `fill_alpha`: Number
  - Current fill opacity (0.0 to 1.0).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_alpha = ap.Number(0.5)
>>> rectangle.fill_alpha
Number(0.5)
```