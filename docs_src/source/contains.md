# contains interface

This page explains the container class, like the `Graphics`\, `Sprite`\, `Stage`) `contains` method interface.

## What interface is this?

The `contains` interface returns the boolean (`Boolean`) value whether that `Sprite` instance has a given child or not.

## Basic usage

The following example checks whether the first rectangle is a child of the `Sprite` container. If it is `true`\, remove the rectangle from the sprite and display a log to the console (please press F12 to display that message).

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
    rectangle_1: ap.Rectangle = options['rectangle']
    condition: ap.Boolean = sprite.graphics.contains(child=rectangle_1)
    with ap.If(condition):
        sprite.remove_child(child=rectangle_1)
        ap.trace('Removed the rectangle!')


ap.Stage(
    background_color='#333',
    stage_width=250,
    stage_height=150,
    stage_elem_id='stage')

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle_1: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)
options: _RectOptions = {'rectangle': rectangle_1}
sprite.click(on_sprite_click, options=options)

ap.save_overall_html(
    dest_dir_path='sprite_contains_basic_usage/')
```

<iframe src="static/sprite_contains_basic_usage/index.html" width="250" height="150"></iframe>

## See also

- [Add child and remove child interfaces](add_child_and_remove_child.md)

## contains API

<!-- Docstring: apysc._display.child_interface.ChildInterface.contains -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `contains(self, child:apysc._display.display_object.DisplayObject) -> apysc._type.boolean.Boolean`<hr>

**[Interface summary]** Get a boolean whether this instance contains a specified child.<hr>

**[Parameters]**

- `child`: DisplayObject
  - Child instance to check.

<hr>

**[Returns]**

- `result`: Boolean
  - If this instance contains a specified child, this method returns True.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af', alpha=0.5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> sprite.graphics.contains(rectangle)
Boolean(True)

>>> rectangle.remove_from_parent()
>>> sprite.graphics.contains(rectangle)
Boolean(False)
```