# apysc._type.type_util docstrings

## Module summary

Type related common implementations. Mainly following interface is defined: <br>・is_number <br> ・Get a boolean value whether specified value is Number value. <br>・is_float_or_number <br> ・Get a boolean value whether specified value is float or Nuber value. <br>・is_bool <br> ・Get a boolean value whether specified value is bool or Boolean value. <br>・is_same_class_instance <br> ・Get a boolean value whether specified class and instance's class are same or not. <br>・is_immutable_type <br> ・Get a boolean value whether specified value is immutable type or not.

## is_bool function docstring

Get a boolean value whether specified value is bool or Boolean value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If bool or Boolean value is specified, True will be returned.

## is_float_or_number function docstring

Get a boolean value whether specified value is float or Nuber value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If float or Number value is specified, True will be returned.

## is_immutable_type function docstring

Get a boolean value whether specified value is immutable type or not.<hr>

**[Parameters]**

- `value`: Any
  - Target value to check.

<hr>

**[Returns]**

- `result`: bool
  - If a specified value is immutable, then True will be set.

<hr>

**[Notes]**

apysc's value types, such as the `Int`, are checked as immutable since these js types are immutable.

## is_number function docstring

Get a boolean value whether specified value is Number value.<hr>

**[Parameters]**

- `value`: *
  - Any value to check.

<hr>

**[Returns]**

- `result`: bool
  - If Number value is specified, True will be returned.

## is_same_class_instance function docstring

Get a boolean value whether specified class and instance's class are same or not.<hr>

**[Parameters]**

- `class_`: Type
  - Expected class.
- `instance`: *
  - Intance to check it's class.

<hr>

**[Returns]**

- `result`: bool
  - If a specified class and instance's class are same, then True will be set.

<hr>

**[Notes]**

If instance is subclass of `cls` argument, differ from `isinstace`, then False will be returned.