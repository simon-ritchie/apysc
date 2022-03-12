# AnimationBase class target property interface

This page explains the `AnimationBase` class `target` property interface.

## What property is this?

The `target` property returns the animation target instance (e.g., `Sprite`\, `Rectangle`).

## Basic usage

Each subclass of the `AnimationBase` (e.g., `AnimationMove`\, `AnimationX`) has the `target` getter property.

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

The `AnimationBase` class and its subclasses can set a generic type annotation. For example, the `target` property type becomes its type if you set it.

The following code sets the `[ap.Rectangle]` generic type annotation:

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

It is also sometimes useful to annotate generic type to the handler's `AnimationEvent`\. This generic type annotation also affects the `target` type (`e.this.target`), as follows:

```py
# runnable
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler the animation calls when its end.

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

## target property API

<!-- Docstring: apysc._animation.animation_base.AnimationBase.target -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface summary]** Get an animation target instance.<hr>

**[Returns]**

- `target`: VariableNameInterface
  - An animation target instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...         e: ap.AnimationEvent[ap.Rectangle],
...         options: dict) -> None:
...     rectangle: ap.Rectangle = e.this.target
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_x(
...     x=100,
... ).animation_complete(on_animation_complete).start()
```