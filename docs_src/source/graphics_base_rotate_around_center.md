# GraphicsBase rotate_around_center interface

This page will explain the `GraphicsBase` class (base class of each graphics, such as the `Rectangle`) `rotate_around_center` method interface.

## What interface is this?

The `rotate_around_center` method interface will append the rotation angle to its instance (rotate around its center point).

## Basic usage

The `rotate_around_center` interface has the one `int` or `Int` value argument, `additional_rotation`.

```py
# runnable
import apysc as ap

stage: ap.Stage = ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)

# Set the cyan fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#0af', alpha=0.5)
cyan_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
cyan_rect.rotate_around_center(additional_rotation=30)

# Set the magenta fill color and draw the rectangle.
sprite.graphics.begin_fill(color='#f0a', alpha=0.5)
magenta_rect: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
# Append the rotation angle multiple times, and the results angle
# will be 60.
magenta_rect.rotate_around_center(additional_rotation=30)
magenta_rect.rotate_around_center(additional_rotation=30)

ap.save_overall_html(
    dest_dir_path='graphics_base_rotate_around_center_basic_usage/')
```

<iframe src="static/graphics_base_rotate_around_center_basic_usage/index.html" width="150" height="150"></iframe>

## Notes

This interface will support only the graphics instances. The container instances, such as the `Sprite` instance, are not supported (due to the HTML (SVG) specification).
