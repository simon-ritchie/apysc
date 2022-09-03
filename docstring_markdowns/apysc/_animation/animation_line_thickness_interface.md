# `apysc._animation.animation_line_thickness_interface` docstrings

## Module summary

Class implementation for the animation_line_thickness interface.

## `AnimationLineThicknessInterface` class docstring

### `animation_line_thickness` method docstring

Set the line thickness animation setting.<hr>

**[Parameters]**

- `thickness`: Int or int
  - The final line thickness of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_thickness`: AnimationLineThickness
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
>>> sprite.graphics.line_style(color="#fff", thickness=1)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = rectangle.animation_line_thickness(
...     thickness=6,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_thickness interface](https://simon-ritchie.github.io/apysc/en/animation_line_thickness.html)
- [Animation interfaces duration setting](https://simon-ritchie.github.io/apysc/en/animation_duration.html)
- [Animation interfaces delay setting](https://simon-ritchie.github.io/apysc/en/animation_delay.html)
- [Each animation interface return value](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)
- [Sequential animation setting](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)
- [animation_parallel interface](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)
- [Easing enum](https://simon-ritchie.github.io/apysc/en/easing_enum.html)