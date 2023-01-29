# `apysc._testing.testing_helper` docstrings

## Module summary

Common testing helper implementations.

## `_assert_has_attr` function docstring

Check object has a specified attribute.<hr>

**[Parameters]**

- `any_obj`: *
  - Any object to check.
- `attr_name`: str
  - Expected attribute name.

## `_validate_retrying_sleep_seconds` function docstring

Validate whether specified retrying sleep seconds is not greater than 10.<hr>

**[Parameters]**

- `retrying_sleep_seconds`: float
  - Sleep seconds of retrying.

<hr>

**[Raises]**

- ValueError: If a specified `retrying_sleep_seconds` is greater than 10.

## `apply_test_settings` function docstring

Apply each test setting to a test function. This function is a decorator function.<hr>

**[Parameters]**

- `retrying_max_attempts_num`: int, optional
  - A maximum number of retry attempts.
- `retrying_sleep_seconds`: Optional[float], optional
  - A Sleep seconds of retrying (Maximum seconds is 10).

<hr>

**[Returns]**

- `wrapped`: Callable
  - Wrapped callable object.

<hr>

**[Raises]**

- ValueError: If a specified `retrying_sleep_seconds` is greater than 10.

## `assert_attrs` function docstring

Check a specified object's attributes.<hr>

**[Parameters]**

- `expected_attrs`: dict
  - A dict that has attribute names in key and expected values in value.
- `any_obj`: *
  - Any object to check.

<hr>

**[Raises]**

- AssertionError: If an expected attribute value does not exist or differ.

## `assert_attrs_type` function docstring

Check a specified object's attribute types.<hr>

**[Parameters]**

- `expected_types`: dict
  - A dict that has attribute names in key and expected types in value.
- `any_obj`: *
  - Any object to check.

<hr>

**[Raises]**

- AssertionError: If any attribute type differs from an expected type.

## `assert_raises` function docstring

Check that a specified callable raises an exception.<hr>

**[Parameters]**

- `expected_error_class`: type
  - Expected error class, for instance, ValueError, Exception, etc.
- `callable_`: callable
  - Target function or method.
- `match`: str or None, default None
  - Error message's regular expression match pattern.
- `**kwargs`: dict, optional
  - Keyword arguments to pass to the function or method.

<hr>

**[Raises]**

- AssertionError: If a specified interface does not raise an error.

## `make_blank_file` function docstring

Make a blank file. If there is no directory, also create a parent directory.<hr>

**[Parameters]**

- `file_path`: str
  - File path to make.