# `apysc._animation.animation_fill_alpha_interface` docstrings

## Module summary

Class implementation for the animation_fill_alpha interface.

## `AnimationFillAlphaInterface` class docstring

### `animation_fill_alpha` method docstring

Set the fill alpha (opacity) animation setting.<hr>

**[Parameters]**

- `alpha`: Number or float
  - The final alpha (opacity) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_fill_alpha`: AnimationFillAlpha
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
>>> circle: ap.Circle = sprite.graphics.draw_circle(
...     x=100, y=100, radius=50)
>>> _ = circle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_fill_alpha interface document](https://simon-ritchie.github.io/apysc/animation_fill_alpha.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)