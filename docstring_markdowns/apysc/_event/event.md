# `apysc._event.event` docstrings

## Module summary

Class Implementation for an event.

## `Event` class docstring

Basic event class.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
... )
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
```

### `__init__` method docstring

Basic event class.<hr>

**[Parameters]**

- `this`: VariableNameMixIn
  - Instance that listening event (e.g., Sprite).
- `type_name`: str or None, default None
  - Type name to set. Only specify when inheriting this class.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_custom_event(e: ap.Event[ap.Rectangle], options: dict) -> None:
...     rectangle: ap.Rectangle = e.this
...     rectangle.fill_color = ap.Color("#f0a")
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.begin_fill(color=ap.Color("#0af"))
>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(
...     x=50, y=50, width=50, height=50
... )
>>> e: ap.Event = ap.Event(this=rectangle)
>>> _ = rectangle.bind_custom_event(
...     custom_event_type="my_custom_event", handler=on_custom_event, e=e
... )
>>> # Do something here and then trigger the custom event
>>> rectangle.trigger_custom_event(custom_event_type="my_custom_event")
```

### `_validate_type_name_and_self_type` method docstring

Validate type_name argument is None when a self instance is not Event subclass, and the same is true for the opposite pattern.<hr>

**[Parameters]**

- `type_name`: str or None
  - Type name to set.

<hr>

**[Raises]**

- ValueError: <br> ・If type_name is not None and self instance is Event type. <br> ・If type_name is None and self instance is not Event type.