# `apysc._html.debug_mode` docstrings

## Module summary

Debugging mode setting interface implementations for the HTML and JavaScript.

## `_get_callable_count` function docstring

Get a specified callable count number.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value will be set the `__name__` value.
- `class_`: Type or str or None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this argument will be ignored.

<hr>

**[Returns]**

- `callable_count`: int
  - Target count number.

## `_get_callable_path_name` function docstring

Get a specified callable count data path name.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value will be set the `__name__` value.
- `class_`: Type or str or None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this argument will be ignored.

<hr>

**[Returns]**

- `path_name`: str
  - Target path name.

## `_get_callable_str` function docstring

Get a callable string (label).<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.

<hr>

**[Returns]**

- `callable_str`: str
  - A callable string (label).

## `_increment_callable_count` function docstring

Increment a specified callable count number.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value will be set the `__name__` value.
- `class_`: Type or str or None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this argument will be ignored.

## `add_debug_info_setting` function docstring

Set a debug information setting to a target callable object (decorator function).<hr>

**[Parameters]**

- `module_name`: str
  - A target module name.
- `class_name`: str or None, default None
  - Target class name. If a target callable is function, this interface requires None of this argument.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

<hr>

**[Notes]**

Currently this interface raise a mypy error under the some mypy setting. Please set `type: ignore` comment if encountered its mypy error.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> @ap.add_debug_info_setting(  # type: ignore
...     module_name=__name__)
... def sample_method(a: int) -> None:
...     ...
```

## `is_debug_mode` function docstring

Get a boolean value whether the current debug mode is enabled or not.<hr>

**[Returns]**

- `result`: bool
  - If the current debug mode is enabled, True will be returned.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> ap.is_debug_mode()
True

>>> int_val: ap.Int = ap.Int(10)
>>> ap.unset_debug_mode()
>>> ap.is_debug_mode()
False
```

## `set_debug_mode` function docstring

Set the debug mode for the HTML and JavaScript debugging. This interface applies the following setting if calling this function: <br> ・Disabling HTML minify setting. <br> ・Changing to append per each interface JavaScript divider string.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
```

<hr>

**[References]**

- [set_debug_mode interface document](https://simon-ritchie.github.io/apysc/set_debug_mode.html)

## `unset_debug_mode` function docstring

Unset the debug mode for the HTML and JavaScript debugging.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
>>> ap.unset_debug_mode()
```

<hr>

**[References]**

- [unset_debug_mode interface document](https://simon-ritchie.github.io/apysc/unset_debug_mode.html)

## `DebugInfo` class docstring

Save a debug information (append callable interface name comment and arguments information) to the JavaScript expression file. This class is used at the `with` statement.<hr>

**[Notes]**

If the debug mode setting is not enabled, saving will be skipped.

### `__enter__` method docstring

The method will be called at the start of the with block.

### `__exit__` method docstring

The method will be called at the end of the with block.<hr>

**[Parameters]**

- `*args`: list
  - Positional arguments.

### `__init__` method docstring

Save debug information (append callable interface name comment and arguments information) to the JavaScript expression file. This class needs to use the `with` statement when instantiating.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `args`: list
  - Function positional arguments.
- `kwargs`: dict
  - Function keyword arguments.
- `module_name`: str
  - Module name. This value requires the `__name__` value.
- `class_name`: str or None, optional
  - Target class type name. If the target callable_ variable is not a method, this interface ignores this argument.

<hr>

**[Notes]**

If the debug mode setting is not enabled, this interface skips the saving.

### `_get_class_info` method docstring

Get a class information string.<hr>

**[Returns]**

- `class_info`: str
  - Target class information string.