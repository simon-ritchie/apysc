# `apysc._type._return` docstrings

## Module summary

This module is for the `return` expression class implementation.

## `Return` class docstring

Class for the return expression.<hr>

**[References]**

- [Return document](https://simon-ritchie.github.io/apysc/return.html)

### `__init__` method docstring

Class for the return expression.<hr>

**[Notes]**

This class can be instantiated only in an event handler scope.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     """
...     The handler that the timer calls.
...
```

<hr>

**[References]**

- [Return document](https://simon-ritchie.github.io/apysc/return.html)

### `_validate_current_scope_is_event_handler` method docstring

Validate whether the current scope is an event handler scope or not.