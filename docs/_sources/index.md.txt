# apysc documentation

Welcome to apysc documentation! apysc is the Python front-end library (currently developing and only works partially).

## Project links

- [GitHub](https://github.com/simon-ritchie/apysc)
  - Clicks on the GitHub star are very welcome! It empowers developer motivation.
- [Twitter](https://twitter.com/apysc)
  - The progress and updates will be informed on Twitter. Please follow!
- [PyPI](https://pypi.org/project/apysc/)

## Contents

**Quick start guide**

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

---

**apysc basic data classes**

- [Why not using the Python built-in data type in the apysc library?](why_not_using_python_builtin_data_type.md)
- [apysc basic data classes common value interface](basic_data_classes_value_interface.md)
- [Int and Number classes](int_and_number.md)
- [Int and Number classes common arithmetic operations](int_and_number_arithmetic_operations.md)
- [Int and Number classes common comparison operations](int_and_number_comparison_operations.md)
- [String class](string.md)
- [String class comparison operations](string_comparison_operations.md)
- [String class addition and multiplication operations](string_addition_and_multiplication.md)
- [Boolean class](boolean.md)

---

**DisplayObject and GraphicsBase classes**

The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass, and the base class of each graphics class, such as the `Rectangle`.

- [DisplayObject class](display_object.md)
- [DisplayObject class x and y interfaces](display_object_x_and_y.md)
- [DisplayObject class parent interfaces](display_object_parent.md)
- [DisplayObject class visible interface](display_object_visible.md)
- [DisplayObject class get and set css interfaces](display_object_get_and_set_css.md)
- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)
- [GraphicsBase class rotate around center interface](graphics_base_rotate_around_center.md)
- [GraphicsBase class rotate around point interface](graphics_base_rotate_around_point.md)

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

---

**Common event interfaces**

- [Bind and trigger custom event interfaces](bind_and_trigger_custom_event.md)

---

**MouseEvent class and mouse event binding**

- [Common mouse event interfaces](mouse_event_common.md)
- [Click interface](click.md)
- [Mousedown and mouseup interfaces](mousedown_and_mouseup.md)
- [Mouseover and mouseout interfaces](mouseover_and_mouseout.md)
- [Mousemove interface](mousemove.md)

---

**Branch instruction**

- [If class](if.md)
- [Elif class](elif.md)
- [Else class](else.md)
- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)

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
