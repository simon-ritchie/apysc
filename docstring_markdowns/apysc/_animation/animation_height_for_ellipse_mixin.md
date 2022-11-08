# `apysc._animation.animation_height_for_ellipse_mixin` docstrings

## Module summary

Class implementation for the animation_height (for ellipse) interface.

## `AnimationHeightForEllipseMixIn` class docstring

### `animation_height` method docstring

Set the ellipse-height animation setting.<hr>

**[Parameters]**

- `height`: Int or int
  - The final ellipse-height of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_height_for_ellipse`: AnimationHeightForEllipse
  - Created animation setting instance.

<hr>

**[Notes]**

To start this animation, you need to call the `start` method of the returned instance.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color="#0af")
>>> ellipse: ap.Ellipse = sprite.graphics.draw_ellipse(
...     x=50, y=50, width=50, height=50
... )
>>> _ = ellipse.animation_height(
...     height=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_width and animation_height interfaces](https://simon-ritchie.github.io/apysc/en/animation_width_and_height.html)
- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)