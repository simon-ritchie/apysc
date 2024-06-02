# `apysc._mask.svg_mask` docstrings

## Module summary

Implementation for the SVG mask class.

## `SvgMask` class docstring

The class for the object masking.

### `__init__` method docstring

The class for the SVG masking.<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `add_svg_masking_object` method docstring

Add an SVG masking object to this mask. This instance uses its masking object to mask other SVG graphics objects. It is possible to add multiple masking objects to a mask.<hr>

**[Parameters]**

- `masking_object`: FillColorMixIn
  - The masking object to add.
- `alpha`: float or Number, default 1.0
  - The alpha value for masking. 1.0 means fully visible, and 0.0 means fully invisible.

<hr>

**[Notes]**

This method updates the `masking_object` argument's fill color.