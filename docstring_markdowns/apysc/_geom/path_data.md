# apysc._geom.path_data docstrings

## Module summary

Class definitions of each path data class.

## PathBezier2D class docstring

Path data class for the svg's `2D bezier curve` (Q).

Path data class for the svg's `2D bezier curve` (Q).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `2D bezier curve` (Q).<hr>

**[Parameters]**

- `control_x`: int or Int
  - X-coordinate of the bezier's control point.
- `control_y`: int or Int
  - Y-coordinate of the bezier's control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_control_x_linking_setting method docstring

Append a control_x attribute linking setting.

### _append_control_y_linking_setting method docstring

Append a control_y attribute linking setting.

### _append_dest_x_linking_setting method docstring

Append a dest_x attribute linking setting.

### _append_dest_y_linking_setting method docstring

Append a dest_y linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_control_x_if_not_initialized method docstring

Initialize the _control_x attribute if it hasn't been initialized yet.

### _initialize_control_y_if_not_initialized method docstring

Initialize the _control_y attribute if it hasn't been initialized yet.

### _initialize_dest_x_if_not_initialized method docstring

Initialize the _dest_x attribute if it hasn't been initialized yet.

### _initialize_dest_y_if_not_initialized method docstring

Initialize the _dest_y attribute if it hasn't been initialized yet.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `control_x`: int or Int
  - X-coordinate of the bezier's control point.
- `control_y`: int or Int
  - Y-coordinate of the bezier's control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_2d: ap.PathBezier2D = ap.PathBezier2D(
...     control_x=50, control_y=0,
...     dest_x=100, dest_y=50)
>>> bezier_2d.update_path_data(
...     control_x=150, control_y=100,
...     dest_x=200, dest_y=150)
>>> bezier_2d.control_x
Int(150)

>>> bezier_2d.control_y
Int(100)

>>> bezier_2d.dest_x
Int(200)

>>> bezier_2d.dest_y
Int(150)
```

## PathBezier2DContinual class docstring

Path data class for the svg's `continual 2D bezier curve` (T).

Path data class for the svg's `continual 2D bezier curve` (T).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...         ap.PathBezier2DContinual(x=150, y=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `continual 2D bezier curve` (T).<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...         ap.PathBezier2DContinual(x=150, y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_x_linking_setting method docstring

Append a x attribute linking setting.

### _append_y_linking_setting method docstring

Append a y attribute linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_x_if_not_initialized method docstring

Initialize the _x attribute if it hasn't been initialized yet.

### _initialize_y_if_not_initialized method docstring

Initialize the _y attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_2d_continual = ap.PathBezier2DContinual(x=100, y=50)
>>> bezier_2d_continual.update_path_data(x=150, y=100)
>>> bezier_2d_continual.x
Int(150)

>>> bezier_2d_continual.y
Int(100)
```

## PathBezier3D class docstring

Path data class for the svg's `3D bezier curve` (C).

Path data class for the svg's `3D bezier curve` (C).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `3D bezier curve` (C).<hr>

**[Parameters]**

- `control_x1`: int or Int
  - X-coordinate of the bezier's first control point.
- `control_y1`: int or Int
  - Y-coordinate of the bezier's first control point.
- `control_x2`: int or Int
  - X-coordinate of the bezier's second control point.
- `control_y2`: int or Int
  - Y-coordinate of the bezier's second control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_control_x1_linking_setting method docstring

Append a control_x1 attribute to the linking setting.

### _append_control_x2_linking_setting method docstring

Append a control_x2 attribute linking setting.

### _append_control_y1_linking_setting method docstring

Append a control_y1 attribute linking setting.

### _append_control_y2_linking_setting method docstring

Append a control_y2 attribute linking setting.

### _append_dest_x_linking_setting method docstring

Append a dest_x attribute linking setting.

### _append_dest_y_linking_setting method docstring

Append a dest_y linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_control_x1_if_not_initialized method docstring

Initialize the _control_x1 attribute if it hasn't been initialized yet.

### _initialize_control_x2_if_not_initialized method docstring

Initialize the _control_x2 attribute if it hasn't been initialized yet.

### _initialize_control_y1_if_not_initialized method docstring

