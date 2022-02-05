# animation_scale_x_from_center and animation_scale_y_from_center interfaces

This page explains the `animation_scale_x_from_center` and `animation_scale_y_from_center` method interfaces.

## What interfaces are these?

The `animation_scale_x_from_center` method interface creates an `ap.AnimationScaleXFromCenter` instance. You can animate x-direction's scale with it.

Similarly, the `animation_scale_y_from_center` method interface creates an `ap.AnimationScaleYFromCenter` instance. You can animate y-direction's scale with it.

These interfaces exist on a `GraphicsBase` subclass (that has the `scale_x_from_center` and `scale_y_from_center` interfaces), such as the `Rectangle` or `Circle`.

## Basic usage

The following example sets the scale-x (left-side rectangle) and scale-y (right-side rectangle) animation (from 1.0 to 2.0) with the `animation_scale_x_from_center` and `animation_scale_y_from_center` methods:

```py
# runnable
from enum import Enum

from typing_extensions import TypedDict

import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


class Direction(Enum):
    X = 1
    Y = 2


class Options(TypedDict):
    direction: Direction


def on_animation_complete_1(
        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:
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
    SCALE: float = 1.0
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_center(
            scale_x_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_center(
            scale_y_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_2,
            options=options,
        ).start()


def on_animation_complete_2(
        e: ap.AnimationEvent[ap.Rectangle], options: Options) -> None:
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
    SCALE: float = 2.0
    if options['direction'] == Direction.X:
        rectangle.animation_scale_x_from_center(
            scale_x_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()
    elif options['direction'] == Direction.Y:
        rectangle.animation_scale_y_from_center(
            scale_y_from_center=SCALE,
            duration=DURATION,
            easing=EASING,
        ).animation_complete(
            on_animation_complete_1,
            options=options,
        ).start()


ap.Stage(
    stage_width=250, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#0af')
left_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
right_rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=150, y=50, width=50, height=50)

options: Options = {'direction': Direction.X}
left_rectangle.animation_scale_x_from_center(
    scale_x_from_center=2.0,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

options = {'direction': Direction.Y}
right_rectangle.animation_scale_y_from_center(
    scale_y_from_center=2.0,
    duration=DURATION,
    easing=EASING,
).animation_complete(
    on_animation_complete_1,
    options=options,
).start()

ap.save_overall_html(
    dest_dir_path='./animation_scale_x_and_y_from_center_basic_usage/')
```

<iframe src="static/animation_scale_x_and_y_from_center_basic_usage/index.html" width="250" height="150"></iframe>


## animation_scale_x_from_center API

<!-- Docstring: apysc._animation.animation_scale_x_from_center_interface.AnimationScaleXFromCenterInterface.animation_scale_x_from_center -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_scale_x_from_center(self, scale_x_from_center:Union[float, apysc._type.number.Number], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_scale_x_from_center.AnimationScaleXFromCenter`<hr>

**[Interface summary]** Set the scale-x from the center point animation setting.<hr>

**[Parameters]**

- `scale_x_from_center`: Number or float
  - The final scale-x of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_scale_x_from_center`: AnimationScaleXFromCenter
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
>>> _ = rectangle.animation_scale_x_from_center(
...     scale_x_from_center=0.5,
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

## animation_scale_y_from_center API

<!-- Docstring: apysc._animation.animation_scale_y_from_center_interface.AnimationScaleYFromCenterInterface.animation_scale_y_from_center -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_scale_y_from_center(self, scale_y_from_center:Union[float, apysc._type.number.Number], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_scale_y_from_center.AnimationScaleYFromCenter`<hr>

**[Interface summary]** Set the scale-y from the center point animation setting.<hr>

**[Parameters]**

- `scale_y_from_center`: Number or float
  - The final scale-y of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_scale_y_from_center`: AnimationScaleYFromCenter
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
>>> _ = rectangle.animation_scale_y_from_center(
...     scale_y_from_center=0.5,
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