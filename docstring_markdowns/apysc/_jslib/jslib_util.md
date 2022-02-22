# `apysc._jslib.jslib_util` docstrings

## Module summary

Common JavaScript library utility implementations. Mainly the following interfaces are defined: <br>・get_jslib_file_names Get the JavaScript libraries file's names. <br>・get_jslib_abs_dir_path Get the Javascript library's absolute directory path. This interface returns this module's directory. <br>・export_jslib_to_specified_dir Export a JavaScript library to a specified directory. <br>・read_jslib_str Read a JavaScript library file str.

## `export_jslib_to_specified_dir` function docstring

Export a JavaScript library to a specified directory.<hr>

**[Parameters]**

- `dest_dir_path`: str
  - Directory path to export JavaScript library file.
- `jslib_name`: str
  - JavaScript file name to export.

<hr>

**[Returns]**

- `dest_file_path`: str
  - Exported Javascript library's file path.

<hr>

**[Raises]**

- FileNotFoundError: If there is no specified JavaScript file.

## `get_jslib_abs_dir_path` function docstring

Get the Javascript library's absolute directory path. This interface returns this module's directory.<hr>

**[Returns]**

- `jslib_abs_dir_path`: str
  - Javascript library's absolute directory path. This module's directory will be set.

## `get_jslib_file_names` function docstring

Get the JavaScript libraries file's names.<hr>

**[Returns]**

- `jslib_file_names`: list of str
  - JavaScript libraries file names existing in this module's directory. e.g., ['jquery.min.js', 'svg.min.js']

## `read_jslib_str` function docstring

Read a JavaScript library file str.<hr>

**[Parameters]**

- `jslib_name`: str
  - JavaScript file name to read.

<hr>

**[Returns]**

- `jslib_str`: str
  - Read JavaScript library string.