# apysc documentation

Welcome to apysc documentation! apysc is the Python front-end library (currently developing and only works partially).

## Project links

- [GitHub](https://github.com/simon-ritchie/apysc)
  - Stargazers are very welcome!
- [Twitter](https://twitter.com/apysc)
  - The progress and updates are informed on Twitter. Please follow!
- [PyPI](https://pypi.org/project/apysc/)

## Contents

**Quick start guide**

- [What apysc can do in its current implementation](what_apysc_can_do.md)
- [Quick start guide](quick_start.md)
- [Import conventions](import_conventions.md)

---

**Stage class**

The `Stage` is the apysc overall drawing area.

- [Stage class](stage.md)

---

**Exporting**

The HTML and JavaScript exporting interfaces.

- [Save overall html interface](save_overall_html.md)
- [Display on the jupyter interface](display_on_jupyter.md)
- [Display on the Google Colaboratory interface](display_on_colaboratory.md)
- [Append js expression interface](append_js_expression.md)

---

**apysc basic data classes**

- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)
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
- [Array class insert and insert at interfaces](array_insert_and_insert_at.md)
- [Array class pop interface](array_pop.md)
- [Array class remove and remove at interfaces](array_remove_and_remove_at.md)
- [Array class sort interface](array_sort.md)
- [Array class reverse interface](array_reverse.md)
- [Array class slice interface](array_slice.md)
- [Array class length interface](array_length.md)
- [Array class join interface](array_join.md)
- [Array class index of interface](array_index_of.md)
- [Array class comparison interfaces](array_comparison.md)
- [Dictionary class](dictionary.md)
- [Dictionary class generic type settings](dictionary_generic.md)
- [Dictionary class get interface](dictionary_get.md)
- [Dictionary class length interface](dictionary_length.md)
- [Point2D class](point2d.md)

---

**DisplayObject and GraphicsBase classes**

The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass and the base class of each graphics class, such as the `Rectangle`\.

- [DisplayObject class](display_object.md)
- [DisplayObject and GraphicsBase classes basic properties abstract](display_object_and_graphics_base_prop_abstract.md)
- [DisplayObject class x and y interfaces](display_object_x_and_y.md)
- [DisplayObject class parent interfaces](display_object_parent.md)
- [DisplayObject class visible interface](display_object_visible.md)
- [DisplayObject class get and set css interfaces](display_object_get_and_set_css.md)
- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)
- [GraphicsBase class rotation around center interface](graphics_base_rotation_around_center.md)
- [GraphicsBase class rotation around point interfaces](graphics_base_rotation_around_point.md)
- [GraphicsBase class scale from center interfaces](graphics_base_scale_from_center.md)
- [GraphicsBase class scale from point interfaces](graphics_base_scale_from_point.md)
- [GraphicsBase class flip x and flip y interfaces](graphics_base_flip_interfaces.md)
- [GraphicsBase class skew x and skew y interfaces](graphics_base_skew.md)

---

**Sprite class**

The `Sprite` is the container of each display object instance.

- [Sprite class](sprite.md)
- [Sprite class add child and remove child interfaces](sprite_add_child_and_remove_child.md)
- [Sprite class contains interface](sprite_contains.md)
- [Sprite class num children interface](sprite_num_children.md)
- [Sprite class get child at interface](sprite_get_child_at.md)

---

**Graphics class**

The `Graphics` class handles each vector graphics drawing.

- [Draw interfaces abstract](draw_interfaces_abstract.md)
- [Graphics class](graphics.md)
- [Graphics class begin fill interface](graphics_begin_fill.md)
- [Graphics class line style interface](graphics_line_style.md)
- [Graphics class draw rect interface](graphics_draw_rect.md)
- [Graphics class draw round rect interface](graphics_draw_round_rect.md)
- [Graphics class draw circle interface](graphics_draw_circle.md)
- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)
- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)
- [Graphics class draw line interface](graphics_draw_line.md)
- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)
- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)
- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)
- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)
- [Graphics class draw polygon interface](graphics_draw_polygon.md)
- [Graphics class fill color interface](graphics_fill_color.md)
- [Graphics class fill alpha interface](graphics_fill_alpha.md)
- [Graphics class line color interface](graphics_line_color.md)
- [Graphics class line alpha interface](graphics_line_alpha.md)
- [Graphics class line thickness interface](graphics_line_thickness.md)
- [Graphics class line dot setting interface](graphics_line_dot_setting.md)
- [Graphics class line dash setting interface](graphics_line_dash_setting.md)
- [Graphics class line round dot setting interface](graphics_line_round_dot_setting.md)
- [Graphics class line dash dot setting interface](graphics_line_dash_dot_setting.md)

