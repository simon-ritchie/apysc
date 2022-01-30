# Graphics begin_fill interface

This page explains the `Graphics` class `begin_fill` method interface.

## What interface is this?

`begin_fill` interface would set the fill color and fill alpha settings. This setting would be maintained until it is called again or called the `clear` method.

## Basic usage

Draw vector graphics interfaces (e.g., `draw_rect`) would use these fill settings when creating, so the `begin_fill` method needs to be called before calling each drawing interface.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set blue fill color and draw the first rectangle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Draw the second rectangle (fill color setting will be maintained).
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

# Set the other fill color and draw the third rectangle.
sprite.graphics.begin_fill(color='#f0a')
sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_basic_usage/')
```

<iframe src="static/graphics_begin_fill_basic_usage/index.html" width="350" height="150"></iframe>

## Fill color setting

The `color` argument sets the fill color, and the `begin_fill` interface requires this argument.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set a cyan fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_fill_color/')
```

<iframe src="static/graphics_begin_fill_fill_color/index.html" width="150" height="150"></iframe>

If you want to clear fill color, specify a blank string to this argument.

For example, since the following code clears fill color settings, a rectangle graphic becomes invisible.

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

# Clear fill color by specifying blank string.
sprite.graphics.begin_fill(color='')

# Since fill color is not set, the rectangle is invisible.
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_color_setting_clear/')
```

<iframe src="static/graphics_begin_fill_color_setting_clear/index.html" width="150" height="150"></iframe>

Color code is acceptable like the following list:

- Six characters, e.g., `#00aaff`.
- Three characters, e.g., `#0af` (this becomes `#00aaff`).
- Single character, e.g., `#5` (this becomes `#000005`).
- Skipped `#` symbol, e.g., `0af` (this becomes `#00aaff`).
- Blank string, e.g., `''` (this setting clears the fill color setting).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=450,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Six characters fill color setting (a cyan color).
sprite.graphics.begin_fill(color='#00aaff')
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Three characters fill color setting (a magenta color).
sprite.graphics.begin_fill(color='#f0a')
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

# Single characters fill color setting (a black color).
sprite.graphics.begin_fill(color='#0')
sprite.graphics.draw_rect(
    x=250, y=50, width=50, height=50)

# Fill color that Skipped `#` symbol is also acceptable.
sprite.graphics.begin_fill(color='999')
sprite.graphics.draw_rect(
    x=350, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_acceptable_color_settings/')
```

<iframe src="static/graphics_begin_fill_acceptable_color_settings/index.html" width="450" height="150"></iframe>

## Fill color alpha (opacity) setting

Fill color alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

sprite.graphics.begin_fill(color='#00aaff', alpha=0.2)
sprite.graphics.draw_rect(
    x=50, y=75, width=50, height=50)
sprite.graphics.draw_rect(
    x=75, y=50, width=50, height=50)
sprite.graphics.draw_rect(
    x=75, y=75, width=50, height=50)
sprite.graphics.draw_rect(
    x=75, y=100, width=50, height=50)
sprite.graphics.draw_rect(
    x=100, y=75, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_begin_fill_alpha_setting/')
```

<iframe src="static/graphics_begin_fill_alpha_setting/index.html" width="200" height="200"></iframe>


## begin_fill API

<!-- Docstring: apysc._display.begin_fill_interface.BeginFillInterface.begin_fill -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `begin_fill(self, color:~StrOrString, *, alpha:Union[float, apysc._type.number.Number]=1.0) -> None`<hr>

**[Interface summary]** Set single color value for fill.<hr>

**[Parameters]**

- `color`: str or String
  - Hexadecimal color string. e.g., '#00aaff'
- `alpha`: float or Number, default 1.0
  - Color opacity (0.0 to 1.0).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color
String('#00aaff')
```

## fill_color property API

<!-- Docstring: apysc._display.begin_fill_interface.BeginFillInterface.fill_color -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get current fill color.<hr>

**[Returns]**

- `fill_color`: String
  - Current fill color (hexadecimal string, e.g., '#00aaff'). If not be set, this interface returns a blank string.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_color
String('#00aaff')
```

## fill_alpha property API

<!-- Docstring: apysc._display.begin_fill_interface.BeginFillInterface.fill_alpha -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get current fill color opacity.<hr>

**[Returns]**

- `fill_alpha`: Number
  - Current fill color opacity (0.0 to 1.0). If not be set, 1.0 will be returned.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle.fill_alpha
Number(0.5)
```