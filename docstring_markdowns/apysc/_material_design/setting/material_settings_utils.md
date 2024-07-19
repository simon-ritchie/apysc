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

### `get_error_color` method docstring

Get an error color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `error` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_error_container_color` method docstring

Get an `error_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `error_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_error_color` method docstring

Get an `on_error` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_error` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_error_container_color` method docstring

Get an `on_error_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_error_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_primary_color` method docstring

Get an `on_primary` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_primary` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_primary_container_color` method docstring

Get an `on_primary_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_primary_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_secondary_color` method docstring

Get an `on_secondary` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_secondary` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_secondary_container_color` method docstring

Get an `on_secondary_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_secondary_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_tertiary_color` method docstring

Get an `on_tertiary` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_tertiary` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_on_tertiary_container_color` method docstring

Get an `on_tertiary_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_tertiary_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_outline_color` method docstring

Get an `outline` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `outline` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_outline_variant_color` method docstring

Get an `outline_variant` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `outline_variant` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_primary_color` method docstring

Get a primary color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `primary` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_primary_container_color` method docstring

Get a `primary_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `primary_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_secondary_color` method docstring

Get a secondary color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `secondary` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_secondary_container_color` method docstring

Get a `secondary_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `secondary_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_surface` method docstring

Get a surface color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `surface` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_tertiary_color` method docstring

Get a `tertiary` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `tertiary` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `get_tertiary_container_color` method docstring

Get a `tertiary_container` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `tertiary_container` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.

### `on_surface_color` method docstring

Get an `on_surface` color setting from a setting or argument.<hr>

**[Parameters]**

- `argument_color`: Optional[Color]
  - A specified argument color.

<hr>

**[Returns]**

- `target_color`: Color
  - A target `on_surface` color. This value becomes according to the following priorities: 1. If the `argument_color` is not the `None` 2. If a color scheme is set in the `MaterialSettings` 3. A fixed color value.