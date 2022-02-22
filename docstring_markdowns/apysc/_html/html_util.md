# `apysc._html.html_util` docstrings

## Module summary

HTML related implementations. Mainly following interfaces are defined: <br>・remove_first_selector_symbol_char : Remove a first selector symbol (`.` or `#`) from a string. <br>・append_html_to_str : Add an HTML string to another string with the line break and specified number's indentation. <br>・append_indent_to_each_script_line : Append indentation spaces to each script lines of specified html. <br>・ScriptLineUtil : The class for HTML's script line utility. <br>・is_script_start_tag_line : Get a boolean whether the specified line contains script start tag (`<script ...>`). <br>・is_script_end_tag_line : Get a boolean whether the specified line contains script end tag (`</script>`). <br>・wrap_expression_by_script_tag : Wrap an expression string by script start and end tag.

## `_append_remove_first_selector_symbol_char_expression` function docstring

Append remove_first_selector_symbol_char function's expression.<hr>

**[Parameters]**

- `str_val`: String
  - A first character removed string instance.

## `append_html_to_str` function docstring

Add an HTML string to another string with the line break and specified number's indentation.<hr>

**[Parameters]**

- `to_append_html`: str
  - HTML string to append.
- `dest_html`: str
  - `to_append_html` will be appended to this string.
- `indent_num`: int
  - Indentation's number. The spaces that multiplied this number by 2 will be added.

<hr>

**[Returns]**

- `result`: str
  - HTML appended string.

## `append_indent_to_each_script_line` function docstring

Append indentation spaces to each script lines of specified html. e.g., if the html is following string, then only `console.log` line will be added indentation. <html> <script type="text/javascript"> console.log('Hello!'); </script> </html><hr>

**[Parameters]**

- `html`: str
  - Target html string.
- `indent_num`: int
  - Indentation number. e.g., if specified 1, then will be added two spaces.

<hr>

**[Returns]**

- `result_html`: str
  - Indentation added html string.

## `is_script_end_tag_line` function docstring

Get a boolean whether the specified line contains script end tag (`</script>`).<hr>

**[Parameters]**

- `line`: str
  - Target line string.

<hr>

**[Returns]**

- `result`: bool
  - If a specified line contains the script end tag, this interface returns True.

<hr>

**[Notes]**

External js script tag will not be target. e.g., `<script type="text/javascript" src="any_script.js"></script>`

## `is_script_start_tag_line` function docstring

Get a boolean whether the specified line contains script start tag (`<script ...>`).<hr>

**[Parameters]**

- `line`: str
  - Target line string.

<hr>

**[Returns]**

- `result`: bool
  - If a specified line contains the script start tag, this interface returns True.

<hr>

**[Notes]**

External js script tag will not be target. e.g., `<script type="text/javascript" src="any_script.js"></script>`

## `remove_first_selector_symbol_char` function docstring

Remove a first selector symbol (`.` or `#`) from a string.<hr>

**[Parameters]**

- `str_val`: str or String
  - Target string value. e.g., '#container'

<hr>

**[Returns]**

- `str_val`: str or String
  - The string removed a first selector symbol character.

<hr>

**[Raises]**

- TypeError: If a specified value is other than str or String type value.

## `wrap_expression_by_script_tag` function docstring

Wrap an expression string by script start and end tag.<hr>

**[Parameters]**

- `expression`: str
  - An expression to wrap.

<hr>

**[Returns]**

- `expression`: str
  - Wrapped expression string.

## `ScriptLineUtil` class docstring

### `__init__` method docstring

The class for HTML's script line utility.<hr>

**[Parameters]**

- `html`: str
  - Target HTML string.

### `_set_script_line_ranges` method docstring

Set each script's start and end line numbers.

### `is_script_line` method docstring

Get a boolean value whether a specified line number is a script line or not.<hr>

**[Parameters]**

- `line_number`: int
  - Target line number (start at 1, not 0).

<hr>

**[Returns]**

- `result`: bool
  - If the target line is a script line, this interface returns True.