# AnimationBase class target property interface

This page will explain the `AnimationBase` class `target` property interface.

## What property is this?

The `target` property will return the animation target instance (e.g., `Sprite`, `Rectangle`).

## Basic usage

Each subclass of the `AnimationBase` (e.g., `AnimationMove`, `AnimationX`) has the `target` getter property.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
assert isinstance(animation_x.target, ap.Rectangle)
```

## Generic type annotation setting

The `AnimationBase` class and its subclasses can set a generic type annotation and if it is set the `target` property type will be its type.

The following code will set the `[ap.Rectangle]` generic type annotation:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX[ap.Rectangle] = rectangle.animation_x(x=100)
assert isinstance(animation_x.target, ap.Rectangle)
```

It is also sometimes useful to annotate generic type to the handler's `AnimationEvent`. This generic type annotation also affects the `target` type (`e.this.target`), as follows:

```py
# runnable
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is completed.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_x(x=50).start()


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
```
