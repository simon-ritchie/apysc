# apysc documentation

Welcome to apysc documentation! apysc is the Python front-end library (currently developing and only works partially).

## Project links

- [GitHub](https://github.com/simon-ritchie/apysc)
  - Please leave a ⭐️star⭐️ if you favor the apysc library or have high hopes for the library's future!
- [Twitter](https://twitter.com/apysc)
  - The progress and updates are informed on Twitter. Please follow!
- [PyPI](https://pypi.org/project/apysc/)

## Quick start guide

### Table of contents

- [What apysc can do in its current implementation](what_apysc_can_do.md)
- [Quick start guide](quick_start.md)
- [import conventions](import_conventions.md)

---

## Container classes

The `Stage` is the apysc overall drawing area container, and the `Sprite` is the container class.

### Table of contents

- [Stage class](stage.md)
- [Sprite class](sprite.md)

---

## Exporting

The HTML and JavaScript exporting interfaces.

### Table of contents

- [save_overall_html interface](save_overall_html.md)
- [display_on_jupyter interface](display_on_jupyter.md)
- [display_on_colaboratory interface](display_on_colaboratory.md)
- [append_js_expression interface](append_js_expression.md)

---

## Child-related interfaces

The parent class, such as the `Sprite` or `Stage` have the following interfaces:

### Table of contents

- [add_child and remove_child interfaces](add_child_and_remove_child.md)
- [contains interface](contains.md)
- [num_children interface](num_children.md)
- [get_child_at interface](get_child_at.md)

---

## apysc basic data classes

### Table of contents

- [Why the apysc library does not use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)
- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)
- [Int and Number classes](int_and_number.md)
- [Int and Number classes common arithmetic operations](int_and_number_arithmetic_operations.md)
- [Int and Number classes common comparison operations](int_and_number_comparison_operations.md)
- [String class](string.md)
- [String class comparison operations](string_comparison_operations.md)
- [String class addition and multiplication operations](string_addition_and_multiplication.md)
- [Boolean class](boolean.md)
- [Array class](array.md)
- [Array class append and push interfaces](array_append_and_push.md)
- [Array class extend and concat interfaces](array_extend_and_concat.md)
- [Array class insert and insert_at interfaces](array_insert_and_insert_at.md)
- [Array class pop interface](array_pop.md)
- [Array class remove and remove_at interfaces](array_remove_and_remove_at.md)
- [Array class sort interface](array_sort.md)
- [Array class reverse interface](array_reverse.md)
- [Array class slice interface](array_slice.md)
- [Array class length interface](array_length.md)
- [Array class join interface](array_join.md)
- [Array class index_of interface](array_index_of.md)
- [Array class comparison interfaces](array_comparison.md)
- [Dictionary class](dictionary.md)
- [Dictionary class generic type settings](dictionary_generic.md)
- [Dictionary class get interface](dictionary_get.md)
- [Dictionary class length interface](dictionary_length.md)
- [Point2D class](point2d.md)

---

## DisplayObject and GraphicsBase classes

The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass and the base class of each graphics class, such as the `Rectangle` class.

### Table of contents

- [DisplayObject class](display_object.md)
- [DisplayObject and GraphicsBase classes basic properties abstract](display_object_and_graphics_base_prop_abstract.md)
- [DisplayObject class x and y interfaces](display_object_x_and_y.md)
- [DisplayObject class parent interfaces](display_object_parent.md)
- [DisplayObject class visible interface](display_object_visible.md)
- [DisplayObject class get_css and set_css interfaces](display_object_get_and_set_css.md)
- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)
- [GraphicsBase class rotation_around_center interface](graphics_base_rotation_around_center.md)
- [GraphicsBase class rotation_around_point interfaces](graphics_base_rotation_around_point.md)
- [GraphicsBase class scale_from_center interfaces](graphics_base_scale_from_center.md)
- [GraphicsBase class scale_from_point interfaces](graphics_base_scale_from_point.md)
- [GraphicsBase class flip_x and flip_y interfaces](graphics_base_flip_interfaces.md)
- [GraphicsBase class skew_x and skew_y interfaces](graphics_base_skew.md)

---

## Graphics class

### Table of contents

The `Graphics` class handles each vector graphics drawing.

- [Draw interfaces abstract](draw_interfaces_abstract.md)
- [Graphics class](graphics.md)
- [Graphics class begin_fill interface](graphics_begin_fill.md)
- [Graphics class line_style interface](graphics_line_style.md)
- [Graphics class draw_rect interface](graphics_draw_rect.md)
- [Graphics class draw_round_rect interface](graphics_draw_round_rect.md)
- [Graphics class draw_circle interface](graphics_draw_circle.md)
- [Graphics class draw_ellipse interface](graphics_draw_ellipse.md)
- [Graphics class move_to and line_to interfaces](graphics_move_to_and_line_to.md)
- [Graphics class draw_line interface](graphics_draw_line.md)
- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)
- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)
- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)
- [Graphics class draw_polygon interface](graphics_draw_polygon.md)
- [Graphics class fill_color interface](graphics_fill_color.md)
- [Graphics class fill_alpha interface](graphics_fill_alpha.md)
- [Graphics class line_color interface](graphics_line_color.md)
- [Graphics class line_alpha interface](graphics_line_alpha.md)
- [Graphics class line_thickness interface](graphics_line_thickness.md)
- [Graphics class line_dot_setting interface](graphics_line_dot_setting.md)
- [Graphics class line_dash_setting interface](graphics_line_dash_setting.md)
- [Graphics class line_round_dot_setting interface](graphics_line_round_dot_setting.md)
- [Graphics class line_dash_dot_setting interface](graphics_line_dash_dot_setting.md)

