# `apysc._event.prevent_default_interface` docstrings

## Module summary

Class implementation for the prevent_default interface.

## `PreventDefaultInterface` class docstring

### `prevent_default` method docstring

Prevent event's default behavior.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(
...         e: ap.MouseEvent[ap.Rectangle], options: dict) -> None:
...     e.prevent_default()
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.String('#f0a')
...     rectangle.unbind_mouseup_all()
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = rectangle.click(on_click)
```

<hr>

**[References]**

- [Event class prevent_default and stop_propagation interfaces document](https://simon-ritchie.github.io/apysc/event_prevent_default_and_stop_propagation.html)