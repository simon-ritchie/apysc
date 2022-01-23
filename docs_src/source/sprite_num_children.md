# Sprite class num_children interface

This page explains the `Sprite` class (or the other container class, like the `Graphics`) `num_children` property interface.

## What interface is this?

The `num_children` property interface returns the integer (`Int`) value of the number of children.

## Notes

The `Sprite` instance's initial children number is 1, not 0 since a sprite instance has a `graphics` child.

## Basic usage

The `num_children` property returns the number of children (`Int` value). You can use it for the calculation, for instance, coordinates calculation.

The following example appends a new rectangle when you click the sprite (rectangle) instance. The `num_children` property determines a new rectangle x-coordinate. This code also displays the current `num_children` property value to the browser console when clicking a rectangle (please press the F12 key).

```py
# runnable
import apysc as ap


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    sprite: ap.Sprite = e.this
    rectangle_x: ap.Int = (sprite.num_children - 1) * 100 + 50
    new_rect: ap.Rectangle = sprite.graphics.draw_rect(
        x=rectangle_x,
        y=50, width=50, height=50)
    sprite.add_child(new_rect)
    ap.trace(
        'Current sprite children number:', sprite.num_children,
        'rectangle x:', rectangle_x)


ap.Stage(
    background_color='#333',
    stage_width=450,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
sprite.add_child(rectangle_1)
sprite.click(on_sprite_click)

ap.save_overall_html(
    dest_dir_path='sprite_num_children_basic_usage/')
```

<iframe src="static/sprite_num_children_basic_usage/index.html" width="450" height="150"></iframe>