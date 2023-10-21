# `apysc._display.svg_foreign_object_child` docstrings

## Module summary

The module for the `SVGForeignObjectChild` class.

## `SVGForeignObjectChild` class docstring

### `__init__` method docstring

Class implementation for the SVG's foreignObject child.<hr>

**[Parameters]**

- `html_str`: Union[str, String]
  - A HTML string.
- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `_append_constructor_expression` method docstring

Append a constructor expression of the SVG's foreignObject child.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value(s).<hr>

**[Returns]**

- `instance`: SVGForeignObjectChild
  - An initialized instance.

### `_make_snapshot` method docstring

Make values' snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### `_revert` method docstring

Revert values if a snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.