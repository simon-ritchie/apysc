# animation_rotation_around_point interface

This page explains the `animation_rotation_around_point` method interface.

## What interface is this?

The `animation_rotation_around_point` method interface creates an `ap.AnimationRotationAroundPoint` instance. You can animate rotation around the given point of the instance with it.

This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle` class.

## Basic usage

The `animation_rotation_around_point` method requires rotation and x and y coordinates arguments to animate.

The following example sets the rotation animation around the x=100, y=100 coordinates (the bottom-right coordinates of the rectangle) from 0 to 90 degrees.

```py
# runnable
import apysc as ap

DURATION: int = 1000


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_rotation_around_point(
        rotation_around_point=0,
        x=100,
        y=100,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_2).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:
    """
    The handler that the animation calls when its end.

    Parameters
    ----------
    e : AnimationEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    rectangle: ap.Rectangle = e.this.target
    rectangle.animation_rotation_around_point(
        rotation_around_point=90,
        x=100,
        y=100,
        duration=1000,
        easing=ap.Easing.EASE_OUT_QUINT,
    ).animation_complete(on_animation_complete_1).start()


ap.Stage(
    stage_width=150, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
rectangle.animation_rotation_around_point(
    rotation_around_point=90,
    x=100,
    y=100,
    duration=1000,
    easing=ap.Easing.EASE_OUT_QUINT,
).animation_complete(on_animation_complete_1).start()

ap.save_overall_html(
    dest_dir_path='./animation_rotation_around_point_basic_usage/')
```

<iframe src="static/animation_rotation_around_point_basic_usage/index.html" width="150" height="150"></iframe>


## animation_rotation_around_point API

<!-- Docstring: apysc._animation.animation_rotation_around_point_interface.AnimationRotationAroundPointInterface.animation_rotation_around_point -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_rotation_around_point(self, rotation_around_point:Union[int, apysc._type.int.Int], x:Union[int, apysc._type.int.Int], y:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_rotation_around_point.AnimationRotationAroundPoint`<hr>

**[Interface summary]** Set the rotation around the given point animation setting.<hr>

**[Parameters]**

- `rotation_around_point`: Int or int
  - The final rotation of the animation.
- `x`: Int or int
  - X-coordinate.
- `y`: Int or int
  - Y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_rotation_around_point`: AnimationRotationAroundPoint
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
>>> _ = rectangle.animation_rotation_around_point(
...     rotation_around_point=90,
...     x=ap.Int(100),
...     y=ap.Int(100),
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