# apysc documentation

Welcome to apysc documentation! apysc is a Python front-end library (currently developing and only works partially).

## Project links

- [GitHub](https://github.com/simon-ritchie/apysc)
  - Please leave a ⭐️star⭐️ if you favor the apysc library or have high hopes for the library's future!
- [PyPI](https://pypi.org/project/apysc/)

Other languages documentations: | English | [Japanese (日本語)](https://simon-ritchie.github.io/apysc/jp/jp_index.html) |

## Quick start guide

```{toctree}
:maxdepth: 1
what_apysc_can_do
quick_start
import_conventions
recommended_type_checker_settings
```

## Container classes

The `Stage` is the apysc overall drawing area container, and the `Sprite` is the container class.

```{toctree}
:maxdepth: 1
stage
sprite
```

## Exporting

The HTML and JavaScript exporting interfaces.

```{toctree}
:maxdepth: 1
save_overall_html
display_on_jupyter
display_on_colaboratory
append_js_expression
```

## Child-related interfaces

The parent class, such as the `Sprite` or `Stage`, has the following interfaces:

```{toctree}
:maxdepth: 1
add_child_and_remove_child
remove_children
contains
num_children
get_child_at
```

## apysc basic data classes

```{toctree}
:maxdepth: 1
why_apysc_doesnt_use_python_builtin_data_type
fundamental_data_classes_value_interface
to_string
```

### Int and Number classes

```{toctree}
:maxdepth: 1
int_and_number
int_and_number_arithmetic_operations
int_and_number_comparison_operations
int_and_number_to_fixed
int_and_number_to_hex
```

### String class

```{toctree}
:maxdepth: 1
string
string_comparison_operations
string_addition_and_multiplication
string_split
string_lstrip
string_strip
string_rstrip
string_length
string_apply_max_num_of_decimal_places
string_zfill
string_lower
string_upper
string_slice
```

### Boolean class and constants

```{toctree}
:maxdepth: 1
boolean
true_and_false
```

### Array class

```{toctree}
:maxdepth: 1
array
array_append_and_push
array_extend_and_concat
array_insert_and_insert_at
array_pop
array_remove_and_remove_at
array_sort
array_reverse
array_slice
array_length
array_join
array_index_of
array_clear
array_comparison
array_last_value
```

### Dictionary class

```{toctree}
:maxdepth: 1
dictionary
dictionary_generic
dictionary_get
dictionary_length
```

### Color class and constants

```{toctree}
:maxdepth: 1
color
colors
material_design_colors
colorless
color_from_rgb
red_color
green_color
blue_color
```

## DisplayObject and GraphicsBase classes

The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass and the base class of each graphic class, such as the `Rectangle` class.

```{toctree}
:maxdepth: 1
display_object
display_object_and_graphics_base_prop_abstract
display_object_x_and_y
display_object_parent
display_object_visible
display_object_get_and_set_css
display_object_mouse_event
graphics_base_fill_color
graphics_base_fill_alpha
graphics_base_line_color
graphics_base_line_alpha
graphics_base_line_thickness
graphics_base_line_dot_setting
graphics_base_line_dash_setting
graphics_base_line_round_dot_setting
graphics_base_line_dash_dot_setting
graphics_base_rotation_around_center
graphics_base_rotation_around_point
graphics_base_scale_from_center
graphics_base_scale_from_point
graphics_base_flip_interfaces
graphics_base_skew
```

## Each graphic class

```{toctree}
:maxdepth: 1
triangle
rectangle
circle
ellipse
line
polyline
polygon
path
```

## Graphics class

<br><iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>

The `Graphics` class handles each vector graphics drawing.

```{toctree}
:maxdepth: 1
draw_interfaces_abstract
graphics
graphics_begin_fill
graphics_line_style
graphics_draw_triangle
graphics_draw_rect
graphics_draw_round_rect
graphics_draw_circle
graphics_draw_ellipse
graphics_move_to_and_line_to
graphics_draw_line
graphics_draw_dotted_line
graphics_draw_dashed_line
graphics_draw_round_dotted_line
graphics_draw_dash_dotted_line
graphics_draw_polygon
graphics_draw_path
graphics_clear
```

## Text

```{toctree}
:maxdepth: 1
multi_line_text
text_fill_color
text_fill_alpha
text_bold
```

## SVG text

```{toctree}
:maxdepth: 1
svg_text
svg_text_span
```

## Geometry-related classes

```{toctree}
:maxdepth: 1
point2d
path_move_to
path_line_to
path_horizontal
path_vertical
path_close
path_bezier_2d
path_bezier_2d_continual
path_bezier_3d
path_bezier_3d_continual
rectangle_geom
get_bounds
```

## Common event interfaces

```{toctree}
:maxdepth: 1
about_handler_options_type
event_prevent_default_and_stop_propagation
bind_and_trigger_custom_event
```

## MouseEvent class and mouse event binding

<br><iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

```{toctree}
:maxdepth: 1
mouse_event_abstract
mouse_event_basic
click
dblclick
mousedown_and_mouseup
mouseover_and_mouseout
mousemove
```

## Branch instruction

```{toctree}
:maxdepth: 1
if
elif
else
branch_instruction_variables_reverting_setting
return
```

## Loop

```{toctree}
:maxdepth: 1
for_array_indices
for_array_values
for_array_indices_and_values
for_dict_keys
for_dict_values
for_dict_keys_and_values
continue
range
```

## Timer and enter-frame

<br><iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>

```{toctree}
:maxdepth: 1
timer
timer_event
timer_delay
fps
timer_repeat_count
timer_start_and_stop
timer_complete
timer_reset
enter_frame
unbind_enter_frame_and_unbind_enter_frame_all
```

## DateTime class

```{toctree}
:maxdepth: 1
datetime
datetime_year
datetime_month
datetime_day
datetime_hour
datetime_minute
datetime_second
datetime_millisecond
datetime_weekday_js_and_weekday_py
datetime_now
datetime_set_month_end
```

## TimeDelta class

```{toctree}
:maxdepth: 1
timedelta
timedelta_days
timedelta_total_seconds
```

## Animation

<br><iframe src="static/animation_interfaces_abstract_rotation_around_center/index.html" width="150" height="150"></iframe>

```{toctree}
:maxdepth: 1
animation_interfaces_abstract
animation_event
animation_duration
animation_delay
animation_return_value
animation_base_start
animation_complete
animation_method_chaining
animation_base_target
animation_pause_and_play
animation_reset
animation_finish
animation_reverse
animation_time
easing_enum
sequential_animation
animation_parallel
animation_move
animation_x
animation_y
animation_width_and_height
animation_fill_color
animation_fill_alpha
animation_line_color
animation_line_alpha
animation_line_thickness
animation_radius
animation_rotation_around_center
animation_rotation_around_point
animation_scale_x_and_y_from_center
animation_scale_x_and_y_from_point
```

## Mathematics

```{toctree}
:maxdepth: 1
math_min
math_max
math_trunc
```

## Other manipulation interfaces

```{toctree}
:maxdepth: 1
delete
```

## Debugging

```{toctree}
:maxdepth: 1
trace
set_debug_mode
unset_debug_mode
add_debug_info_setting
variable_name_suffix
```

## Testing

```{toctree}
:maxdepth: 1
assertion_basic_behavior
assert_equal_and_not_equal
assert_true_and_false
assert_greater_and_greater_equal
assert_less_and_less_equal
assert_arrays_equal_and_arrays_not_equal
assert_dicts_equal_and_dicts_not_equal
assert_defined_and_undefined
```