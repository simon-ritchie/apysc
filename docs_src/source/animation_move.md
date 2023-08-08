# animation_move interface

This page explains the `animation_move` method interface.

## What interface is this?

The `animation_move` method interface creates an `AnimationMove` instance. You can animate the x and y coordinates with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.

## Basic usage

The following example sets the coordinates animation (from x=50, y=50 to x=100, y=100) with the `animation_move` method.

```py
# runnable
import apysc as ap


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
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=50, y=50, duration=1000
    )
    animation_move.animation_complete(on_animation_complete_2)
    animation_move.start()


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
    animation_move: ap.AnimationMove = e.this.target.animation_move(
        x=100, y=100, duration=1000
    )
    animation_move.animation_complete(on_animation_complete_1)
    animation_move.start()


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
animation_move.animation_complete(on_animation_complete_1)
animation_move.start()

ap.save_overall_html(dest_dir_path="./animation_move_basic_usage/")
```

<iframe src="static/animation_move_basic_usage/index.html" width="200" height="200"></iframe>


## animation_move API

<!-- Docstring: apysc._animation.animation_move_mixin.AnimationMoveMixIn.animation_move -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_move(self, *, x: Union[float, apysc._type.number.Number], y: Union[float, apysc._type.number.Number], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_move.AnimationMove`<hr>

**[Interface summary]**

Set the x and y coordinates animation settings.<hr>

**[Parameters]**

- `x`: float or Number
  - Destination of the x-coordinate.
- `y`: float or Number
  - Destination of the y-coordinate.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_move`: AnimationMove
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
>>> sprite.graphics.line_style(color=ap.Color("#fff"), thickness=1)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_move(
...     x=100,
...     y=150,
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