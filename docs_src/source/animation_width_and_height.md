# animation_width and animation_height interfaces

This page explains the `animation_width` and `animation_height` interfaces.

## What interfaces are these?

The `animation_width` method interface creates an `AnimationWidth` instance. You can animate object width with it.

Similarly, the `animation_height` method interface creates an `AnimationHeight` instance. You can animate object height with it.

These interfaces exist on some `DisplayObject` instances, such as the `Rectangle` class.

## Basic usage

The following example sets the width animation (from 50 to 100) with the `animation_width` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


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
    animation_width: ap.AnimationWidth = rectangle.animation_width(
        width=50, duration=DURATION, easing=EASING)
    animation_width.animation_complete(on_animation_complete_2)
    animation_width.start()


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
    animation_width: ap.AnimationWidth = rectangle.animation_width(
        width=100, duration=DURATION, easing=EASING)
    animation_width.animation_complete(on_animation_complete_1)
    animation_width.start()


ap.Stage(
    stage_width=200, stage_height=150,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_width: ap.AnimationWidth = rectangle.animation_width(
    width=100, duration=DURATION, easing=EASING)
animation_width.animation_complete(on_animation_complete_1)
animation_width.start()

ap.save_overall_html(
    dest_dir_path='./animation_width_basic_usage/')
```

<iframe src="static/animation_width_basic_usage/index.html" width="200" height="150"></iframe>

Similarly, the following example animates the height with the `animation_height` method:

```py
# runnable
import apysc as ap

DURATION: int = 1000
EASING: ap.Easing = ap.Easing.EASE_OUT_QUINT


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
    animation_height: ap.AnimationHeight = rectangle.animation_height(
        height=50, duration=DURATION, easing=EASING)
    animation_height.animation_complete(on_animation_complete_2)
    animation_height.start()


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
    animation_height: ap.AnimationHeight = rectangle.animation_height(
        height=100, duration=DURATION, easing=EASING)
    animation_height.animation_complete(on_animation_complete_1)
    animation_height.start()


ap.Stage(
    stage_width=150, stage_height=200,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
rectangle: ap.Rectangle = sprite.graphics.draw_rect(
    x=50, y=50, width=50, height=50)
animation_height: ap.AnimationHeight = rectangle.animation_height(
    height=100, duration=DURATION, easing=EASING)
animation_height.animation_complete(on_animation_complete_1)
animation_height.start()

ap.save_overall_html(
    dest_dir_path='./animation_height_basic_usage/')
```

<iframe src="static/animation_height_basic_usage/index.html" width="150" height="200"></iframe>

## Notes for the Ellipse instance

The ellipse instance's `animation_width` and `animation_height` interfaces will return an `AnimationWidthForEllipse` and `AnimationHeightForEllipse` instance instead of an `AnimationWidth` instance, for the reason of the internal implementation, as follows:

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=150, stage_height=200,
    background_color='#333', stage_elem_id='stage')
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color='#00aaff')
ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
    x=100, y=100, width=100, height=100)
animation_width: ap.AnimationWidthForEllipse = ellipse.animation_width(
    width=200, duration=1000)
animation_width.start()
```


## animation_width API

<!-- Docstring: apysc._animation.animation_width_interface.AnimationWidthInterface.animation_width -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_width(self, width:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_width.AnimationWidth`<hr>

**[Interface summary]** Set the width animation setting.<hr>

**[Parameters]**

- `width`: Int or int
  - The final width of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_width`: AnimationWidth
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
>>> _ = rectangle.animation_width(
...     width=100,
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

## animation_height API

<!-- Docstring: apysc._animation.animation_height_interface.AnimationHeightInterface.animation_height -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_height(self, height:Union[int, apysc._type.int.Int], *, duration:Union[int, apysc._type.int.Int]=3000, delay:Union[int, apysc._type.int.Int]=0, easing:apysc._animation.easing.Easing=<Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_height.AnimationHeight`<hr>

**[Interface summary]** Set the height animation setting.<hr>

**[Parameters]**

- `height`: Int or int
  - The final height of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_height`: AnimationHeight
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
>>> _ = rectangle.animation_height(
...     height=100,
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