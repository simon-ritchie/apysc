# `apysc._time.fps` docstrings

## Module summary

Definition of the FPS enum.

## `FPS` class docstring

Definition of the FPS enum.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> def on_timer(e: ap.TimerEvent, options: dict) -> None:
...     pass
>>> ap.Timer(on_timer, delay=ap.FPS.FPS_60).start()
```

<hr>

**[References]**

- [FPS enum](https://simon-ritchie.github.io/apysc/en/fps.html)

## `FPSDefinition` class docstring

### `__init__` method docstring

FPS definition class.<hr>

**[Parameters]**

- `fps`: int
  - FPS values, such as 30 and 60.
- `millisecond_interval`: int or float
  - FPS value in millisecond intervals, such as 33.333...