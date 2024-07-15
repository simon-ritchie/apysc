# `apysc._material_design.setting.material_settings_utils` docstrings

## Module summary

The utility module for getting material design settings.

## `MaterialSettingsUtils` class docstring

### `_get_target_color_and_add_expressions_by_color_name` method docstring

Get a target color and add expressions of the specified color name.<hr>

**[Parameters]**

- `color_name`: MaterialColorNames
  - A target color name (e.g., "primary").
- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target primary color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `_initialize_fixed_color_scheme_if_not_initialized` method docstring

Initialize the `_fixed_color_scheme` attribute if it has not been initialized yet.

### `_set_color_scheme_value_and_append_expression` method docstring

Set a color scheme value to the target color and append color-related expressions.<hr>

**[Parameters]**

- `color_scheme`: Optional[MaterialColorScheme]
  - A target color scheme.
- `color_name`: MaterialColorNames
  - A target color name (e.g., "primary").
- `target_color`: Color
  - A target color.

<hr>

**[Notes]**

If the specified `color_scheme` is `None`, then this method will do nothing.

### `get_primary_color` method docstring

Get a primary color setting from setting.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target primary color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.