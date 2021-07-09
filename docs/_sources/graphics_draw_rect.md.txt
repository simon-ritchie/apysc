# Graphics draw_rect interface

This page will explain the `Graphics` class `draw_rect` method interface.

## What interface is this?

`draw_rect` interface will draw vector rectangle graphics.

## Basic usage

`draw_rect` interface has `x`, `y`, `width`, and `height` arguments. `x` and `y` are rectangle coordinates setting, and `width` and `height` will determine rectangle size.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=100, height=50)

ap.save_overall_html(dest_dir_path='graphics_draw_rect_basic_usage/')
```

The previous script will draw horizontal rectangle graphics.

<iframe src="static/graphics_draw_rect_basic_usage/index.html" width="200" height="150"></iframe>

Notes: `begin_fill` call (fill color setting) is necessary before `draw_rect` interface call. If it is skipped, nothing will be displayed on stage.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.draw_rect(x=50, y=50, width=100, height=50)

ap.save_overall_html(
    dest_dir_path='graphics_draw_rect_basic_usage_skipped_begin_fill/')
```

<iframe src="static/graphics_draw_rect_basic_usage_skipped_begin_fill/index.html" width="200" height="150"></iframe>

## Rectangle instance

`draw_rect` interface will return `Rectangle` instance. You can update each setting or bind events.

For instance, the following script will set the mouse event to `Rectangle` and updating x position in the handler (`on_click`).

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: Dict[str, Any]) -> None:
    """
    The handler that it will be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Created event instance.
    options : dict
        Optional arguments.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.x = ap.Int(100)


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='graphics_draw_rect_rectangle/')
```

If you click rectangle, x position will be changed to 100.

<iframe src="static/graphics_draw_rect_rectangle/index.html" width="200" height="150"></iframe>
