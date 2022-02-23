# `apysc._string.indent_util` docstrings

## Module summary

Common indentation related utility implementations. Mainly following interfaces are defined: <br>・make_spaces_for_html: Make spaces that multiplied 2 to specified indentation number. <br>・append_spaces_to_expression: Append spaces to a expression string.

## `append_spaces_to_expression` function docstring

Append spaces to a js expression string.<hr>

**[Parameters]**

- `expression`: str
  - JavaScript expression string to add spaces.
- `indent_num`: int
  - Indentation number. If 1 is specified, spaces become 2.

<hr>

**[Returns]**

- `expression`: str
  - Expression string after adding spaces.

## `make_spaces_for_html` function docstring

Make spaces that multiply 2 to a specified indentation number.<hr>

**[Parameters]**

- `indent_num`: int
  - Indentation number.

<hr>

**[Returns]**

- `spaces`: str
  - Result spaces string.