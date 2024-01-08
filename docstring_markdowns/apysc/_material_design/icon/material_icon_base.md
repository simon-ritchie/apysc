# `apysc._material_design.icon.material_icon_base` docstrings

## Module summary

The class implementation for the material icon's base class.

## `MaterialIconBase` class docstring

### `__init__` method docstring

The class implementation for the material icon's base class.<hr>

**[Parameters]**

- `svg_path_value`: Union[str, String]
  - SVG path value string. This value requires the `d` attribute of the SVG `path` tag. E.g., "M15.5 14h-.79l-.28-.27C15.41 12.59 ..."
- `fill_color`: Color
  - An icon fill-color.
- `fill_alpha`: Union[float, Number], optional
  - An icon fill-alpha (opacity).
- `x`: Union[float, Number], optional
  - An icon x-coordinate.
- `y`: Union[float, Number], optional
  - An icon y-coordinate.
- `width`: Union[int, Int], optional
  - An icon width.
- `height`: Union[int, Int], optional
  - An icon height.
- `parent`: ChildMixIn or None, default None
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name`: str, optional
  - A Variable name of JavaScript.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.

### `_append_constructor_expression` method docstring

Append a constructor expression string.

### `_initialize_with_base_value` method docstring

Initialize this class with a base value.<hr>

**[Returns]**

- `icon`: MaterialIconBase
  - An initialized icon instance.

### `_make_variable_name_if_empty` method docstring

Make a variable name if it is empty.<hr>

**[Parameters]**

- `variable_name`: str
  - A variable name of JavaScript.

<hr>

**[Returns]**

- `variable_name`: str
  - A variable name of JavaScript.