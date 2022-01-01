# Display object x and y interfaces

This page explains the `DisplayObject` class x and y property interfaces.

## What interfaces are these?

The x and y properties change the `DisplayObject` instance 2-dimensional coordinates.

## Basic usage

Each `DisplayObject` instance has the x and y properties and can get/set the value with it.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=0, y=0, width=50, height=50)

# Update the x and y coordinates from 0 to 50.
rectangle.x = ap.Int(50)
rectangle.y = ap.Int(50)

ap.save_overall_html(
    dest_dir_path='display_object_x_and_y_basic_usage/')
```

<iframe src="static/display_object_x_and_y_basic_usage/index.html" width="150" height="150"></iframe>

## Augmented assignment

The x and y properties support the Augmented assignments, like the `+=`\, `-=`\, `/=`\, and `*=` operators.

The following example appends 10-pixel to the y-coordinate when you click the rectangle.

```py
# runnable
import apysc as ap


def on_click(e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the rectangle calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this
    rectangle.y += 10


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.click(on_click)

ap.save_overall_html(
    dest_dir_path='display_object_x_and_y_augmented_assignment/')
```

<iframe src="static/display_object_x_and_y_augmented_assignment/index.html" width="150" height="150"></iframe>
