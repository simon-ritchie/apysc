# apysc._expression.indent_num docstrings

## Module summary

Implementations of expression's indent number related interfaces. Mainly following interfaces are defined: <br>・get_current_indent_num: Get a current indent number. <br>・Indent: Class implementation for increment and decrement indentation number. Basically use this class at with statement. <br>・reset: Reset current indent number.

## _get_indent_num_table_name function docstring

Get a indentation number table name. This value will switch by scope condition (e.g., event handler's scope or not).<hr>

**[Returns]**

- `table_name`: str
  - Target table name.

## _save_current_indent_num function docstring

Save the current indentation number.<hr>

**[Parameters]**

- `indent_num`: int
  - Current indentation number.

## get_current_indent_num function docstring

Get a current indent number.<hr>

**[Returns]**

- `current_indent_num`: int
  - Current indent number.

## reset function docstring

Reset current indent number.

## Indent class docstring

Class implementation for increment and decrement indentation number. Basically use this class at with statement.

### __enter__ method docstring

Method to be used by with statement. This method will increment indentation number.

### __exit__ method docstring

Method to be used by with statement. This method will decrement indentation number.<hr>

**[Parameters]**

- `*args`: list
  - Any positional arguments.