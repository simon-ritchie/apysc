# Sprite

This page will explain the `Sprite` class.

## What is the Sprite?

The `Sprite` class is the container of each `DisplayObject` instance. It also has the `Graphics` class interfaces and can draw each vector graphic.

## graphics attribute interfaces

The `Sprite` instance has the `graphics` attribute and you can draw each vector graphic with it. For example, the following code will draw the cyan color rectangle.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(
    dest_dir_path='sprite_graphics_attribute/')
```

<iframe src="static/sprite_graphics_attribute/index.html" width="150" height="150"></iframe>

For more details, please see the `Graphics` related documents, for example:

- [Graphics class](graphics.md)
- [Graphics class begin fill interface](graphics_begin_fill.md)
- [Graphics class line style interface](graphics_line_style.md)
- [Graphics class draw rect interface](graphics_draw_rect.md)
- [Graphics class draw circle interface](graphics_draw_circle.md)

## Move DisplayObject instances simultaneously

The `Sprite` class is a container and if you move that coordinates, then children's coordinates will be changed simultaneously. For example, the following code will change the sprite y-coordinate when you click the rectangle.

```py
# runnable
from typing import Any, Dict

import apysc as ap


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: Dict[Any, Any]) -> None:
    """
    The handler would be called when the sprite instance is clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    sprite.y += 50


stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=250,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_sprite_click)

ap.save_overall_html(
    dest_dir_path='sprite_move_instances_simultaneously/')
```

<iframe src="static/sprite_move_instances_simultaneously/index.html" width="250" height="250"></iframe>

The subsequent pages will explain the other interfaces, such as the `add_child` interface.

## See also

- [Sprite class add child and remove child interfaces](sprite_add_child_and_remove_child.md)
- [Sprite class contains interface](sprite_contains.md)
- [Sprite class num children interface](sprite_num_children.md)
- [Sprite class get child at interface](sprite_get_child_at.md)
