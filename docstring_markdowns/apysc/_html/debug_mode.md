# `apysc._html.debug_mode` docstrings

## Module summary

This module is for the HTML and JavaScript debugging-mode setting interface implementations.

## `_get_callable_count` function docstring

Get a specified callable count number.<hr>

**[Parameters]**

- `callable_`: Callable or str
  - Target function or method or property or dunder method name.
- `module_name`: str
  - Module name. This value needs to set the `__name__` value.
- `class_`: Type or str or None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this interface ignores this argument.

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
  - Module name. This value needs to set the `__name__` value.
- `class_`: Type or str or None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this interface ignores this argument.

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
  - Module name. This value needs to set the `__name__` value.
- `class_`: Type or str or None, optional
  - Target class type or type name. If the target callable_ variable is not a method, this interface ignores this argument.

## `add_debug_info_setting` function docstring

Set a debug information setting to a target callable object (decorator function).<hr>

**[Parameters]**

- `module_name`: str
  - A target module name.

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

<hr>

**[Notes]**

Currently, this interface raises a mypy error under some mypy settings. Please set `type: ignore[misc]` comment or `--disable-error-code misc` mypy's command argument if encountered its mypy error.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> @ap.add_debug_info_setting(module_name=__name__)  # type: ignore[misc]
... def sample_method(a: int) -> None: ...
```

## `is_debug_mode` function docstring

Get a boolean value whether the current debug mode is enabled or not.<hr>

**[Returns]**

- `result`: bool
  - If the current debug mode is enabled, this interface returns True.

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

Set the debug mode for the HTML and JavaScript debugging. If calling this function, this interface applies the following setting: <br> ・Disabling HTML minify setting. <br> ・Changing to append per each interface JavaScript divider string.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> ap.set_debug_mode()
>>> int_val: ap.Int = ap.Int(10)
```

<hr>

**[References]**

- [set_debug_mode interface](https://simon-ritchie.github.io/apysc/en/set_debug_mode.html)

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

- [unset_debug_mode interface](https://simon-ritchie.github.io/apysc/en/unset_debug_mode.html)

## `DebugInfo` class docstring

Save debugging information (append callable interface name comment and arguments information) to the JavaScript expression file. The apysc uses this class at the `with` statement.<hr>

**[Notes]**

If the debug mode setting is not enabled, the apysc skips the saving.

### `__enter__` method docstring

This class uses this method at the start of the with-block.

### `__exit__` method docstring

This class uses this method at the end of the with-block.<hr>

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