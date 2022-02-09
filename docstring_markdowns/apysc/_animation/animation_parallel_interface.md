# `apysc._animation.animation_parallel_interface` docstrings

## Module summary

Class implementation for the parallel animation interface.

## `AnimationParallel` class docstring

The parallel animation setting class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> animation: ap.AnimationParallel = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color='#f0a'),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### `animation_parallel` method docstring

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
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_parallel(
...     animations=[
...         rectangle.animation_x(x=100),
...         rectangle.animation_fill_color(fill_color='#f0a'),
...         rectangle.animation_fill_alpha(alpha=0.5),
...     ],
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