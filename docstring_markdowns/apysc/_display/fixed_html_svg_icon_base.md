# `apysc._display.fixed_html_svg_icon_base` docstrings

## Module summary

The class implementation for the fixed HTML SVG icon's base class.

## `FixedHtmlSvgIconBase` class docstring

### `__init__` method docstring

The class implementation for the fixed HTML SVG icon's base class.<hr>

**[Parameters]**

- `x`: Union[float, Number], optional
  - X-coordinate of the icon.
- `y`: Union[float, Number], optional
  - Y-coordinate of the icon.
- `size`: Union[int, Int], optional
  - Size of the icon.
- `fill_color`: Color, optional
  - Fill-color of the icon.
- `fill_alpha`: Union[float, Number], optional
  - Fill-alpha of the icon.
- `parent`: Optional[ChildMixIn], optional
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `_get_fixed_svg_icon_html` method docstring

Get a fixed SVG icon HTML string.<hr>

**[Returns]**

- `fixed_svg_icon_html`: str
  - Fixed SVG icon HTML string.