# `apysc._string.string_util` docstrings

## Module summary

Common string utilities. Mainly following interfaces and defined. <br>・escape_str Escape special characters (e.g. line breaks of ` `). <br>・escape_double_quotation Escape double quotations. <br>・wrap_by_double_quotation_if_value_is_string Wrap specified by double quotation if value is a string. <br>・substitute_file_by_pattern Substitute text file by regular expression pattern. <br>・replace_double_spaces_to_single_space Replace double spaces to a single space.

## `escape_double_quotation` function docstring

Escape double quotations.<hr>

**[Parameters]**

- `string`: str
  - String to escape.

<hr>

**[Returns]**

- `string`: str
  - Escaped string.

## `escape_str` function docstring

Escape special characters (e.g. line breaks of ` `).<hr>

**[Parameters]**

- `string`: str
  - String to escape.

<hr>

**[Returns]**

- `string`: str
  - Escaped string.

## `replace_double_spaces_to_single_space` function docstring

Replace double spaces to a single space.<hr>

**[Parameters]**

- `string`: str
  - Target string to replace.

<hr>

**[Returns]**

- `string`: str
  - Replaced string.

## `substitute_file_by_pattern` function docstring

Substitute text file by regular expression pattern.<hr>

**[Parameters]**

- `file_path`: str
  - Target file path.
- `pattern`: str
  - Regular expression pattern.
- `repl`: str
  - String that replace matched pattern one.
- `flags`: Any
  - Regular expression flags.

## `wrap_by_double_quotation_if_value_is_string` function docstring

Wrap specified by double quotation if value is a string.<hr>

**[Parameters]**

- `value`: *
  - Any value to wrap.

<hr>

**[Returns]**

- `value`: *
  - Wrapped value. If not string value is specified, return that value imediatelly.