# get_child_at interface

This page explains the container class, like the `Graphics`\, `Sprite`\, `Stage`) `get_child_at` method interface.

## What interface is this?

The `get_child_at` interface returns a child (`DisplayObject`) instance at the specified index.

## Basic usage

The following code example is adding the rectangle to the sprite container. The `Sprite` class adds the `Graphics` instance at the constructor so that the first child becomes the `Graphics` instance. The second child becomes the `Rectangle` instance, which the sprite added with the `add_child` method.

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

## get_child_at API

<!-- Docstring: apysc._display.child_interface.ChildInterface.get_child_at -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `get_child_at(self, index:Union[int, apysc._type.int.Int]) -> apysc._display.display_object.DisplayObject`<hr>

**[Interface summary]** Get child at a specified index.<hr>

**[Parameters]**

- `index`: int or Int
  - Child's index (start from 0).

<hr>

**[Returns]**

- `child`: DisplayObject
  - Target index child instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> rectangle_2: ap.Rectangle = sprite.graphics.draw_rect(
...     x=150, y=50, width=50, height=50)
>>> child_at_index_1: ap.DisplayObject = (
...     sprite.graphics.get_child_at(1))
>>> child_at_index_1 == rectangle_2
True
```