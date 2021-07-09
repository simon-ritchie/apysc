# DisplayObject

This page will explain the `DisplayObject` class.

## What is the DisplayObject?

The `DisplayObject` is the apysc base class for each display class, such as  `Sprite`, `Rectanble`, `Circle`, or something else.

You can verify the inheritance of the `DisplayObject` with each instance by the `isinstance` function.

```py
# runnable
from apysc import Stage
from apysc import Sprite
from apysc import Circle
from apysc import DisplayObject

stage: Stage = Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: Sprite = Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
circle: Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)

# Verify each instance type.
assert isinstance(sprite, DisplayObject)
assert isinstance(circle, DisplayObject)
```

This class is used for the common interfaces or the creation of the new display object with the `DisplayObject` inheritance.

The `DisplayObject` class has the basic interfaces, like `x`, `y`, `visible`, each mouse event binding, or others. The following page will explain these interfaces one by one.

## See also

- [DisplayObject class x and y interfaces](display_object_x_and_y.md)
- [DisplayObject class parent interfaces](display_object_parent.md)
- [DisplayObject class visible interface](display_object_visible.md)
- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)
