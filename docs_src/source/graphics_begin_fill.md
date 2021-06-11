# Graphics begin_fill interface

This page will explain the `Graphics` class `begin_fill` method interface.

## What interface is this?

`begin_fill` interface will set the fill color and fill alpha settings. This setting will be maintained until it is called again or called the `clear` method.

## Basic usage

Draw vector graphics interfaces (e.g., `draw_rect`) will use these fill settings when they are creating, so the `begin_fill` method needs to be called before calling each drawing interface.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=350,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

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

save_overall_html(
    dest_dir_path='graphics_begin_fill_basic_usage/')
```

<iframe src="static/graphics_begin_fill_basic_usage/index.html" width="350" height="150"></iframe>

## Fill color setting

A fill color can be set by the `color` argument, and this is required.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

# Set a cyan fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

save_overall_html(
    dest_dir_path='graphics_begin_fill_fill_color/')
```

<iframe src="static/graphics_begin_fill_fill_color/index.html" width="150" height="150"></iframe>

If you want to clear fill color, then specify a blank string to this argument.

For example, since the following code will clear fill color setting, so a result rectangle graphic is invisible.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

sprite.graphics.begin_fill(color='#0af')

# Clear fill color by specifying blank string.
sprite.graphics.begin_fill(color='')

# Since fill color is not set, the rectangle is invisible.
sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

save_overall_html(
    dest_dir_path='graphics_begin_fill_color_setting_clear/')
```

<iframe src="static/graphics_begin_fill_color_setting_clear/index.html" width="150" height="150"></iframe>

Color code is acceptable like the following list:

- Six characters, e.g., `#00aaff`.
- Three characters, e.g., `#0af` (this will be interpreted as `#00aaff`).
- Single character, e.g., `#5` (this will be interpreted as `#000005`).
- Skipped `#` symbol, e.g., `0af` (this will be interpreted as `#00aaff`).
- Blank string, e.g., `''` (this will clear fill color setting).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=450,
    stage_height=150,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

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

save_overall_html(
    dest_dir_path='graphics_begin_fill_acceptable_color_settings/')
```

<iframe src="static/graphics_begin_fill_acceptable_color_settings/index.html" width="450" height="150"></iframe>

## Fill color alpha (opacity) setting

Fill color alpha (opacity) can be set by the `alpha` argument. It can accept 0.0 (transparent) to 1.0 (opaque).

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')
sprite: Sprite = Sprite(stage=stage)

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

save_overall_html(
    dest_dir_path='graphics_begin_fill_alpha_setting/')
```

<iframe src="static/graphics_begin_fill_alpha_setting/index.html" width="200" height="200"></iframe>
