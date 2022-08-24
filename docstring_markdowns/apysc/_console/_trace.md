# `apysc._console._trace` docstrings

## Module summary

`trace` (console.log expression) interface implementations

## `_get_func_callers_info` function docstring

Get a function caller's information.<hr>

**[Returns]**

- `func_caller_info`: str
  - A function caller's information, such as the caller's name, module name, and line number.

## `_get_outer_frames_index` function docstring

Get the trace's outer frames' index setting.<hr>

**[Returns]**

- `outer_frames_index`: int
  - The trace's outer frames' index setting.

## `trace` function docstring

Display arguments information to console. This function saves a JavaScript `console.log` expression.<hr>

**[Parameters]**

- `*args`: list
  - Any arguments to display to console.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> int_val: ap.Int = ap.Int(10)
>>> ap.trace("Int value is:", int_val)
```

<hr>

**[References]**

- [Trace interface document](https://simon-ritchie.github.io/apysc/en/trace.html)

## `TemporaryOuterFramesIndexAdjustment` class docstring

### `__enter__` method docstring

Enter and set the temporary outer frames index setting.

### `__exit__` method docstring

Exit and revert the temporary outer frames index setting.

### `__init__` method docstring

The class for the trace's temporary outer frames index setting.<hr>

**[Parameters]**

- `temporary_outer_frames_index_adjustments`: int
  - A temporary outer frames index setting to set.