---

## Common event interfaces

### Table of contents

- [About the handler options type](about_handler_options_type.md)
- [Event class prevent_default and stop_propagation interfaces](event_prevent_default_and_stop_propagation.md)
- [bind_custom_event and trigger_custom_event interfaces](bind_and_trigger_custom_event.md)

---

## MouseEvent class and mouse event binding

### Table of contents

- [MouseEvent interfaces abstract](mouse_event_abstract.md)
- [Basic mouse event interfaces](mouse_event_basic.md)
- [click interface](click.md)
- [dblclick interface](dblclick.md)
- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [mousemove interface](mousemove.md)

---

## Branch instruction

### Table of contents

- [If class](if.md)
- [Elif class](elif.md)
- [Else class](else.md)
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
- [Return class](return.md)

---

## Loop

### Table of contents

- [For loop class](for.md)
- [Continue class](continue.md)

---

## Timer

### Table of contents

- [Timer class](timer.md)
- [TimerEvent class](timer_event.md)
- [Timer class delay setting](timer_delay.md)
- [FPS enum](fps.md)
- [Timer class repeat_count setting](timer_repeat_count.md)
- [Timer class start and stop interfaces](timer_start_and_stop.md)
- [Timer class timer_complete interface](timer_complete.md)
- [Timer class reset interface](timer_reset.md)

---

## Animation

### Table of contents

- [Animation interfaces abstract](animation_interfaces_abstract.md)
- [AnimationEvent class](animation_event.md)
- [Animation duration setting](animation_duration.md)
- [Animation delay setting](animation_delay.md)
- [Each animation interface return value](animation_return_value.md)
- [AnimationBase class start interface](animation_base_start.md)
- [AnimationBase class animation_complete interface](animation_complete.md)
- [AnimationBase class interfaces method chaining](animation_method_chaining.md)
- [AnimationBase class target property](animation_base_target.md)
- [Animation pause and play interfaces](animation_pause_and_play.md)
- [Animation reset interface](animation_reset.md)
- [Animation finish interface](animation_finish.md)
- [Animation reverse interface](animation_reverse.md)
- [animation_time interface](animation_time.md)
- [Easing enum](easing_enum.md)
- [Sequential animation setting](sequential_animation.md)
- [animation_parallel interface](animation_parallel.md)
- [animation_move interface](animation_move.md)
- [animation_x interface](animation_x.md)
- [animation_y interface](animation_y.md)
- [animation_width and animation_height interfaces](animation_width_and_height.md)
- [animation_fill_color interface](animation_fill_color.md)
- [animation_fill_alpha interface](animation_fill_alpha.md)
- [animation_line_color interface](animation_line_color.md)
- [animation_line_alpha interface](animation_line_alpha.md)
- [animation_line_thickness interface](animation_line_thickness.md)
- [animation_radius interface](animation_radius.md)
- [animation_rotation_around_center interface](animation_rotation_around_center.md)
- [animation_rotation_around_point interface](animation_rotation_around_point.md)
- [animation_scale_x_from_center and animation_scale_y_from_center interfaces](animation_scale_x_and_y_from_center.md)
- [animation_scale_x_from_point and animation_scale_y_from_point interfaces](animation_scale_x_and_y_from_point.md)
- [animation_skew_x interface](animation_skew_x.md)

---

## Debugging

### Table of contents

- [trace function interface](trace.md)
- [set_debug_mode interface](set_debug_mode.md)
- [unset_debug_mode interface](unset_debug_mode.md)

---

## Testing

### Table of contents

- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)
- [assert_equal and assert_not_equal interfaces](assert_equal_and_not_equal.md)
- [assert_true and assert_false interfaces](assert_true_and_false.md)
- [assert_arrays_equal and assert_arrays_not_equal interfaces](assert_arrays_equal_and_arrays_not_equal.md)
- [assert_dicts_equal and assert_dicts_not_equal interfaces](assert_dicts_equal_and_dicts_not_equal.md)
- [assert_defined and assert_undefined interfaces](assert_defined_and_undefined.md)