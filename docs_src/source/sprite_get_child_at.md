# Sprite class get_child_at interface

This page will explain the `Sprite` class (or the other container class, like the `Graphics`) `get_child_at` method interface.

## What interface is this?

The `get_child_at` interface will return a child (`DisplayObject`) instance at the specified index.

## Basic usage

The following code example is adding the rectangle to the sprite container. The `Sprite` class will add the `Graphics` instance at the constructor, so the first child will be the `Graphics` instance. The second child will be the `Rectangle` instance, that added by the `add_child` method.

```py
# runnable
import apysc as ap

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

first_child: ap.DisplayObject = sprite.get_child_at(index=0)
assert isinstance(first_child, ap.Graphics)

second_child: ap.DisplayObject = sprite.get_child_at(index=1)
assert isinstance(second_child, ap.Rectangle)
```
