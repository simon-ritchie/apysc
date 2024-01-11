# `apysc._material_design.icon.path_and_var_name_setting_base` docstrings

## Module summary

The base class for the Material Design icon. This class handles the icon's path value and variable name settings.

## `PathAndVarNameSettingBase` class docstring

### `__init__` method docstring

Create a material icon.<hr>

**[Parameters]**

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
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[References]**

- [Material icons](https://fonts.google.com/icons?selected=Material+Icons:search:)
- [APACHE LICENSE, VERSION 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)

### `_get_icon_variable_name` method docstring

Get this icon variable name's constant value.

### `_get_svg_path_value` method docstring

Get this icon's SVG path value.