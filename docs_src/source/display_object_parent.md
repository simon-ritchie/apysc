# Display object parent interfaces

This page explains the `DisplayObject` class `parent` interfaces (the `parent` property and `remove_from_parent` method).

## What interfaces are these?

The `parent` attribute is the getter property. This attribute becomes a `Stage` instance or a container instance like a `Sprite` instance.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

assert isinstance(sprite.parent, ap.Stage)
assert isinstance(sprite.graphics.parent, ap.Sprite)
assert isinstance(rectangle.parent, ap.Graphics)
```

Notes: This interface automatically adds the sprite to the stage at the constructor. Similarly, this interface adds the `Graphics` instance to the `Sprite` instance.

The `remove_from_parent` interface removes self-instance from the parent (and not be displayed on the stage).

## Basic usage of the remove_from_parent interface

The `remove_from_parent` method interface (no argument options) removes the self-instance from the parent. A Removed instance is not displayed until any parent adds it again.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

# Remove the rectangle from the parent and nothing displays
# on the stage.
rectangle.remove_from_parent()

ap.save_overall_html(
    dest_dir_path='display_object_remove_from_parent_basic_usage/')
```

<iframe src="static/display_object_remove_from_parent_basic_usage/index.html" width="150" height="150"></iframe>

## See also

- [Sprite class add child and remove child interfaces](sprite_add_child_and_remove_child.md)