---

**Common event interfaces**

- [About the handler options type](about_handler_options_type.md)
- [Event class prevent default and stop propagation interfaces](event_prevent_default_and_stop_propagation.md)
- [Bind and trigger custom event interfaces](bind_and_trigger_custom_event.md)

---

**MouseEvent class and mouse event binding**

- [MouseEvent interfaces abstract](mouse_event_abstract.md)
- [Basic mouse event interfaces](mouse_event_basic.md)
- [Click interface](click.md)
- [Double click interface](dblclick.md)
- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [Mousemove interface](mousemove.md)

---

**Branch instruction**

- [If class](if.md)
- [Elif class](elif.md)
- [Else class](else.md)
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)
- [Return class](return.md)

---

**Loop**

- [For loop class](for.md)
- [Continue class](continue.md)

---

**Timer**

- [Timer class](timer.md)
- [TimerEvent class](timer_event.md)
- [Timer class delay setting](timer_delay.md)
- [FPS enum](fps.md)
- [Timer class repeat count setting](timer_repeat_count.md)
- [Timer class start and stop interfaces](timer_start_and_stop.md)
- [Timer class timer complete interface](timer_complete.md)
- [Timer class reset interface](timer_reset.md)

---

**Animation**

- [Animation interfaces abstract](animation_interfaces_abstract.md)
- [AnimationEvent class](animation_event.md)
- [Animation duration setting](animation_duration.md)
- [Animation delay setting](animation_delay.md)
- [Each animation interface return value](animation_return_value.md)
- [AnimationBase class start interface](animation_base_start.md)
- [AnimationBase class animation complete interface](animation_complete.md)
- [AnimationBase class interfaces method chaining](animation_method_chaining.md)
- [AnimationBase class target property](animation_base_target.md)
- [Animation pause and play interfaces](animation_pause_and_play.md)
- [Animation reset interface](animation_reset.md)
- [Animation finish interface](animation_finish.md)
- [Animation reverse interface](animation_reverse.md)
- [Animation time interface](animation_time.md)
- [Easing enum](easing_enum.md)
- [Sequential animation setting](sequential_animation.md)
- [Animation parallel interface](animation_parallel.md)
- [Animation move interface](animation_move.md)
- [Animation x interface](animation_x.md)
- [Animation y interface](animation_y.md)
- [Animation width and height interfaces](animation_width_and_height.md)
- [Animation fill color interface](animation_fill_color.md)
- [Animation fill alpha interface](animation_fill_alpha.md)
- [Animation line color interface](animation_line_color.md)
- [Animation line alpha interface](animation_line_alpha.md)
- [Animation line thickness interface](animation_line_thickness.md)
- [Animation radius interface](animation_radius.md)
- [Animation rotation around center interface](animation_rotation_around_center.md)
- [Animation rotation around point interface](animation_rotation_around_point.md)
- [Animation scale x and y from center interfaces](animation_scale_x_and_y_from_center.md)
- [Animation scale x and y from point interfaces](animation_scale_x_and_y_from_point.md)
- [Animation skew x interface](animation_skew_x.md)

---

**Debugging**

- [Trace function interface](trace.md)
- [Set debug mode interface](set_debug_mode.md)
- [Unset debug mode interface](unset_debug_mode.md)
- [DebugInfo class](debug_info.md)

---

**Testing**

- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)
- [Assert equal and assert not equal interfaces](assert_equal_and_not_equal.md)
- [Assert true and assert false interfaces](assert_true_and_false.md)
- [Assert arrays equal and arrays not equal interfaces](assert_arrays_equal_and_arrays_not_equal.md)
- [Assert dicts equal and dicts not equal interfaces](assert_dicts_equal_and_dicts_not_equal.md)
- [Assert defined and undefined interfaces](assert_defined_and_undefined.md)

---
