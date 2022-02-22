# `apysc._lint_and_doc.docstring_to_markdown_converter` docstrings

## Module summary

The script to convert and sync each docstring to markdown files.

## `_append_each_section_to_markdown` function docstring

Append each docstring section to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `docstring`: str
  - Target docstring.

<hr>

**[Returns]**

- `markdown`: str
  - A result markdown string.

## `_append_module_docstring_to_markdown` function docstring

Append a module description docstring to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `docstring`: str or None
  - Target module description docstring.

<hr>

**[Returns]**

- `markdown`: str
  - A result markdown string.

## `_append_toplevel_class_docstring_to_markdown` function docstring

Append a top-level class docstring to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `toplevel_class`: Type
  - Target top-level class.
- `module_str`: str
  - Target Python module's string.

<hr>

**[Returns]**

- `markdown`: str
  - A result markdown string.

## `_append_toplevel_function_docstring_to_markdown` function docstring

Append a top-level function docstring to a specified markdown string.<hr>

**[Parameters]**

- `markdown`: str
  - Target markdown string.
- `toplevel_function`: Callable
  - Target top-level functions.

<hr>

**[Returns]**

- `markdown`: str
  - A result markdown string.

## `_convert_module_docstring_to_markdown` function docstring

Convert a specified module's docstring to a markdown string.<hr>

**[Parameters]**

- `module_path`: str
  - Target Python module path.

<hr>

**[Returns]**

- `markdown`: str
  - Converted markdown string.

## `_get_excluding_target_builtin_methods` function docstring

Get an excluding target built-in methods' docstring values dict.<hr>

**[Returns]**

- `excluding_target_builtin_methods_dict`: dict
  - A dictionary which has builtin method name's keys and docstring values.

## `_get_methods_from_class` function docstring

Get methods from a specified class.<hr>

**[Parameters]**

- `class_`: Type
  - Target class.

<hr>

**[Returns]**

- `methods`: list of Callable
  - Extracted methods.

## `_get_module_toplevel_functions` function docstring

Get top-level functions from a specified module.<hr>

**[Parameters]**

- `module`: ModuleType
  - Target module.

<hr>

**[Returns]**

- `toplevel_functions`: list of Callable
  - Top-level functions.

## `_get_toplevel_classes` function docstring

Get top-level classes from a specified module.<hr>

**[Parameters]**

- `module`: ModuleType
  - Target module.

<hr>

**[Returns]**

- `toplevel_classes`: list of Type
  - Top-level classes.

## `_save_markdown` function docstring

Save a specified module's markdown file.<hr>

**[Parameters]**

- `module_path`: str
  - Target Python module path.

<hr>

**[Returns]**

- `markdown_file_path`: str
  - Saved markdown file path.

## `convert_recursively` function docstring

Convert each docstring in the specified directory to markdown files recursively.<hr>

**[Parameters]**

- `dir_path`: str
  - Target directory path.

<hr>

**[Returns]**

- `saved_markdown_file_paths`: list of str
  - list of saved markdown file paths.