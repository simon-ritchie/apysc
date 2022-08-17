# Notes of the variable assignment in a handler scope

This page explains the notes of the variable assignment in a handler scope.

## Current restriction of the variable assignment

Currently, the apysc library does not support basic types' (e.g., `ap.Int`, `ap.String`, and `ap.Boolean`) variable assignment (instantiation) in a handler scope.

For example, the code of `x: ap.Int = ap.Int(50)` in the handler raises an exception, as follows:

```py
import apysc as ap


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    x: ap.Int = ap.Int(50)
    ap.trace("x:", x)


ap.Timer(handler=on_timer, delay=1000, repeat_count=1).start()
```

```
...
apysc._validation.handler_validation.InvalidAssignmentInHandler: Assigning values of basic types such as the ap.Int or ap.String to variables is not supported in a handler.

Instead, consider passing a predefined value to a second argument dictionary of a handler, or updating it via the `value` property.

E.g.,
x = options["x"]
x.value = ap.Int(...)
...
```

If you want to use a variable assignment in a handler scope, please create it outside the handler scope and pass it through the `options` argument, for example:

```py
# runnable
import apysc as ap

from typing_extensions import TypedDict


class XOptions(TypedDict):
    x: ap.Int


def on_timer(e: ap.TimerEvent, options: XOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : XOptions
        Optional arguments dictionary.
    """
    ap.trace("x:", options["x"])


options: XOptions = {"x": ap.Int(50)}
ap.Timer(handler=on_timer, delay=1000, repeat_count=1, options=options).start()
```

It applies this restriction only when it instantiates and assigns a new variable.

So if an assignment does not instantiate a variable, it does not raise an exception, as follows (`x: ap.Int = options["x"]`):

```py
# runnable
import apysc as ap

from typing_extensions import TypedDict


class XOptions(TypedDict):
    x: ap.Int


def on_timer(e: ap.TimerEvent, options: XOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : XOptions
        Optional arguments dictionary.
    """
    x: ap.Int = options["x"]
    ap.trace("x:", x)


options: XOptions = {"x": ap.Int(50)}
ap.Timer(handler=on_timer, delay=1000, repeat_count=1, options=options).start()
```

Not an apysc basic types (such as the Python built-in types) also do not raise an exception (e.g., `x: int = 50`):

```py
# runnable
import apysc as ap


def on_timer(e: ap.TimerEvent, options: dict) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    x: int = 50
    ap.trace("x:", x)


ap.Timer(handler=on_timer, delay=1000, repeat_count=1).start()
```

A value's updating (e.g., `x.value = ap.Int(100)`) in a handler scope is also acceptable:

```py
# runnable
import apysc as ap

from typing_extensions import TypedDict


class XOptions(TypedDict):
    x: ap.Int


def on_timer(e: ap.TimerEvent, options: XOptions) -> None:
    """
    The timer event handler.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : XOptions
        Optional arguments dictionary.
    """
    x: ap.Int = options["x"]
    x.value = ap.Int(100)
    ap.trace("x:", x)


options: XOptions = {"x": ap.Int(50)}
ap.Timer(handler=on_timer, delay=1000, repeat_count=1, options=options).start()
```
