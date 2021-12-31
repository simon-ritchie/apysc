# GraphicsBase rotation_around_center interface

This page will explain the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `rotation_around_center` property interface.

## What interface is this?

The `rotation_around_center` property interface can set the rotation angle to its instance (rotation value around its center point).

## Basic usage

The `rotation_around_center` interface accepts the `int` or `Int` value.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()

# Set the cyan fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#0af', alpha=0.5)
cyan_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
cyan_rect.rotation_around_center = ap.Int(30)

# Set the magenta fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
magenta_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
# Append the rotation angle with the incremental addition (the result
# rotation will be 60 degrees).
magenta_rect.rotation_around_center += ap.Int(30)
magenta_rect.rotation_around_center += ap.Int(30)

ap.save_overall_html(
    dest_dir_path='graphics_base_rotation_around_center_basic_usage/')
```

<iframe src="static/graphics_base_rotation_around_center_basic_usage/index.html" width="150" height="150"></iframe>

## Notes

This interface supports only the graphics instances currently. The container instances, such as the `Sprite` instance, are not supported (due to the HTML (SVG) specification).
