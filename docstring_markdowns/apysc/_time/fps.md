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

- [FPS enum document](https://simon-ritchie.github.io/apysc/fps.html)

## `FPSDefinition` class docstring

### `__init__` method docstring

FPS definition class.<hr>

**[Parameters]**

- `fps`: int
  - FPS value, such as 30, 60.
- `milisecond_intervals`: int or float
  - FPS value in milisecond intervals, such as 33.333...