# Common mouse event interfaces

This page will explain the common mouse event interfaces, like `this`, .

## Basic binding usage

Each mouse event binding interface accepts `handler` and `options` arguments. The `handler` argument is a callable called when the target event is dispatched.

The `options` argument is an optional parameter dictionary to be passed to the handler. This argument can be skipped.

For instance, the `click` event can be set as follows:

```py
# runnable
from typing import Any, Dict

from apysc import Sprite
from apysc import Stage
from apysc import Rectangle
from apysc import MouseEvent
from apysc import String
from apysc import save_expressions_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')


def on_rectangle_click(e: MouseEvent, options: Dict[str, Any]) -> None:
    """
    The handler that will be called when the rectangle is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments.
    """
    # Change the clicked rectangle color to the passed color.
    rectangle: Rectangle = e.this
    color: String = String(options['color'])
    rectangle.fill_color = color


rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(
    handler=on_rectangle_click,
    options={'color': '#f0a'})

save_expressions_overall_html(
    dest_dir_path='mouse_event_common_basic_binding_usage/')
```

If you click the following rectangle, the rectancle color will be changed to the specified options color.

<iframe src="static/mouse_event_common_basic_binding_usage/index.html" width="150" height="150"></iframe>
