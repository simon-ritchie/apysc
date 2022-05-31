# `apysc._validation.display_validation` docstrings

## Module summary

Each display's validation implementations. Mainly following interfaces are defined: <br>・validate_stage Validate whether the specified instance is Stage type or not. <br>・validate_display_object Validate whether a specified instance is the `DisplayObject` type or its subclass type (e.g., `Sprite`). <br>・validate_display_object_container Validate whether a specified instance is a container type of a `DisplayObject` instance (e.g., `Sprite`, `Stage`). <br>・validate_sprite Validate specified instance is Sprite type. <br>・validate_graphics Validate specified instance is Graphics type. <br>・validate_line_cap Validate specified line cap style setting. <br>・validate_line_joints Validate specified line joints style setting. <br>・validate_multiple_line_settings_are_not_set Validate that there are no multiple line settings (dotted, dashed, and so on).

## `validate_display_object` function docstring

Validate whether a specified instance is the `DisplayObject` type or its subclass type (e.g., Sprite).<hr>

**[Parameters]**

- `display_object`: DisplayObject
  - A `DisplayObject` instance to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified instance is not `DisplayObject` type or its subclass type.

## `validate_display_object_container` function docstring

Validate whether a specified instance is a container type of a `DisplayObject` instance (e.g., `Sprite`, `Stage`).<hr>

**[Parameters]**

- `container_object`: Any
  - A target container instance to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified instance is not a container type instance.

## `validate_graphics` function docstring

Validate specified instance is Graphics type.<hr>

**[Parameters]**

- `graphics`: Graphics
  - Graphics instance to check.

<hr>

**[Raises]**

- ValueError: If a specified instance is not Graphics type.

## `validate_line_cap` function docstring

Validate specified line cap style setting.<hr>

**[Parameters]**

- `cap`: LineCaps or String
  - Target line cap style setting to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If a specified cap setting type is not LineCaps or not defined string value.

## `validate_line_joints` function docstring

Validate specified line joints style setting.<hr>

**[Parameters]**

- `joints`: LineJoints or String
  - Target line joints style setting to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If specified joints setting type is not LineJoints or not defined string value.

## `validate_multiple_line_settings_are_not_set` function docstring

Validate that there are no multiple line settings (dotted, dashed, and so on).<hr>

**[Parameters]**

- `any_instance`: Any
  - Any instance to check.
- `additional_err_msg`: str, optional
  - An additional error message to display.

<hr>

**[Raises]**

- ValueError: If there are multiple line settings.

## `validate_sprite` function docstring

Validate specified instance is Sprite type.<hr>

**[Parameters]**

- `sprite`: Sprite
  - Sprite instance to check.

<hr>

**[Raises]**

- ValueError: If a specified instance is not Sprite type.

## `validate_stage` function docstring

Validate whether the specified instance is Stage type or not.<hr>

**[Parameters]**

- `stage`: Stage
  - Stage instance to check.

<hr>

**[Raises]**

- ValueError: If a specified instance is not stage type.