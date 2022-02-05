# animation_y interface

This page explains the `animation_y` method interface.

## What interface is this?

The `animation_y` method interface creates an `AnimationY` instance. You can animate y-coordinate with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle`.

## Basic usage

The following example sets the y-coordinate animation (from 50 to 100) with the `animation_y` method.

```py
# runnable
import apysc as ap

EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT
DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    animation_y: ap.AnimationY = rectangle.animation_y(
        y=50, duration=DURATION, easing=EASING)
    animation_y.animation_complete(on_animation_complete_2)
    animation_y.start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
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
    animation_y: ap.AnimationY = rectangle.animation_y(
        y=100, duration=DURATION, easing=EASING)
    animation_y.animation_complete(on_animation_complete_1)
    animation_y.start()


ap.Stage(
    stage_width=150, stage_height=200,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_y: ap.AnimationY = rectangle.animation_y(
    y=100, duration=DURATION, easing=EASING)
animation_y.animation_complete(on_animation_complete_1)
animation_y.start()

ap.save_overall_html(
    dest_dir_path='./animation_y_basic_usage/')
```

<iframe src="static/animation_y_basic_usage/index.html" width="150" height="200"></iframe>

## Notes for the Circle and Ellipse classes

The `Circle` and `Ellipse` classes' `animation_y` interface will return an `AnimationCy` (center-y) class instance, instead of a `AnimationY` instance, for internal implementation reason.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
circle: ap.Circle = sprite.graphics.draw_circle(x=100, y=100, radius=50)
animation_cy: ap.AnimationCy = circle.animation_y(
    y=100, duration=1000, easing=ap.Easing.EASE_OUT_QUINT)
```


## animation_y API

<!-- Docstring: apysc._animation.animation_y_interface.AnimationYInterface.animation_y -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_y(self, y:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_y.AnimationY`<hr>

**[Interface summary]** Set the y-coordinate animation setting.<hr>

**[Parameters]**

- `y`: Int or int
  - Destination of the y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_y`: AnimationY
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)