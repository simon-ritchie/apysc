# apysc._animation.easing docstrings

## Module summary

Enum class implementation for the easing setting.

## Easing class docstring

Enum class for the easing setting.

Enum class for the easing setting.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.animation_y(
...     y=100,
...     duration=1500,
...     easing=ap.Easing.EASE_OUT_QUINT,
... ).start()
```

<hr>

**[References]**

- [Easing enum document](https://simon-ritchie.github.io/apysc/easing_enum.html)

### EnumMeta method docstring

Metaclass for Enum

## Enum class docstring

Generic enumeration. Derive from this class to define new enumerations.

Generic enumeration. Derive from this class to define new enumerations.

### EnumMeta method docstring

Metaclass for Enum