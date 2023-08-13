# `apysc._event.stop_propagation_mixin` docstrings

## Module summary

Class implementation for the stop_propagation mix-in.

## `StopPropagationMixIn` class docstring

### `stop_propagation` method docstring

Stop an event propagation.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(e: ap.MouseEvent, options: dict) -> None:
...     e.stop_propagation()
...     ap.trace("Clicked!")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> _ = sprite.click(on_click)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Event class prevent_default and stop_propagation interfaces](https://simon-ritchie.github.io/apysc/en/event_prevent_default_and_stop_propagation.html)