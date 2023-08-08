# DisplayObject class parent interfaces

This page explains the `DisplayObject` class `parent` interfaces (the `parent` property and `remove_from_parent` method).

## What interfaces are these?

The `parent` attribute is the getter property. This attribute becomes a `Stage` instance or a container instance like a `Sprite` instance.

```py
# runnable
import apysc as ap

ap.Stage(
    background_color=ap.Color("#333"),
    stage_width=150,
    stage_height=200,
    stage_elem_id="stage",
)

sprite: ap.Sprite = ap.Sprite()
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

assert isinstance(sprite.parent, ap.Stage)
assert isinstance(sprite.graphics.parent, ap.Sprite)
assert isinstance(rectangle.parent, ap.Graphics)
```

The `remove_from_parent` interface removes self-instance from the parent (and not be displayed on the stage).

## Basic usage of the remove_from_parent interface

The `remove_from_parent` method interface (no argument options) removes the self-instance from the parent. A Removed instance is not displayed until any parent adds it again.

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
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

# Remove the rectangle from the parent, and nothing displays
# on the stage.
rectangle.remove_from_parent()

ap.save_overall_html(dest_dir_path="display_object_remove_from_parent_basic_usage/")
```

<iframe src="static/display_object_remove_from_parent_basic_usage/index.html" width="150" height="150"></iframe>

## See also

- [add_child and remove_child interfaces](add_child_and_remove_child.md)


## parent API

<!-- Docstring: apysc._display.parent_mixin.ParentMixIn.parent -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]**

Get a parent instance that has an add_child and remove_child interfaces.<hr>

**[Returns]**

- `parent`: any parent instance (ChildMixIn) or None
  - Parent instance with `add_child` and `remove_child` interfaces. If this instance does not have a parent instance (not added child), this interface returns None.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite_1: ap.Sprite = ap.Sprite()
>>> sprite_1.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite_1.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> sprite_2: ap.Sprite = ap.Sprite()
>>> sprite_2.add_child(rectangle)
>>> rectangle.parent == sprite_2
True
```

## remove_from_parent API

<!-- Docstring: apysc._display.parent_mixin.ParentMixIn.remove_from_parent -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `remove_from_parent(self) -> None`<hr>

**[Interface summary]**

Remove this instance from a parent.<hr>

**[Raises]**

- ValueError: If a parent is None (there is no parent).