# apysc._event.stop_propagation_interface docstrings

## Module summary

Class implementation for the stop_propagation interface.

## StopPropagationInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.

### stop_propagation method docstring

Stop event propagation. Refenreces ---------- <br> ・Event class prevent_default and stop_propagation interfaces document <br> ・https://simon-ritchie.github.io/apysc/event_prevent_default_and_stop_propagation.html # noqa<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_click(e: ap.MouseEvent, options: dict) -> None:
...     e.stop_propagation()
...     ap.trace('Clicked!')
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color='#0af')
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50)
>>> _ = sprite.click(on_click)
>>> _ = rectangle.click(on_click)
```

## VariableNameInterface class docstring



### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

### _get_previous_variable_name method docstring

Get a previous variable name.<hr>

**[Returns]**

- `previous_variable_name`: str
  - A previous variable name of this instance. If that value is not existing, then a blank string will be returned.