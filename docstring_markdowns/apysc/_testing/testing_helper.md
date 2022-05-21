# `apysc._testing.testing_helper` docstrings

## Module summary

Common testing helper implementations.

## `_assert_has_attr` function docstring

Check object has specified attribute.<hr>

**[Parameters]**

- `any_obj`: *
  - Any object to check.
- `attr_name`: str
  - Expected attribute name.

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