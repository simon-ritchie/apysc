# `apysc._mask.svg_mask` docstrings

## Module summary

Implementation for the SVG mask class.

## `SvgMask` class docstring

The class for the object masking.<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

<hr>

**[References]**

- [SvgMask class and its related interfaces](https://simon-ritchie.github.io/apysc/en/svg_mask.html)

### `__init__` method docstring

The class for the SVG masking.<hr>

**[Parameters]**

- `variable_name_suffix`: str, default ""
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

<hr>

**[References]**

- [SvgMask class and its related interfaces](https://simon-ritchie.github.io/apysc/en/svg_mask.html)

### `_append_constructor_expression` method docstring

Append a constructor expression.

### `add_svg_masking_object` method docstring

Add an SVG masking object to this mask. This instance uses its masking object to mask other SVG graphics objects. It is possible to add multiple masking objects to a mask.<hr>

**[Parameters]**

- `masking_object`: FillColorMixIn
  - The masking object to add.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> _ = ap.Stage()
>>> mask: ap.SvgMask = ap.SvgMask()
>>> circle: ap.Circle = ap.Circle(
...     x=50, y=50, radius=50, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> mask.add_svg_masking_object(masking_object=circle)
>>> rectangle: ap.Rectangle = ap.Rectangle(
...     x=0, y=0, width=100, height=100, fill_color=ap.Colors.CYAN_00AAFF
... )
>>> rectangle.svg_mask = mask
```

<hr>

**[References]**

- [SvgMask class and its related interfaces](https://simon-ritchie.github.io/apysc/en/svg_mask.html)