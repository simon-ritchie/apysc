# Graphics draw_ellipse interface

This page will explain the `Graphics` class `draw_ellipse` method interface.

## What interface is this?

`draw_ellipse` interface will draw the vector ellipse graphics.

## Basic usage

`draw_ellipse` interface has the `x`, `y`, `width`, and `height` arguments. The `x` and the `y` arguments are the ellipse center coordinates. The `width` and the `height` arguments are the ellipse size. These sizes are twice the size of the radius.

```py
# runnable
from apysc import Sprite
from apysc import Stage
from apysc import LineDotSetting
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=325,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)

# Set the cyan fill color and draw the ellipse.
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_ellipse(x=125, y=100, width=150, height=100)

# Set the only dotted-line style and draw the ellipse.
sprite.graphics.begin_fill(color='')
sprite.graphics.line_style(
    color='#fff', thickness=3, dot_setting=LineDotSetting(dot_size=3))
sprite.graphics.draw_ellipse(x=200, y=100, width=150, height=100)

save_overall_html(
    dest_dir_path='graphics_draw_ellipse_basic_usage/')
```

<iframe src="static/graphics_draw_ellipse_basic_usage/index.html" width="325" height="200"></iframe>

## Return value

The return value of the `draw_ellipse` interface is the instance of the `Ellipse` class.

It has the basic interfaces (like the `x` or the `width` attributes) similar to the other graphics classes.

The following code example will bind the click event handler and if you click the ellipse the width and height will be widening.

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Ellipse
from apysc import MouseEvent
from apysc import LineDotSetting
from apysc import save_overall_html


def on_ellipse_click(
        e: MouseEvent[Ellipse], options: Dict[str, Any]) -> None:
    """
    The handler would be called when the ellipse is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ellipse: Ellipse = e.this
    ellipse.width += 15
    ellipse.height += 10


stage: Stage = Stage(
    background_color='#333',
    stage_width=250,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)

sprite.graphics.begin_fill(color='#0af')
ellipse: Ellipse = sprite.graphics.draw_ellipse(
    x=125, y=100, width=150, height=100)
ellipse.click(on_ellipse_click)

save_overall_html(
    dest_dir_path='graphics_draw_ellipse_return_value/')
```

<iframe src="static/graphics_draw_ellipse_return_value/index.html" width="250" height="200"></iframe>
