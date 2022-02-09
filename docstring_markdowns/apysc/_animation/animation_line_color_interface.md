# apysc._animation.animation_line_color_interface docstrings

## Module summary

Class implementation for the animation_line_color interface.

## AnimationLineColor class docstring

The animation class for a line color.

The animation class for a line color.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> sprite.graphics.line_style(
...     color='#fff', thickness=5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> animation: ap.AnimationLineColor = rectangle.animation_line_color(
...     line_color='#0af',
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... )
>>> _ = animation.start()
```

<hr>

**[References]**

- [animation_line_color interface document](https://simon-ritchie.github.io/apysc/animation_line_color.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

## AnimationLineColorInterface class docstring



### animation_line_color method docstring

Set the line color animation setting.<hr>

**[Parameters]**

- `line_color`: str or String
  - The final line color (hex color code) of the animation.
- `duration`: Int or int, default 3000
  - Milliseconds before an animation ends.
- `delay`: Int or int, default 0
  - Milliseconds before an animation starts.
- `easing`: Easing, default Easing.LINEAR
  - Easing setting.

<hr>

**[Returns]**

- `animation_line_color`: AnimationLineColor
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
>>> sprite.graphics.line_style(
...     color='#fff', thickness=5)
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_line_color(
...     line_color='#0af',
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [animation_line_color interface document](https://simon-ritchie.github.io/apysc/animation_line_color.html)
- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/animation_duration.html)
- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/animation_delay.html)
- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/animation_return_value.html)
- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/sequential_animation.html)
- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/animation_parallel.html)
- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)