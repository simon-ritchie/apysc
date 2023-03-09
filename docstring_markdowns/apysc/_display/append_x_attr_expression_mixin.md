# `apysc._display.append_x_attr_expression_mixin` docstrings

## Module summary

The mix-in class implementation for the `_append_x_attr_expression` method.

## `AppendXAttrExpressionMixIn` class docstring

### `_append_x_attr_expression` method docstring

Appen an x attribute expression to a specified expression string.<hr>

**[Parameters]**

- `expression`: str
  - A target expression string.
- `indent_num`: int
  - An indentation number.
- `skip_appending`: bool, optional
  - A boolean, whether to skip appending.

<hr>

**[Returns]**

- `expression`: str
  - After an appending expression string.

<hr>

**[Raises]**

- TypeError: If this is not a `XInterface` instance.