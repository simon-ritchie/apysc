# `apysc._validation.path_validation` docstrings

## Module summary

Path's validation implementations.

## `_validate_bezier_2d_continual_pre_data` function docstring

Validate a preceding data of `PathBezier2DContinual` instance in list is a `PathBezier2D` or `PathBezier2DContinual`.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.

<hr>

**[Raises]**

- ValueError: If a preceding data of `PathBezier2DContinual` instance is not a `PathBezier2D` or `PathBezier2DContinual` one.

## `_validate_bezier_3d_continual_pre_data` function docstring

Validate a preceding data of `PathBezier3DContinual` instance in list is a `PathBezier3D` or `PathBezier3DContinual`.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.

<hr>

**[Raises]**

- ValueError: If a preceding data of `PathBezier3DContinual` instance is not a `PathBezier3D` or `PathBezier3DContinual` one.

## `validate_path_data_list` function docstring

Validate a specified path data list.<hr>

**[Parameters]**

- `path_data_list`: list of PathDataBase
  - Target path data settings, such as the ap.PathData.MoveTo.

<hr>

**[Raises]**

- ValueError: <br> ・If a specified path data list is empty. <br> ・If a preceding data of `PathBezier2DContinual` instance is not a `PathBezier2D` or `PathBezier2DContinual` one. <br> ・If a preceding data of `PathBezier3DContinual` instance is not a `PathBezier3D` or `PathBezier3DContinual` one.