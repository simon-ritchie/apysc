# `apysc._string.string_util` docstrings

## Module summary

Common string utilities. Mainly following interfaces and defined. <br>・escape_str <br> ・Escape special characters (e.g., line breaks). <br>・escape_double_quotation <br> ・Escape double quotations. <br>・wrap_by_double_quotation_if_value_is_string <br> ・Wrap specified value by double quotation if a value is a string. <br>・substitute_file_by_pattern <br> ・Substitute text file by regular expression pattern. <br>・replace_double_spaces_to_single_space <br> ・Replace double spaces with a single space.

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

Replace double spaces with a single space.<hr>

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

Wrap specified value by double quotation if a value is a string.<hr>

**[Parameters]**

- `value`: *
  - Any value to wrap.

<hr>

**[Returns]**

- `value`: *
  - Wrapped value. If a not-string value is specified, return that value immediately.