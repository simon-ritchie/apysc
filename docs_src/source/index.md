# apysc documentation

Welcome to apysc documentation! apysc is the Python front-end library (currently developing and only works partially).

## Project links

- [GitHub](https://github.com/simon-ritchie/apysc)
  - Please leave a ⭐️star⭐️ if you favor the apysc library or have high hopes for the library's future!
- [PyPI](https://pypi.org/project/apysc/)

Other languages documentations: | English | [Japanese (日本語)](https://simon-ritchie.github.io/apysc/jp/jp_index.html) |

## Quick start guide

### Table of contents

```{toctree}
:maxdepth: 1
what_apysc_can_do
quick_start
import_conventions
recommended_type_checker_settings
```

---

## Container classes

The `Stage` is the apysc overall drawing area container, and the `Sprite` is the container class.

### Table of contents

```{toctree}
:maxdepth: 1
stage
sprite
```

---

## Exporting

The HTML and JavaScript exporting interfaces.

### Table of contents

```{toctree}
:maxdepth: 1
save_overall_html
display_on_jupyter
display_on_colaboratory
append_js_expression
```

---

## Child-related interfaces

The parent class, such as the `Sprite` or `Stage`, has the following interfaces:

### Table of contents

```{toctree}
:maxdepth: 1
add_child_and_remove_child
remove_children
contains
num_children
get_child_at
```

---

## apysc basic data classes

### Table of contents

```{toctree}
:maxdepth: 1
why_apysc_doesnt_use_python_builtin_data_type
fundamental_data_classes_value_interface
int_and_number
int_and_number_arithmetic_operations
int_and_number_comparison_operations
string.md
string_comparison_operations
string_addition_and_multiplication
boolean
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
dictionary
dictionary_generic
dictionary_get
dictionary_length
point2d
```

---

## DisplayObject and GraphicsBase classes

The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass and the base class of each graphic class, such as the `Rectangle` class.

### Table of contents

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

---

## Each graphic class

### Table of contents

```{toctree}
:maxdepth: 1
rectangle
circle
ellipse
line
polyline
polygon
```

---

## Graphics class

<br><iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>

### Table of contents

The `Graphics` class handles each vector graphics drawing.

```{toctree}
:maxdepth: 1
draw_interfaces_abstract
graphics
graphics_begin_fill
graphics_line_style
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
graphics_clear
```

---

## Common event interfaces

### Table of contents

```{toctree}
:maxdepth: 1
about_handler_options_type
event_prevent_default_and_stop_propagation
bind_and_trigger_custom_event
```

---

## MouseEvent class and mouse event binding

<br><iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

### Table of contents

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

---

## Branch instruction

### Table of contents

```{toctree}
:maxdepth: 1
if
elif
else
branch_instruction_variables_reverting_setting
return
```

---

## Loop

### Table of contents

```{toctree}
:maxdepth: 1
for
continue
```

---

## Timer

<br><iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>

### Table of contents

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
```

---

## Animation

<br><iframe src="static/animation_interfaces_abstract_rotation_around_center/index.html" width="150" height="150"></iframe>

### Table of contents

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
animation_skew_x
```

---

## Other manipulation interfaces

### Table of contents

```{toctree}
:maxdepth: 1
delete
```

---

## Debugging

### Table of contents

```{toctree}
:maxdepth: 1
trace
set_debug_mode
unset_debug_mode
add_debug_info_setting
```

---

## Testing

### Table of contents

```{toctree}
:maxdepth: 1
assertion_basic_behavior
assert_equal_and_not_equal
assert_true_and_false
assert_arrays_equal_and_arrays_not_equal
assert_dicts_equal_and_dicts_not_equal
assert_defined_and_undefined
```