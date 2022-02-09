# apysc._event.document_mouse_wheel_interface docstrings

## Module summary

Implementation of mouse wheel event interfaces.<hr>

**[Notes]**

Not supported each SVG elements' mouse wheel event currently, only supported document (overall screen) mouse wheel.

## bind_wheel_event_to_document function docstring

Bind wheel event to document (overall window).<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable that handle wheel event.
- `options`: dict or None, default None
  - Optional arguments dictionary to pass to.

<hr>

**[Returns]**

- `name`: str
  - Handler's name.

<hr>

**[References]**

- [About the handler options’ type document](https://simon-ritchie.github.io/apysc/about_handler_options_type.html)

## unbind_wheel_event_all_from_document function docstring

Unbind all wheel event from document (overall window).

## unbind_wheel_event_from_document function docstring

Unbind specified handler's wheel event from document (overall window).<hr>

**[Parameters]**

- `handler`: _Handler
  - Callable to unbind.