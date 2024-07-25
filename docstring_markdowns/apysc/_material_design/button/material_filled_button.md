# `apysc._material_design.button.material_filled_button` docstrings

## Module summary

The class implementation for the material design filled button.

## `MaterialFilledButton` class docstring

The class for the material design filled button.<hr>

**[References]**

- [Material design filled button document](https://m3.material.io/components/buttons/specs#0b1b7bd2-3de8-431a-afa1-d692e2e18b0d)

### `__init__` method docstring

The class for the material design filled button.<hr>

**[Parameters]**

- `label`: Union[str, String]
  - The label text to display on this button.
- `prefix_icon`: Optional[FixedHtmlSvgIconBase], optional
  - An icon to display on the left side of the label.
- `suffix_icon`: Optional[FixedHtmlSvgIconBase], optional
  - An icon to display on the right side of the label.
- `x`: Union[float, Number], optional
  - X-coordinate of this button.
- `y`: Union[float, Number], optional
  - Y-coordinate of this button.
- `text_color`: Optional[Color], optional
  - The color of the label text. The label color becomes according to the following priorities: 1. If this argument is not omitted (i.e., it is not `None`) 2. If a color scheme is set in the `MaterialSettings` (this button refers to the `primary` color) 3. A fixed color value.
- `font_family`: Optional[Union[Array[String], List[str]]], optional
  - A font-family setting.
- `font_size`: Union[int, Int], optional
  - A font-size setting.
- `background_color`: Optional[Color], optional
  - The background color of this button. The background color becomes according to the following priorities: 1. If this argument is not omitted (i.e., it is not `None`) 2. If a color scheme is set in the `MaterialSettings` (this button refers to the `on_primary` color) 3. A fixed color value.
- `parent`: Optional[ChildMixIn], optional
  - A parent instance to add this instance. If the specified value is None, this interface uses a stage instance.
- `variable_name_suffix`: str, optional
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[References]**

- [Material design filled button document](https://m3.material.io/components/buttons/specs#0b1b7bd2-3de8-431a-afa1-d692e2e18b0d)

### `_redraw_background` method docstring

Redraw the background of this button.<hr>

**[Parameters]**

- `label_text_bounding_box`: RectangleGeom
  - The bounding box of the label text.
- `prefix_icon`: Optional[FixedHtmlSvgIconBase]
  - An icon to display on the left side of the label.
- `suffix_icon`: Optional[FixedHtmlSvgIconBase]
  - An icon to display on the right side of the label.