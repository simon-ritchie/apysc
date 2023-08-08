# AnimationBase class animation_complete interface

This page explains the `AnimationBase` class `animation_complete` method interface.

## What interface is this?

The `animation_complete` method binds a handler that the animation calls when its end.

The handler's arguments require the event instance (`ap.AnimationEvent`) at the first argument and the options dictionary at the second argument.

## Basic usage

The `animation_complete` method requires a handler at the first argument and the optional options dictionary at the second argument.

The following example calls the `animation_complete` method at the x-coordinate animation end. It starts another animation to reset the x-coordinate:

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    animation_x: ap.AnimationX = rectangle.animation_x(x=50, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=200,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=1000)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(dest_dir_path="./animation_complete_basic_usage/")
```

<iframe src="static/animation_complete_basic_usage/index.html" width="200" height="150"></iframe>

## Notes about the other interface calling order

You can only call the `animation_complete` before the animation start, so if you call the `animation_complete` method after the `start` method, it raises an exception:

```py
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Animation complete!")


ap.Stage(
    stage_width=200,
    stage_height=200,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)
animation_move.start()
animation_move.animation_complete(on_animation_complete)
```

```
Exception: This interface can not be called after the animation is started.
```

The calling of the `animation_complete` method before the `start` method works correctly:

```py
# runnable
import apysc as ap


def on_animation_complete(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace("Animation complete!")


ap.Stage(
    stage_width=200,
    stage_height=200,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)

animation_move: ap.AnimationMove = rectangle.animation_move(x=100, y=100, duration=1000)
animation_move.animation_complete(on_animation_complete)
animation_move.start()
```


## animation_complete API

<!-- Docstring: apysc._animation.animation_base.AnimationBase.animation_complete -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_complete(self, handler: Callable[[ForwardRef('animation_event.AnimationEvent'), ~_Options], NoneType], *, options: Union[~_Options, NoneType] = None) -> 'AnimationBase'`<hr>

**[Interface summary]**

Add an animation complete event listener setting.<hr>

**[Parameters]**

- `handler`: _Handler
  - A callable that an instance calls when an animation is complete.
- `options`: dict or None, default None
  - Optional arguments dictionary to be passed to a handler.

<hr>

**[Returns]**

- `self`: AnimatonBase
  - This instance.

<hr>

**[Raises]**

- Exception: If calling this interface after an animation starts

<hr>

**[Notes]**

This interface can only use before an animation starts<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_animation_complete(
...     e: ap.AnimationEvent[ap.Rectangle], options: dict
... ) -> None:
...     ap.trace("Animation completed!")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = (
...     rectangle.animation_x(
...         x=100,
...     )
...     .animation_complete(on_animation_complete)
...     .start()
... )
```

<hr>

**[References]**

- [About the handler options' type](https://simon-ritchie.github.io/apysc/en/about_handler_options_type.html)