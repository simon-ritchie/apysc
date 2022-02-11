# `apysc._callable.callable_util` docstrings

## Module summary

Typical callable utility implementations.

## `get_arg_name_at` function docstring

Get specified index argument name from function.<hr>

**[Parameters]**

- `func`: Callable
  - Target function (or method).
- `index`: int
  - Argument index (start from 0).

<hr>

**[Returns]**

- `arg_name`: str
  - Target index's argument name.

## `get_func_default_vals` function docstring

Get specified function's arguments default values.<hr>

**[Parameters]**

- `func`: Callable
  - Target function (or method).

<hr>

**[Returns]**

- `default_vals`: dict
  - Dictionary with an argument name at key and default value at value. This interface sets the `empty` object if an argument has no default value.

## `get_method_class_name` function docstring

Get a specified method's class name.<hr>

**[Parameters]**

- `method`: Callable
  - Target method.

<hr>

**[Returns]**

- `class_name`: str
  - Target method's class name. This interface returns a blank string if a specified argument is not a method (e.g., function).

## `get_name_and_arg_value_dict_from_args` function docstring

Get a dictionary with an argument name at key and specified argument values at value.<hr>

**[Parameters]**

- `func`: Callable
  - Target function (or method).
- `args`: list
  - Specified positional arguments.
- `kwargs`: dict
  - Specified keyword arguments.

<hr>

**[Returns]**

- `name_and_arg_value_dict`: dict
  - Dictionary that has an argument name at key and specified argument values at value.