# DisplayObject

This page explains the `DisplayObject` class.

## What is the DisplayObject?

The `DisplayObject` is the apysc base class for each display class, such as  `Sprite`\, `Rectangle`\, `Circle`\, or something else.

You can verify the `DisplayObject` inheritance with each instance by the `isinstance` function.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=200,
    stage_height=200,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=100)

# Verify each instance type.
assert isinstance(sprite, ap.DisplayObject)
assert isinstance(circle, ap.DisplayObject)
```

The apysc uses this class for the basic interfaces or the creating the new display object with the `DisplayObject` inheritance.

The `DisplayObject` class has the basic interfaces, like `x`\, `y`\, `visible`\, each mouse event binding, or others. The following page explains these interfaces one by one.

## See also

- [DisplayObject class x and y interfaces](display_object_x_and_y.md)
- [DisplayObject class parent interfaces](display_object_parent.md)
- [DisplayObject class visible interface](display_object_visible.md)
- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)
