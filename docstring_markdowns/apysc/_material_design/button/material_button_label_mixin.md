# `apysc._material_design.button.material_button_label_mixin` docstrings

## Module summary

The mix-in class implementation for the material design button's label.

## `MaterialButtonLabelMixIn` class docstring

### `_initialize_label` method docstring

Initialize the label setting with the specified argument.<hr>

**[Parameters]**

- `label`: Union[str, String]
  - A label text to display on this button.
- `text_color`: Color
  - The color of the label text.
- `font_family`: Optional[Union[Array[String], List[str]]]
  - A font-family setting.
- `font_size`: Union[int, Int]
  - A font-size setting.

### `_locate_label_text` method docstring

Locate the label text.<hr>

**[Parameters]**

- `label_text_bounding_box`: RectangleGeom
  - The bounding box of the label text.
- `prefix_icon`: Optional[FixedHtmlSvgIconBase]
  - An icon to display on the left side of the label.