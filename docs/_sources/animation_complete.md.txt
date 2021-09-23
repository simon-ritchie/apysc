# AnimationBase class animation_complete interface

This page will explain the `AnimationBase` class `animation_complete` method interface.

## What interface is this?

The `animation_complete` method will bind a handler will be called when an animation is complete.

The handler's arguments require the event instance (`ap.AnimationEvent`) at the first argument and the options dictionary at the second argument.

## Basic usage

The `animation_complete` method requires a handler at the first argument and optional options dictionary at the second argument.

The following example will call the `animation_complete` method at the x-coordinate animation end and start another animation to reset the x-coordinate:

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=100, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=150, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=1000)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(
    dest_dir_path='./animation_complete_basic_usage/')
```

<iframe src="static/animation_complete_basic_usage/index.html" width="200" height="150"></iframe>

## Notes about the other interface calling order

The `animation_complete` method can only be called before the animation start, so if you call the `animation_complete` method after the `start` method, an exception will be raised:

```py
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Animation complete!')


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000)
animation_move.start()
animation_move.animation_complete(on_animation_complete)
```

```
Exception: This interface can not be called after an animation is started.
```

The calling of the `animation_complete` method before the `start` method will work correctly:

```py
# runnable
import apysc as ap


def on_animation_complete(
        e: ap.AnimationEvent[ap.Rectangle],
        options: dict) -> None:
    """
    The handler will be called when the animation is complete.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace('Animation complete!')


stage: ap.Stage = ap.Stage(
    stage_width=200, stage_height=200, background_color='#333',
    stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite(stage=stage)
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(
    x=100, y=100, duration=1000)
animation_move.animation_complete(on_animation_complete)
animation_move.start()
```
