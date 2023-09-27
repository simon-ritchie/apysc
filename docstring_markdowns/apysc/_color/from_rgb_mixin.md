# `apysc._color.from_rgb_mixin` docstrings

## Module summary

The mix-in class for the `from_rgb` method.

## `_get_py_str_from_rgb` function docstring

Get a Python string from RGB values.<hr>

**[Parameters]**

- `red`: Union[int, Int]
  - The red color.
- `green`: Union[int, Int]
  - The green color.
- `blue`: Union[int, Int]
  - The blue color.

<hr>

**[Returns]**

- `py_str`: str
  - A Python string, e.g., '#0000ff'.

## `FromRgbMixIn` class docstring

### `from_rgb` method docstring

Create a color instance from RGB (red, green, and blue) values.<hr>

**[Parameters]**

- `red`: Union[int, Int]
  - A red color value (0 to 255).
- `green`: Union[int, Int]
  - A green color value (0 to 255).
- `blue`: Union[int, Int]
  - A blue color value (0 to 255).
- `variable_name_suffix`: str, default ''
  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.

<hr>

**[Returns]**

- `color`: Color
  - A created color instance.

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> color: ap.Color = ap.Color.from_rgb(red=0, green=255, blue=0)
>>> color
Color("#00FF00")
```

<hr>

**[References]**

- [Color class from_rgb class method](https://simon-ritchie.github.io/apysc/en/color_from_rgb.html)
- [Color class](https://simon-ritchie.github.io/apysc/en/color.html)