# add_child and remove_child interfaces

This page explains the container class, like the `Graphics`\, `Sprite`\, `Stage`) `add_child` and `remove_child` method interfaces.

## What interfaces are these?

The `add_child` and `remove_child` add or remove a `DisplayObject` child instance from a container instance. The apysc does not display a removed `DisplayObject` instance.

## Automatic addition of the children

The apysc appends each `DisplayObject` instance to a parent at the constructor. So, for example, it appends a `Sprite` instance to a parent stage. Similarly, it appends a `graphics` instance to a parent `Sprite` instance.

If you need to adjust a parent, it is necessary to call the `add_child` or `remove_child` interfaces manually (for instance, set a `Sprite` parent to the other `Sprite`).

## Basic usage of the remove_child interface

The `remove_child` interface removes a child from a parent container instance. The apysc does not display a removed `DisplayObject` instance.

For example, the following code calls the `remove_child` interface in the click handler, so if you click the rectangle, it removes that rectangle.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _RectOptions(TypedDict):
    rectangle: ap.Rectangle


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite], options: _RectOptions) -> None:
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
    rectangle: ap.Rectangle = options['rectangle']
    sprite.remove_child(child=rectangle)


ap.Stage(
    background_color='#333',
    stage_width=150,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='sprite_basic_usage_of_remove_child/')
```

<iframe src="static/sprite_basic_usage_of_remove_child/index.html" width="150" height="150"></iframe>

## The basic usage of the add_child interface

The `add_child` interface adds a removed child again or adds a child to the other container instance.

The following code example removes the rectangle from the first `Sprite` container (be positioned to the left) when you click the rectangle. Also, that click event adds the rectangle to the second `Sprite` container (be positioned to the right).

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _SpriteAndRectOptions(TypedDict):
    rectangle: ap.Rectangle
    sprite: ap.Sprite


def on_sprite_click(
        e: ap.MouseEvent[ap.Sprite],
        options: _SpriteAndRectOptions) -> None:
    """
    The handler that the sprite calls when clicked.

    Parameters
    ----------
    e : MouseEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    first_sprite: ap.Sprite = e.this
    rectangle: ap.Rectangle = options['rectangle']
    second_sprite: ap.Sprite = options['sprite']
    first_sprite.remove_child(child=rectangle)
    second_sprite.add_child(child=rectangle)


ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

first_sprite: ap.Sprite = ap.Sprite()
first_sprite.graphics.begin_fill(color='#0af')
first_sprite.x = ap.Int(50)
first_sprite.y = ap.Int(50)
rectangle: ap.Rectangle = first_sprite.graphics.draw_rect(
    x=0, y=0, width=50, height=50)

second_sprite: ap.Sprite = ap.Sprite()
second_sprite.x = ap.Int(150)
second_sprite.y = ap.Int(50)

options: _SpriteAndRectOptions = {
    'rectangle': rectangle, 'sprite': second_sprite}
first_sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='sprite_basic_usage_of_add_child/')
```

<iframe src="static/sprite_basic_usage_of_add_child/index.html" width="250" height="150"></iframe>

## See also

- [DisplayObject class parent interfaces](display_object_parent.md)
- [Contains interface](contains.md)

## add_child API

<!-- Docstring: apysc._display.child_interface.ChildInterface.add_child -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `add_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>

**[Interface summary]** Add display object child to this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to add.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
```

## remove_child API

<!-- Docstring: apysc._display.child_interface.ChildInterface.remove_child -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `remove_child(self, child:apysc._display.display_object.DisplayObject) -> None`<hr>

**[Interface summary]** Remove display object child from this instance.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to remove.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.remove_child(rectangle)
>>> print(rectangle.parent)
None
```