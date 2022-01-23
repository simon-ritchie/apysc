# AnimationEvent

This page explains the `AnimationEvent` class.

## What class is this?

An animation-related event handler uses the `AnimationEvent` class, such as the complete animation event. Each animation interface passes this event instance to the handler.

## Basic usage

The following example sets the animation complete event handler. The animation interface passes the `AnimationEvent` instance argument as the `e: ap.AnimationEvent`:

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Animation is completed!')


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
animation_x.start()
```

## this property

The `AnimationEvent` instance's `this` property is a subclass instance of the `AnimationBase` class, such as the `AnimationMove`\, `AnimationX`\, or other class.

This type depends on the called interface, e.g., if you use the `animation_x` interface, `this` property type becomes an `AnimationX` instance.

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    assert isinstance(e.this, ap.AnimationX)


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(x=100)
animation_x.animation_complete(on_animation_complete)
animation_x.start()
```

## Generic type annotation

The `AnimationEvent` class can set a generic type annotation. If you set a generic type annotation, then the animation target property type (e.g., `DisplayObject`) changes.

The following example sets a `Rectangle` generic type annotation to the `AnimationEvent` and benefits from type checking libraries (such as the `mypy` or `Pylance`).

```py
# runnable
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

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
animation_x.start()
```