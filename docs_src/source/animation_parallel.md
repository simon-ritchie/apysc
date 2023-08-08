# animation_parallel interface

This page explains the `animation_parallel` interface.

## What interface is this?

The `animation_parallel` method interface creates an `AnimationParallel` instance. You can set multiple simultaneous animations to the same instance with it.

This interface exists on a `DisplayObject` subclass instance, such as the `Sprite` or `Rectangle` class.

## Basic usage

You can use this interface with the `animation_parallel` method. The `animations` list argument does not require any animation settings.

The following example sets the simultaneous animations of the x, fill alpha, fill color, and line thickness.

```py
# runnable
import apysc as ap

ap.Stage(
    stage_width=400,
    stage_height=150,
    background_color=ap.Color("#333"),
    stage_elem_id="stage",
)
sprite: ap.Sprite = ap.Sprite()
sprite.graphics.begin_fill(color=ap.Color("#0af"))
sprite.graphics.line_style(color=ap.Color("#fff"), thickness=3)

rectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
rectangle.animation_parallel(
    animations=[
        rectangle.animation_x(x=300),
        rectangle.animation_fill_color(fill_color=ap.Color("#f0a")),
        rectangle.animation_fill_alpha(alpha=0.3),
        rectangle.animation_line_thickness(thickness=7),
    ],
    duration=3000,
    delay=3000,
    easing=ap.Easing.EASE_OUT_QUINT,
).start()

ap.save_overall_html(dest_dir_path="animation_parallel_basic_usage/")
```

<iframe src="static/animation_parallel_basic_usage/index.html" width="400" height="150"></iframe>

## Note for each animation's duration, delay, and easing setting

Animation settings of the `duration`\, `delay`\, and `easing` in the `animations` argument can't be changed since these animation settings are referring to the `animation_parallel` arguments. If you set these parameters in the `animations` arguments, setting raise an error:

```py
...
rectangle.animation_parallel(
    animations=[
        rectangle.animation_x(x=300, duration=1000),
    ],
    duration=3000,
    delay=2000,
    easing=ap.Easing.EASE_OUT_QUINT,
)
...
```

```
ValueError: There is an animation target that is changed duration setting: 1000
The duration setting of animation in the `animations` argument can not be changed.
Target animation type: <class 'apysc._animation.animation_x.AnimationX'>
```

## animation_parallel API

<!-- Docstring: apysc._animation.animation_parallel_mixin.AnimationParallelMixIn.animation_parallel -->

<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>

**[Interface signature]** `animation_parallel(self, *, animations: List[apysc._animation.animation_base.AnimationBase], duration: Union[int, apysc._type.int.Int] = 3000, delay: Union[int, apysc._type.int.Int] = 0, easing: apysc._animation.easing.Easing = <Easing.LINEAR: 'function(x) {return x;}'>) -> apysc._animation.animation_parallel.AnimationParallel`<hr>

**[Interface summary]**

Set the parallel animation setting.<hr>

**[Parameters]**

- `animations`: list of AnimationBase
  - Target animation settings.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_parallel`: AnimationParallel
  - Created animation setting instance.

<hr>

**[Raises]**

- ValueError: <br> ・If the animations' target is not this instance. <br> ・If there are changed duration, delay, or easing animation settings in the `animations` list.

<hr>

**[Notes]**

 ・To start this animation, you need to call the `start` method of the returned instance. <br> ・The `animations` argument can't contains the `AnimationParallel` instance. <br> ・This interface ignores the duration, delay, and easing arguments in the `animations` argument (this interface uses self-arguments instead).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color=ap.Color("#f0a")),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
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
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)