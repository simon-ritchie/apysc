# `apysc._display.graphics_clear_mixin` docstrings

## Module summary

Class implementation for the graphics clear method-related mix-in.

## `GraphicsClearMixIn` class docstring

### `clear` method docstring

Clear all graphics and reset fill and line settings.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> _ = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)
>>> _ = sprite.graphics.draw_rect(x=150, y=50, width=50, height=50)
>>> sprite.graphics.num_children
Int(2)

>>> sprite.graphics.fill_color
Color("#00aaff")

>>> sprite.graphics.clear()
>>> sprite.graphics.num_children
Int(0)

>>> sprite.graphics.fill_color
String("")
```

<hr>

**[References]**

- [Graphics clear interface](https://simon-ritchie.github.io/apysc/en/graphics_clear.html)