Initialize the _control_y1 attribute if it hasn't been initialized yet.

### _initialize_control_y2_if_not_initialized method docstring

Initialize the _control_y2 attribute if it hasn't been initialized yet.

### _initialize_dest_x_if_not_initialized method docstring

Initialize the _dest_x attribute if it hasn't been initialized yet.

### _initialize_dest_y_if_not_initialized method docstring

Initialize the _dest_y attribute if it hasn't been initialized yet.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `control_x1`: int or Int
  - X-coordinate of the bezier's first control point.
- `control_y1`: int or Int
  - Y-coordinate of the bezier's first control point.
- `control_x2`: int or Int
  - X-coordinate of the bezier's second control point.
- `control_y2`: int or Int
  - Y-coordinate of the bezier's second control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_3d_continual = ap.PathBezier3D(
...     control_x1=0, control_y1=0,
...     control_x2=50, control_y2=0,
...     dest_x=50, dest_y=50)
>>> bezier_3d_continual.update_path_data(
...     control_x1=100, control_y1=100,
...     control_x2=150, control_y2=100,
...     dest_x=150, dest_y=150)
>>> bezier_3d_continual.control_x1
Int(100)

>>> bezier_3d_continual.control_y1
Int(100)

>>> bezier_3d_continual.control_x2
Int(150)

>>> bezier_3d_continual.control_y2
Int(100)

>>> bezier_3d_continual.dest_x
Int(150)

>>> bezier_3d_continual.dest_y
Int(150)
```

## PathBezier3DContinual class docstring

Path data class for the svg's `continual 3D bezier curve` (S).

Path data class for the svg's `continual 3D bezier curve` (S).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `continual 3D bezier curve` (S).<hr>

**[Parameters]**

- `control_x`: int or Int
  - X-coordinate of the bezier's control point.
- `control_y`: int or Int
  - Y-coordinate of the bezier's control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_control_x_linking_setting method docstring

Append a control_x attribute linking setting.

### _append_control_y_linking_setting method docstring

Append a control_y attribute linking setting.

### _append_dest_x_linking_setting method docstring

Append a dest_x attribute linking setting.

### _append_dest_y_linking_setting method docstring

Append a dest_y linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_control_x_if_not_initialized method docstring

Initialize the _control_x attribute if it hasn't been initialized yet.

### _initialize_control_y_if_not_initialized method docstring

Initialize the _control_y attribute if it hasn't been initialized yet.

### _initialize_dest_x_if_not_initialized method docstring

Initialize the _dest_x attribute if it hasn't been initialized yet.

### _initialize_dest_y_if_not_initialized method docstring

Initialize the _dest_y attribute if it hasn't been initialized yet.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `control_x`: int or Int
  - X-coordinate of the bezier's control point.
- `control_y`: int or Int
  - Y-coordinate of the bezier's control point.
- `dest_x`: int or Int
  - X-coordinate of the destination point.
- `dest_y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> bezier_3d_continual = ap.PathBezier3DContinual(
...     control_x=100, control_y=100,
...     dest_x=100, dest_y=50)
>>> bezier_3d_continual.update_path_data(
...     control_x=150, control_y=150,
...     dest_x=150, dest_y=100)
>>> bezier_3d_continual.control_x
Int(150)

>>> bezier_3d_continual.control_y
Int(150)

>>> bezier_3d_continual.dest_x
Int(150)

>>> bezier_3d_continual.dest_y
Int(100)
```

## PathClose class docstring

Path data class for the svg's `close path` (Z).

Path data class for the svg's `close path` (Z).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __init__ method docstring

Path data class for the svg's `close path` (Z).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ])
```

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

## PathData class docstring

Class definitions of each path data class.

Class definitions of each path data class.

### PathBezier2D method docstring

Path data class for the svg's `2D bezier curve` (Q).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...     ])
```

### PathBezier2DContinual method docstring

Path data class for the svg's `continual 2D bezier curve` (T).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier2D(
...             control_x=50, control_y=0,
...             dest_x=100, dest_y=50),
...         ap.PathBezier2DContinual(x=150, y=50),
...     ])
```

### PathBezier3D method docstring

Path data class for the svg's `3D bezier curve` (C).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### PathBezier3DContinual method docstring

