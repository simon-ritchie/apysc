# AnimationEvent

This page will explain the `AnimationEvent` class.

## What class is this?

The `AnimationEvent` class is used by an animation-related event handler, such as the animation complete event. This instance will be passed to the handler's first argument.

## Basic usage

The following example will set the animation complete event handler and the `AnimationEvent` instance argument is set as the `e: ap.AnimationEvent`:

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:
    """
    The handler will be called when the animation is completed.

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

The `AnimationEvent` instance's `this` property will be a subclass instance of the `AnimationBase` class, such as the `AnimationMove`, `AnimationX` or other class (this depends on the called interface, e.g., if you use the `animation_x` interface, `this` property type will be an `AnimationX` instance).

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent, options: dict) -> None:
    """
    The handler will be called when the animation is completed.

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

The `AnimationEvent` class can set a generic type annotation. If you set a generic type annotation, then the animation target property type (e.g., `DisplayObject`) will change to it.

The following example will set a `Rectangle` generic type annotation to the `AnimationEvent` and get the benefit of type checking libraries (such as the `mypy` or `Pylance`).

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
animation_x.start()
```
