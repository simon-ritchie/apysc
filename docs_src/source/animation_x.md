# animation_x interface

This page explains the `animation_x` method interface.

## What interface is this?

The `animation_x` method interface creates an `AnimationX` instance. You can animate x-coordinate with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.

## Basic usage

The following example sets the x-coordinate animation (from 50 to 100) with the `animation_x` method:

```py
# runnable
import apysc as ap

EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT
DURATION: int = 1000


def on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=50, duration=DURATION, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_2)
    animation_x.start()


def on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : ap.AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    animation_x: ap.AnimationX = rectangle.animation_x(
        x=100, duration=DURATION, easing=EASING
    )
    animation_x.animation_complete(on_animation_complete_1)
    animation_x.start()


ap.Stage(
    stage_width=200,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
animation_x: ap.AnimationX = rectangle.animation_x(
    x=100, duration=DURATION, easing=EASING
)
animation_x.animation_complete(on_animation_complete_1)
animation_x.start()

ap.save_overall_html(dest_dir_path="./animation_x_basic_usage/")
```

<iframe src="static/animation_x_basic_usage/index.html" width="200" height="150"></iframe>

## Notes for the Circle and Ellipse classes

The `Circle` and `Ellipse` classes' `animation_x` interface will return an `AnimationCx` (center x) class instance, instead of an `AnimationX` instance, for internal implementation reasons.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#00aaff"))
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
animation_cx: ap.AnimationCx = circle.animation_x(
    x=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT
)
```


## animation_x API

<!-- Docstring: apysc._animation.animation_x_mixin.AnimationXMixIn.animation_x -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_x(self, *, x: Union[float, apysc._type.number.Number], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_x.AnimationX`<hr>

**[Interface summary]**

Set the x-coordinate animation setting.<hr>

**[Parameters]**

- `x`: float or Number
  - Destination of the x-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_x`: AnimationX
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_x(
...     x=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)