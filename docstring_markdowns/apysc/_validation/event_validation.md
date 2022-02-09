# `apysc._validation.event_validation` docstrings

## Module summary

Event validation implementation. Mainly following interfaces are defined. <br>・validate_event Validate specified instance is Event.

## `validate_event` function docstring

Validate whether specified instance is Event or not.<hr>

**[Parameters]**

- `e`: Event
  - Event instance to check.

<hr>

**[Returns]**

- `e`: Event
  - Event instance.

<hr>

**[Raises]**

- ValueError: If specified instance is not Event instance.

## `validate_event_type` function docstring

Validate whether specified value is MouseEventType one or not.<hr>

**[Parameters]**

- `mouse_event_type`: MouseEventType
  - EventTMouseEventTypeype value to check.

<hr>

**[Returns]**

- `mouse_event_type`: MouseEventType
  - MouseEventType value.