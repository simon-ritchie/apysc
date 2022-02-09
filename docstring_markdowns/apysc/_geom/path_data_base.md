# apysc._geom.path_data_base docstrings

## Module summary

Base class implementation for the path data.

## PathDataBase class docstring

Base class for the path data.

### __init__ method docstring

Base class for the path data.<hr>

**[Parameters]**

- `path_label`: PathLabel
  - Target (svg's) path label.
- `relative`: bool or Boolean
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.