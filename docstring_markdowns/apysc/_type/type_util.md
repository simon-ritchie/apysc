# `apysc._type.type_util` docstrings

## Module summary

Type related common implementations. Mainly following interface is defined: <br>・is_number <br> ・Get a boolean value whether a specified value is a Number value. <br>・is_float_or_number <br> ・Get a boolean value whether a specified value is a float or Number value. <br>・is_bool <br> ・Get a boolean value whether a specified value is bool or Boolean value. <br>・is_same_class_instance <br> ・Get a boolean value whether a specified class and instance's class are the same or not. <br>・is_immutable_type <br> ・Get a boolean value whether a specified value is an immutable type or not.

## `is_bool` function docstring

Get a boolean value whether a specified value is bool or Boolean value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If bool or Boolean value is specified, this interface returns True.

## `is_float_or_number` function docstring

Get a boolean value whether a specified value is a float or Number value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If float or Number value is specified, this interface returns True.

## `is_immutable_type` function docstring

Get a boolean value whether a specified value is an immutable type or not.<hr>

**[Parameters]**

- `value`: Any
  - Target value to check.

<hr>

**[Returns]**

- `result`: bool
  - This interface checks the apysc value types as immutable to match the JavaScript behavior.

<hr>

**[Notes]**

apysc's value types, such as the `Int`, are checked as immutable since these js types are immutable.

## `is_number` function docstring

Get a boolean value whether a specified value is a Number value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If a Number value is specified, this interface returns True.

## `is_same_class_instance` function docstring

Get a boolean value whether a specified class and instance's class are the same or not.<hr>

**[Parameters]**

- `class_`: Type
  - Expected class.
- `instance`: *
  - Intance to check it's class.

<hr>

**[Returns]**

- `result`: bool
  - If a specified class and instance's class are the same, this interface returns True.

<hr>

**[Notes]**

If an instance is a subclass of the `cls` argument (differ from `isinstance`), this interface returns False.