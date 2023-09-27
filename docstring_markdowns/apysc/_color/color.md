# `apysc._color.color` docstrings

## Module summary

The color class implementation.

## `Color` class docstring

The color class implementation.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color("#0af")
>>> color
Color("#00aaff")

>>> color = ap.Color("#ffffff")
>>> color
Color("#ffffff")
```

<hr>

**[References]**

- [Color class](https://simon-ritchie.github.io/apysc/en/color.html)
- [Colors class](https://simon-ritchie.github.io/apysc/en/colors.html)
- [MaterialDesignColors class](https://simon-ritchie.github.io/apysc/en/material_design_colors.html)
- [COLORLESS constant](https://simon-ritchie.github.io/apysc/en/colorless.html)
- [Color class from_rgb class method](https://simon-ritchie.github.io/apysc/en/color_from_rgb.html)

### `__eq__` method docstring

Comparison method between two color values.<hr>

**[Parameters]**

- `other`: Color
  - The other color value.

<hr>

**[Returns]**

- `result`: Boolean
  - If the two color values are equal, this interface returns True.

### `__init__` method docstring

The color class implementation.<hr>

**[Parameters]**

- `value`: str or String
  - A hexadecimal color code string (e.g., '#000000').
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color("#0af")
>>> color
Color("#00aaff")

>>> color = ap.Color("#ffffff")
>>> color
Color("#ffffff")
```

<hr>

**[References]**

- [Color class](https://simon-ritchie.github.io/apysc/en/color.html)
- [Colors class](https://simon-ritchie.github.io/apysc/en/colors.html)
- [MaterialDesignColors class](https://simon-ritchie.github.io/apysc/en/material_design_colors.html)
- [COLORLESS constant](https://simon-ritchie.github.io/apysc/en/colorless.html)
- [Color class from_rgb class method](https://simon-ritchie.github.io/apysc/en/color_from_rgb.html)

### `__repr__` method docstring

Get a representation string of this instance.<hr>

**[Returns]**

- `repr_str`: str
  - Representation string of this instance.