Path data class for the svg's `continual 3D bezier curve` (S).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathBezier3D(
...             control_x1=0, control_y1=0,
...             control_x2=50, control_y2=0,
...             dest_x=50, dest_y=50),
...         ap.PathBezier3DContinual(
...             control_x=100, control_y=100,
...             dest_x=100, dest_y=50),
...     ])
```

### PathClose method docstring

Path data class for the svg's `close path` (Z).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=00),
...         ap.PathLineTo(x=50, y=0),
...         ap.PathLineTo(x=50, y=50),
...         ap.PathClose(),
...     ])
```

### PathHorizontal method docstring

Path data class for the svg's `horizontal line` (H).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathHorizontal(x=50),
...     ])
```

### PathLineTo method docstring

Path data class for the svg's `line to` (L).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ])
```

### PathMoveTo method docstring

Path data class for the svg's `move to` (M).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ])
```

### PathVertical method docstring

Path data class for the svg's `vertical line` (V).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathVertical(y=100),
...     ])
```

### __init__ method docstring

Initialize self. See help(type(self)) for accurate signature.

## PathHorizontal class docstring

Path data class for the svg's `horizontal line` (H).

Path data class for the svg's `horizontal line` (H).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathHorizontal(x=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `horizontal line` (H).<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathHorizontal(x=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_x_linking_setting method docstring

Append a x attribute linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_x_if_not_initialized method docstring

Initialize the _x attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> path_horizontal: ap.PathHorizontal = ap.PathHorizontal(x=50)
>>> path_horizontal.update_path_data(x=100)
>>> path_horizontal.x
Int(100)
```

## PathLineTo class docstring

Path data class for the svg's `line to` (L).

Path data class for the svg's `line to` (L).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `line to` (L).<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_x_linking_setting method docstring

Append a x attribute linking setting.

### _append_y_linking_setting method docstring

Append a y attribute linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_x_if_not_initialized method docstring

Initialize the _x attribute if it hasn't been initialized yet.

### _initialize_y_if_not_initialized method docstring

Initialize the _y attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> line_to: ap.PathLineTo = ap.PathLineTo(x=50, y=50)
>>> line_to.update_path_data(x=100, y=150)
>>> line_to.x
Int(100)

>>> line_to.y
Int(150)
```

## PathMoveTo class docstring

Path data class for the svg's `move to` (M).

Path data class for the svg's `move to` (M).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `move to` (M).<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathLineTo(x=50, y=50),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_x_linking_setting method docstring

Append a x attribute linking setting.

### _append_y_linking_setting method docstring

Append a y attribute linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_x_if_not_initialized method docstring

Initialize the _x attribute if it hasn't been initialized yet.

### _initialize_y_if_not_initialized method docstring

Initialize the _y attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `x`: int or Int
  - X-coordinate of the destination point.
- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> move_to: ap.PathMoveTo = ap.PathMoveTo(x=50, y=50)
>>> move_to.update_path_data(x=100, y=150)
>>> move_to.x
Int(100)

>>> move_to.y
Int(150)
```

## PathVertical class docstring

Path data class for the svg's `vertical line` (V).

Path data class for the svg's `vertical line` (V).<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathVertical(y=100),
...     ])
```

### ABCMeta method docstring

Metaclass for defining Abstract Base Classes (ABCs). Use this metaclass to create an ABC. An ABC can be subclassed directly, and then acts as a mix-in class. You can also register unrelated concrete classes (even built-in classes) and unrelated ABCs as 'virtual subclasses' -- these and their descendants will be considered subclasses of the registering ABC by the built-in issubclass() function, but the registering ABC won't show up in their MRO (Method Resolution Order) nor will method implementations defined by the registering ABC be callable (not even via super()).

### __eq__ method docstring

Equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### __init__ method docstring

Path data class for the svg's `vertical line' (V).<hr>

**[Parameters]**

- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean, default False
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> stage: ap.Stage = ap.Stage()
>>> sprite: ap.Sprite = ap.Sprite()
>>> sprite.graphics.line_style(color='#fff', thickness=3)
>>> path: ap.Path = sprite.graphics.draw_path(
...     path_data_list=[
...         ap.PathMoveTo(x=0, y=50),
...         ap.PathVertical(y=100),
...     ])
```

### __ne__ method docstring

Not equal comparison method.<hr>

**[Parameters]**

- `other`: Any
  - Other value to compare.

<hr>

**[Returns]**

- `result`: Boolean
  - Comparison result.

### _append_applying_new_attr_val_exp method docstring

Append the expression of applying new attribute value to each stacked value.<hr>

**[Parameters]**

- `new_attr`: Int or Number or String or Boolean
  - New attribute value.
- `attr_name`: str
  - Target attribute name.

### _append_attr_to_linking_stack method docstring

Append an attribute to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

### _append_y_linking_setting method docstring

Append a y attribute linking setting.

### _delete_snapshot_exists_val method docstring

Delete boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _get_next_snapshot_name method docstring

Get a next snapshot name.<hr>

**[Returns]**

- `snapshot_name`: str
  - Next snapshot name.

### _get_svg_char method docstring

Get a SVG character (e.g., 'M' or 'm') from the current setting.<hr>

**[Returns]**

- `svg_char`: String
  - Target SVG character.

### _get_svg_str method docstring

Get a path's SVG string created with the current setting.<hr>

**[Returns]**

- `svg_str`: str
  - A path's SVG string created with the current setting.

### _initialize_attr_linking_stack method docstring

Initialize the _attr_linking_stack attribute if it hasn't been initialized yet.<hr>

**[Parameters]**

- `attr_name`: str
  - Target attribute name.

### _initialize_relative_if_not_initialized method docstring

Initialize the _relative attribute if it hasn't been initialized yet.

### _initialize_ss_exists_val_if_not_initialized method docstring

Initialize _snapshot_exists_ value it hasn't been initialized yet.

### _initialize_y_if_not_initialized method docstring

Initialize the _y attribute if it hasn't been initialized yet.

### _is_target_attr_already_linked method docstring

Get a boolean value whether a specified attribute has already been appended to the linking attribute stack.<hr>

**[Parameters]**

- `attr`: Int or Number or String or Boolean
  - Target attribute to be appended.
- `attr_name`: str
  - Target attribute name.

<hr>

**[Returns]**

- `result`: bool
  - If a specified attribute has already been appended to the linking stack, this value will be True.

### _make_snapshot method docstring

Make a value's snapshot.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _revert method docstring

Revert a value if snapshot exists.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_make_snapshot_methods method docstring

Run all _make_snapshot methods. If instance is multiple inheritance one, and each has RevertInterface, then each _make_snapshot methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_all_revert_methods method docstring

Run all _revert methods. If instance is multiple inheritance one, and each has RevertInterface, then each _revert methods will be called.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_make_snapshot_methods_recursively method docstring

Run base classes make_snapshot methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _run_base_cls_revert_methods_recursively method docstring

Run base classes revert methods recursively.<hr>

**[Parameters]**

- `class_`: type
  - Target type.
- `snapshot_name`: str
  - Target snapshot name.

### _set_single_snapshot_val_to_dict method docstring

Set a single snapshot value to the specified name dictionary.<hr>

**[Parameters]**

- `dict_name`: str
  - Target dictionary name.
- `value`: Any
  - Target value.
- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Notes]**

If a snapshot value of the same name already exists, the process will be stopped.

### _set_snapshot_exists_val method docstring

Set boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

### _snapshot_exists method docstring

Get a boolean value whether snapshot value exists or not.<hr>

**[Parameters]**

- `snapshot_name`: str
  - Target snapshot name.

<hr>

**[Returns]**

- `snapshot_exists`: bool
  - Boolean value whether snapshot value exists or not.

### update_path_data method docstring

Update the path's data settings.<hr>

**[Parameters]**

- `y`: int or Int
  - Y-coordinate of the destination point.
- `relative`: bool or Boolean
  - The boolean value indicating whether the path coordinates are relative or not (absolute).

<hr>

**[Examples]**

```py
>>> import apysc as ap
>>> path_vertical: ap.PathVertical = ap.PathVertical(y=50)
>>> path_vertical.update_path_data(y=100)
>>> path_vertical.y
Int(100)
```