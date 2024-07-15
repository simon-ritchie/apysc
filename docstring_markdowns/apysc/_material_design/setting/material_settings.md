# `apysc._material_design.setting.material_settings` docstrings

## Module summary

The static class implementation for the material design settings.

## `MaterialSettings` class docstring

### `_delete_current_brightness_string_attr` method docstring

Delete the `_current_brightness_string` attribute.

### `_enable_color_scheme_setting` method docstring

Enable the color scheme setting.

### `_initialize_attrs` method docstring

Initialize each attribute if it has not been initialized yet.

### `_initialize_color_scheme_setting_is_enabled_if_not_initialized` method docstring

Initialize the `_color_scheme_setting_is_enabled` attribute if it has not been initialized yet.

### `_initialize_current_brightness_string_if_not_initialized` method docstring

Initialize the `_current_brightness_string` attribute string if it has not been initialized yet.

### `_reset_settings` method docstring

Reset all settings of this class.

### `color_scheme_setting_is_enabled` method docstring

Get a boolean whether the color scheme setting is enabled or not.<hr>

**[Returns]**

- `result`: Boolean
  - If the color scheme setting is enabled, then this method returns True.

### `current_color_scheme_is_dark_color_scheme` method docstring

Get a boolean whether the current color scheme is the dark color scheme or not.<hr>

**[Returns]**

- `result`: Boolean
  - If the current color scheme is the dark color scheme, then this method returns True.

### `current_color_scheme_is_light_color_scheme` method docstring

Get whether the current color scheme is the light color scheme or not.<hr>

**[Returns]**

- `result`: Boolean
  - If the current color scheme is the light color scheme, then this method returns True.

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

- `color_scheme`: MaterialColorScheme
  - Color scheme to set.

<hr>

**[Raises]**

- ValueError: If you call this class method multiple times.

### `set_font_family` method docstring

Set a font-family setting.<hr>

**[Parameters]**

- `font_family`: Union[Array[String], List[str]]
  - A font-family setting.

### `set_light_color_scheme` method docstring

Set a color scheme setting.<hr>

**[Parameters]**

- `color_scheme`: MaterialColorScheme
  - Color scheme to set.

<hr>

**[Raises]**

- ValueError: If you call this class method multiple times.

### `switch_to_dark_color_scheme` method docstring

Switch the current color scheme to the dark color scheme.

### `switch_to_light_color_scheme` method docstring

Switch the current color scheme to the light color scheme.