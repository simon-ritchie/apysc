# Sprite class

This page explains the `Sprite` class.

## What is the Sprite?

The `Sprite` class is the container of each `DisplayObject` instance. It also has the `Graphics` class interfaces and can draw each vector graphic.

## Note for the automated addition

The `Sprite` instance is automated added to the stage (no need to call `add_child` or other related interfaces). However, suppose you want to add to the other instance. In that case, you need to call the `add_child` method manually.

## graphics attribute interfaces

The `Sprite` instance has the `graphics` attribute, and you can draw each vector graphic with it. For example, the following code draws the cyan color rectangle.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=150,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

ap.save_overall_html(dest_dir_path="sprite_graphics_attribute/")
```

<iframe src="static/sprite_graphics_attribute/index.html" width="150" height="150"></iframe>

For more details, please see the `Graphics` related documents, for example:

- [Graphics class](graphics.md)
- [Graphics begin_fill interface](graphics_begin_fill.md)
- [Graphics line_style interface](graphics_line_style.md)
- [Graphics draw_rect interface](graphics_draw_rect.md)
- [Graphics draw_circle interface](graphics_draw_circle.md)

## Move DisplayObject instances simultaneously

The `Sprite` class is a container, and if you move that coordinates, it changes children's coordinates simultaneously. For example, the following code changes the sprite y-coordinate when clicking the rectangle.

```py
# runnable
import apysc as ap


def on_sprite_click(e: ap.MouseEvent[ap.Sprite], options: dict) -> None:
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
    sprite.y += 50


ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=250,
    stage_height=250,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
sprite.click(on_sprite_click)

ap.save_overall_html(dest_dir_path="sprite_move_instances_simultaneously/")
```

<iframe src="static/sprite_move_instances_simultaneously/index.html" width="250" height="250"></iframe>

The subsequent pages explain the other interfaces, such as the `add_child` interface.

## See also

- [add_child and remove_child interfaces](add_child_and_remove_child.md)
- [contains interface](contains.md)
- [num_children interface](num_children.md)
- [get_child_at interface](get_child_at.md)

## Sprite class constructor API

<!-- Docstring: apysc._display.sprite.Sprite.__init__ -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `__init__(self, *, variable_name: str = '', variable_name_suffix: str = '') -> None`<hr>

**[Interface summary]**

Create a basic display object that can be a parent.<hr>

**[Parameters]**

- `variable_name`: str, default '
  - Variable name of this instance. A js expression uses this setting. It is unnecessary to specify any string except when instantiating the `Sprite` subclass.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> # Create the sprite child rectangle
>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
>>> rect: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite_1.graphics.contains(rect)
Boolean(True)

>>> # Move the created rectangle to the other sprite
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rect)
>>> sprite_1.graphics.contains(rect)
Boolean(False)

>>> sprite_2.contains(rect)
Boolean(True)

>>> # Move the sprite container
>>> sprite_2.x = ap.Number(50)
>>> sprite_2.x
Number(50.0)
```