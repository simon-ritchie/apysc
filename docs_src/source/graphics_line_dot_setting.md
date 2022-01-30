# Graphics line_dot_setting interface

This page explains the `Graphics` class `line_dot_setting` property interface.

## What interface is this?

The `line_dot_setting` property interface updates or gets the instance's current line dot setting.

## Basic usage

The getter or setter interface value becomes (or requires) the `LineDotSetting` instance value.

The following example sets the 5-pixel dot to the line:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=250, stage_height=100, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.line_style(color='#0af', thickness=5)

line: ap.Line = sprite.graphics.draw_line(
    x_start=50, y_start=50, x_end=200, y_end=50)
line.line_dot_setting = ap.LineDotSetting(dot_size=5)

ap.save_overall_html(
    dest_dir_path='./graphics_line_dot_setting_basic_usage/')
```

<iframe src="static/graphics_line_dot_setting_basic_usage/index.html" width="250" height="100"></iframe>

## See also

- [Graphics class line style interface](graphics_line_style.md)


## line_dot_setting property API

<!-- Docstring: apysc._display.line_dot_setting_interface.LineDotSettingInterface.line_dot_setting -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get this instance's line dot setting.<hr>

**[Returns]**

- `line_dot_setting`: LineDotSetting or None
  - Lien dot setting.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=10)
>>> line: ap.Line = sprite.graphics.draw_line(
...     x_start=50, y_start=50, x_end=150, y_end=50)
>>> line.line_dot_setting = ap.LineDotSetting(dot_size=5)
>>> line.line_dot_setting.dot_size
Int(5)
```