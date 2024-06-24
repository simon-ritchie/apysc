# `apysc._material_design.setting.material_settings` docstrings

## Module summary

The static class implementation for the material design settings.

## `MaterialSettings` class docstring

### `_delete_current_brightness_string_attr` method docstring

Delete the `_current_brightness_string` attribute.

### `_initialize_current_brightness_string_if_not_initialized` method docstring

Initialize the `_current_brightness_string` attribute string if it has not been initialized yet.

### `get_dark_color_scheme` method docstring

Get a dark color scheme setting.<hr>

**[Returns]**

- `color_scheme`: MaterialColorScheme or None
  - A dark color scheme setting. If the color scheme is not set, this property becomes None.

### `get_light_color_scheme` method docstring

Get a light color scheme setting.<hr>

**[Returns]**

- `color_scheme`: MaterialColorScheme or None
  - A light color scheme setting. If the color scheme is not set, this property becomes None.

### `set_dark_color_scheme` method docstring

Set a dark color scheme setting.<hr>

**[Parameters]**

- `color_scheme`: MaterialColorScheme or None
  - Color scheme to set. If None is specified, the color scheme will be removed.

### `set_light_color_scheme` method docstring

Set a color scheme setting.<hr>

**[Parameters]**

- `color_scheme`: MaterialColorScheme or None
  - Color scheme to set. If None is specified, the color scheme will be removed.

### `switch_to_dark_color_scheme` method docstring

Switch the current color scheme to the dark color scheme.

### `switch_to_light_color_scheme` method docstring

Switch the current color scheme to the light color scheme.