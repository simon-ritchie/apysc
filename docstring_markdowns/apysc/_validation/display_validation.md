# `apysc._validation.display_validation` docstrings

## Module summary

Each display's validation implementations. Mainly following interfaces are defined: <br>・validate_stage Validate whether the specified instance is Stage type or not. <br>・validate_display_object Validate specified instance is DisplayObject type or it's subclass type (e.g., Sprite). <br>・validate_sprite Validate specified instance is Sprite type. <br>・validate_graphics Validate specified instance is Graphics type. <br>・validate_line_cap Validate specified line cap style setting. <br>・validate_line_joints Validate specified line joints style setting. <br>・validate_multiple_line_settings_isnt_set Validate multiple line settings (dotted, dashed, and so on) is not set.

## `validate_display_object` function docstring

Validate specified instance is DisplayObject type or it's subclass type (e.g., Sprite).<hr>

**[Parameters]**

- `display_object`: DisplayObject
  - DisplayObject instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not DisplayObject type or it's subclass type.

## `validate_graphics` function docstring

Validate specified instance is Graphics type.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not Graphics type.

## `validate_line_cap` function docstring

Validate specified line cap style setting.<hr>

**[Parameters]**

- `cap`: LineCaps or String
  - Target line cap style setting to check.

<hr>

**[Raises]**

- ValueError: If specified cap setting type is not LineCaps or not defined string value.

## `validate_line_joints` function docstring

Validate specified line joints style setting.<hr>

**[Parameters]**

- `joints`: LineJoints or String
  - Target line joints style setting to check.

<hr>

**[Raises]**

- ValueError: If specified joints setting type is not LineJoints or not defined string value.

## `validate_multiple_line_settings_isnt_set` function docstring

Validate multiple line settings (dotted, dashed, and so on) is not set.<hr>

**[Parameters]**

- `any_instance`: Any
  - Any instance to check.

<hr>

**[Raises]**

- ValueError: If multiple line settings are set.

## `validate_sprite` function docstring

Validate specified instance is Sprite type.<hr>

**[Parameters]**

- `sprite`: Sprite
  - Sprite instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not Sprite type.

## `validate_stage` function docstring

Validate whether the specified instance is Stage type or not.<hr>

**[Parameters]**

- `stage`: Stage
  - Stage instance to check.

<hr>

**[Raises]**

- ValueError: If specified instance is not stage type.