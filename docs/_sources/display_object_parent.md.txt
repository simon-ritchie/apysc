# Display object parent interfaces

This page will explain the `DisplayObject` class `parent` interfaces (the `parent` property and `remove_from_parent` method).

## What interfaces are these?

The `parent` attribute is the getter property. This will become a `Stage` instance or a container instance like a `Sprite` instance.

```py
# runnable
from apysc import Stage
from apysc import Sprite
from apysc import Rectangle
from apysc import Graphics

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

assert isinstance(sprite.parent, Stage)
assert isinstance(sprite.graphics.parent, Sprite)
assert isinstance(rectangle.parent, Graphics)
```

Notes: the `Sprite` instance will be added to the stage in the constructor automatically. Similarly, the `Graphics` instance will be added to the `Sprite` instance.

The `remove_from_parent` interface will remove self-instance from the parent (and will not be displayed on the stage).

## Basic usage of the remove_from_parent interface

The `remove_from_parent` method interface (no argument options) will remove the self-instance from the parent. A Removed instance will not be displayed until it will add to any parent again.

```py
# runnable
from apysc import Rectangle
from apysc import Sprite
from apysc import Stage
from apysc import save_overall_html

stage: Stage = Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
rectangle: Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Remove the rectangle from the parent and nothing will display
# on the stage.
rectangle.remove_from_parent()

save_overall_html(
    dest_dir_path='display_object_remove_from_parent_basic_usage/')
```

<iframe src="static/display_object_remove_from_parent_basic_usage/index.html" width="150" height="150"></iframe>

## See also

- [Sprite class add child and remove child interfaces](sprite_add_child_and_remove_child.md)
