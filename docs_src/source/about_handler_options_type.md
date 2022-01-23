# About the handler options' type

This page explains the event handler `options` argument's type.

## The dictionary type is acceptable

Each handler's `options` argument can accept a dictionary type value, like the following:

```py
# runnable
from typing import Dict

import apysc as ap


def on_timer(e: ap.TimerEvent, options: Dict[str, str]) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options['msg'])


timer: ap.Timer = ap.Timer(on_timer, delay=1000, options={'msg': 'Hello!'})
timer.start()
```

## About the TypedDict annotation

Sometimes using the `TypedDict` type annotation instead of the `dict` type annotation is helpful and makes it easy to read the code. The apysc check a handler options annotation and the actual options value type when you use the `TypedDict`\.

```py
# runnable
from typing_extensions import TypedDict

import apysc as ap


class _MsgOptions(TypedDict):
    msg: str


def on_timer(e: ap.TimerEvent, options: _MsgOptions) -> None:
    """
    The handler that a timer calls.

    Parameters
    ----------
    e : ap.TimerEvent
        Event instance.
    options : dict
        Optional arguments dictionary.
    """
    ap.trace(options['msg'])


options: _MsgOptions = {'msg': 'Hello!'}
timer: ap.Timer = ap.Timer(on_timer, delay=1000, options=options)
timer.start()
```

Notes: if you are using a Python 3.8 or later version, then importing the `TypedDict` from the `typing` package instead of the `typing_extensions` is available (e.g., `from typing import TypedDict`).