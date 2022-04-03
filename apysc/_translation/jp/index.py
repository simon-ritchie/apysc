"""This module is for the translation mapping data of the
following document:

Document file: index.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# apysc documentation':
    '',

    'Welcome to apysc documentation! apysc is the Python front-end library (currently developing and only works partially).':  # noqa
    '',

    '## Project links':
    '',

    '- [GitHub](https://github.com/simon-ritchie/apysc)':
    '',

    '  - Stargazers are very welcome!':
    '',

    '- [Twitter](https://twitter.com/apysc)':
    '',

    '  - The progress and updates are informed on Twitter. Please follow!':
    '',

    '- [PyPI](https://pypi.org/project/apysc/)':
    '',

    '## Contents':
    '',

    '**Quick start guide**':
    '',

    '- [What apysc can do in its current implementation](what_apysc_can_do.md)':  # noqa
    '',

    '- [Quick start guide](quick_start.md)':
    '',

    '- [Import conventions](import_conventions.md)':
    '',

    '---':
    '',

    '**Container classes**':
    '',

    'The `Stage` is the apysc overall drawing area container, and the `Sprite` is the container class.':  # noqa
    '',

    '- [Stage class](stage.md)':
    '',

    '- [Sprite class](sprite.md)':
    '',

    '---':
    '',

    '**Exporting**':
    '',

    'The HTML and JavaScript exporting interfaces.':
    '',

    '- [save overall html interface](save_overall_html.md)':
    '',

    '- [display on jupyter interface](display_on_jupyter.md)':
    '',

    '- [display on google colaboratory interface](display_on_colaboratory.md)':  # noqa
    '',

    '- [append js expression interface](append_js_expression.md)':
    '',

    '---':
    '',

    '**Child-related interfaces**':
    '',

    'The parent class, such as the `Sprite` or `Stage` have the following interfaces:':  # noqa
    '',

    '- [add child and remove child interfaces](add_child_and_remove_child.md)':  # noqa
    '',

    '- [contains interface](contains.md)':
    '- [contains インターフェイス](jp_contains.md)',

    '- [num children interface](num_children.md)':
    '',

    '- [get child at interface](get_child_at.md)':
    '',

    '---':
    '',

    '**apysc basic data classes**':
    '',

    '- [Why the apysc library does not use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)':  # noqa
    '',

    '- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)':  # noqa
    '- [基本的なデータクラスの共通の value インターフェイス](jp_fundamental_data_classes_value_interface.md)',  # noqa

    '- [Int and Number classes](int_and_number.md)':
    '',

    '- [Int and Number classes common arithmetic operations](int_and_number_arithmetic_operations.md)':  # noqa
    '',

    '- [Int and Number classes common comparison operations](int_and_number_comparison_operations.md)':  # noqa
    '',

    '- [String class](string.md)':
    '',

    '- [String class comparison operations](string_comparison_operations.md)':  # noqa
    '',

    '- [String class addition and multiplication operations](string_addition_and_multiplication.md)':  # noqa
    '',

    '- [Boolean class](boolean.md)':
    '',

    '- [Array class](array.md)':
    '',

    '- [Array class append and push interfaces](array_append_and_push.md)':
    '- [Array クラスの append と push のインターフェイス](jp_array_append_and_push.md)',

    '- [Array class extend and concat interfaces](array_extend_and_concat.md)':  # noqa
    '- [Array クラスの extend と concat のインターフェイス](jp_array_extend_and_concat.md)',  # noqa

    '- [Array class insert and insert at interfaces](array_insert_and_insert_at.md)':  # noqa
    '',

    '- [Array class pop interface](array_pop.md)':
    '- [Array クラスの pop インターフェイス](jp_array_pop.md)',

    '- [Array class remove and remove at interfaces](array_remove_and_remove_at.md)':  # noqa
    '',

    '- [Array class sort interface](array_sort.md)':
    '- [Array クラスの sort インターフェイス](jp_array_sort.md)',

    '- [Array class reverse interface](array_reverse.md)':
    '- [Array クラスの reverse インターフェイス](jp_array_reverse.md)',

    '- [Array class slice interface](array_slice.md)':
    '- [Array クラスの slice インターフェイス](jp_array_slice.md)',

    '- [Array class length interface](array_length.md)':
    '- [Array クラスの length (配列の長さ取得) のインターフェイス](jp_array_length.md)',

    '- [Array class join interface](array_join.md)':
    '- [Array クラスの join (値の連結文字列生成) のインターフェイス](jp_array_join.md)',

    '- [Array class index of interface](array_index_of.md)':
    '',

    '- [Array class comparison interfaces](array_comparison.md)':
    '- [Array クラスの比較の各インターフェイス](jp_array_comparison.md)',

    '- [Dictionary class](dictionary.md)':
    '',

    '- [Dictionary class generic type settings](dictionary_generic.md)':
    '',

    '- [Dictionary class get interface](dictionary_get.md)':
    '',

    '- [Dictionary class length interface](dictionary_length.md)':
    '',

    '- [Point2D class](point2d.md)':
    '',

    '---':
    '',

    '**DisplayObject and GraphicsBase classes**':
    '',

    'The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass and the base class of each graphics class, such as the `Rectangle` class.':  # noqa
    '',

    '- [DisplayObject class](display_object.md)':
    '- [DisplayObject クラス](jp_display_object.md)',

    '- [DisplayObject and GraphicsBase classes basic properties abstract](display_object_and_graphics_base_prop_abstract.md)':  # noqa
    '',

    '- [DisplayObject class x and y interfaces](display_object_x_and_y.md)':
    '- [DisplayObject クラスの x と y インターフェイス](jp_display_object_x_and_y.md)',

    '- [DisplayObject class parent interfaces](display_object_parent.md)':
    '- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)',  # noqa

    '- [DisplayObject class visible interface](display_object_visible.md)':
    '- [DisplayObject クラスの visible (表示・非表示) のインターフェイス](jp_display_object_visible.md)',  # noqa

    '- [DisplayObject class get css and set css interfaces](display_object_get_and_set_css.md)':  # noqa
    '',

    '- [DisplayObject class mouse event binding interfaces](display_object_mouse_event.md)':  # noqa
    '- [DisplayObject クラスのマウスイベント設定の各インターフェイス](jp_display_object_mouse_event.md)',  # noqa

    '- [GraphicsBase class rotation around center interface](graphics_base_rotation_around_center.md)':  # noqa
    '',

    '- [GraphicsBase class rotation around point interfaces](graphics_base_rotation_around_point.md)':  # noqa
    '',

    '- [GraphicsBase class scale from center interfaces](graphics_base_scale_from_center.md)':  # noqa
    '',

    '- [GraphicsBase class scale from point interfaces](graphics_base_scale_from_point.md)':  # noqa
    '',

    '- [GraphicsBase class flip x and flip y interfaces](graphics_base_flip_interfaces.md)':  # noqa
    '',

    '- [GraphicsBase class skew x and skew y interfaces](graphics_base_skew.md)':  # noqa
    '',

    '---':
    '',

    '**Graphics class**':
    '',

    'The `Graphics` class handles each vector graphics drawing.':
    '',

    '- [Draw interfaces abstract](draw_interfaces_abstract.md)':
    '',

    '- [Graphics class](graphics.md)':
    '- [Graphics クラス](jp_graphics.md)',

    '- [Graphics class begin fill interface](graphics_begin_fill.md)':
    '',

    '- [Graphics class line style interface](graphics_line_style.md)':
    '',

    '- [Graphics class draw rect interface](graphics_draw_rect.md)':
    '',

    '- [Graphics class draw round rect interface](graphics_draw_round_rect.md)':  # noqa
    '',

    '- [Graphics class draw circle interface](graphics_draw_circle.md)':
    '',

    '- [Graphics class draw ellipse interface](graphics_draw_ellipse.md)':
    '',

    '- [Graphics class move to and line to interfaces](graphics_move_to_and_line_to.md)':  # noqa
    '',

    '- [Graphics class draw line interface](graphics_draw_line.md)':
    '',

    '- [Graphics class draw dotted line interface](graphics_draw_dotted_line.md)':  # noqa
    '',

    '- [Graphics class draw dashed line interface](graphics_draw_dashed_line.md)':  # noqa
    '',

    '- [Graphics class draw round dotted line interface](graphics_draw_round_dotted_line.md)':  # noqa
    '',

    '- [Graphics class draw dash dotted line interface](graphics_draw_dash_dotted_line.md)':  # noqa
    '',

    '- [Graphics class draw polygon interface](graphics_draw_polygon.md)':
    '',

    '- [Graphics class fill color interface](graphics_fill_color.md)':
    '',

    '- [Graphics class fill alpha interface](graphics_fill_alpha.md)':
    '',

    '- [Graphics class line color interface](graphics_line_color.md)':
    '',

    '- [Graphics class line alpha interface](graphics_line_alpha.md)':
    '',

    '- [Graphics class line thickness interface](graphics_line_thickness.md)':  # noqa
    '',

    '- [Graphics class line dot setting interface](graphics_line_dot_setting.md)':  # noqa
    '',

    '- [Graphics class line dash setting interface](graphics_line_dash_setting.md)':  # noqa
    '',

    '- [Graphics class line round dot setting interface](graphics_line_round_dot_setting.md)':  # noqa
    '',

    '- [Graphics class line dash dot setting interface](graphics_line_dash_dot_setting.md)':  # noqa
    '',

    '---':
    '',

    '**Common event interfaces**':
    '',

    '- [About the handler options type](about_handler_options_type.md)':
    '',

    '- [Event class prevent default and stop propagation interfaces](event_prevent_default_and_stop_propagation.md)':  # noqa
    '',

    '- [bind custom event and trigger custom event interfaces](bind_and_trigger_custom_event.md)':  # noqa
    '',

    '---':
    '',

    '**MouseEvent class and mouse event binding**':
    '',

    '- [MouseEvent interfaces abstract](mouse_event_abstract.md)':
    '',

    '- [Basic mouse event interfaces](mouse_event_basic.md)':
    '- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)',

    '- [click interface](click.md)':
    '- [クリックインターフェイス](jp_click.md)',

    '- [dblclick interface](dblclick.md)':
    '',

    '- [mousedown and mouseup interfaces](mousedown_and_mouseup.md)':
    '- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)',

    '- [mouseover and mouseout interfaces](mouseover_and_mouseout.md)':
    '- [mouseover と mouseout インターフェイス](jp_mouseover_and_mouseout.md)',

    '- [mousemove interface](mousemove.md)':
    '- [mousemove インターフェイス](jp_mousemove.md)',

    '---':
    '',

    '**Branch instruction**':
    '',

    '- [If class](if.md)':
    '- [If クラス](jp_if.md)',

    '- [Elif class](elif.md)':
    '- [Elif クラス](jp_elif.md)',

    '- [Else class](else.md)':
    '- [Else クラス](jp_else.md)',

    '- [Each branch instruction class scope variables reverting setting](branch_instruction_variables_reverting_setting.md)':  # noqa
    '',

    '- [Return class](return.md)':
    '',

    '---':
    '',

    '**Loop**':
    '',

    '- [For loop class](for.md)':
    '',

    '- [Continue class](continue.md)':
    '',

    '---':
    '',

    '**Timer**':
    '',

    '- [Timer class](timer.md)':
    '',

    '- [TimerEvent class](timer_event.md)':
    '',

    '- [Timer class delay setting](timer_delay.md)':
    '- [Timer クラスの delay 設定](jp_timer_delay.md)',

    '- [FPS enum](fps.md)':
    '',

    '- [Timer class repeat count setting](timer_repeat_count.md)':
    '',

    '- [Timer class start and stop interfaces](timer_start_and_stop.md)':
    '',

    '- [Timer class timer complete interface](timer_complete.md)':
    '',

    '- [Timer class reset interface](timer_reset.md)':
    '',

    '---':
    '',

    '**Animation**':
    '',

    '- [Animation interfaces abstract](animation_interfaces_abstract.md)':
    '',

    '- [AnimationEvent class](animation_event.md)':
    '',

    '- [Animation duration setting](animation_duration.md)':
    '',

    '- [Animation delay setting](animation_delay.md)':
    '',

    '- [Each animation interface return value](animation_return_value.md)':
    '',

    '- [AnimationBase class start interface](animation_base_start.md)':
    '',

    '- [AnimationBase class animation complete interface](animation_complete.md)':  # noqa
    '',

    '- [AnimationBase class interfaces method chaining](animation_method_chaining.md)':  # noqa
    '',

    '- [AnimationBase class target property](animation_base_target.md)':
    '',

    '- [Animation pause and play interfaces](animation_pause_and_play.md)':
    '',

    '- [Animation reset interface](animation_reset.md)':
    '',

    '- [Animation finish interface](animation_finish.md)':
    '',

    '- [Animation reverse interface](animation_reverse.md)':
    '',

    '- [animation time interface](animation_time.md)':
    '',

    '- [Easing enum](easing_enum.md)':
    '',

    '- [Sequential animation setting](sequential_animation.md)':
    '',

    '- [animation parallel interface](animation_parallel.md)':
    '',

    '- [animation move interface](animation_move.md)':
    '',

    '- [animation x interface](animation_x.md)':
    '',

    '- [animation y interface](animation_y.md)':
    '',

    '- [animation width and animation height interfaces](animation_width_and_height.md)':  # noqa
    '',

    '- [animation fill color interface](animation_fill_color.md)':
    '',

    '- [animation fill alpha interface](animation_fill_alpha.md)':
    '',

    '- [animation line color interface](animation_line_color.md)':
    '',

    '- [animation line alpha interface](animation_line_alpha.md)':
    '',

    '- [animation line thickness interface](animation_line_thickness.md)':
    '',

    '- [animation radius interface](animation_radius.md)':
    '',

    '- [animation rotation around center interface](animation_rotation_around_center.md)':  # noqa
    '',

    '- [animation rotation around point interface](animation_rotation_around_point.md)':  # noqa
    '',

    '- [animation scale x from center and animation scale y from center interfaces](animation_scale_x_and_y_from_center.md)':  # noqa
    '',

    '- [animation scale x from point and animation scale y from point interfaces](animation_scale_x_and_y_from_point.md)':  # noqa
    '',

    '- [animation skew x interface](animation_skew_x.md)':
    '',

    '---':
    '',

    '**Debugging**':
    '',

    '- [trace function interface](trace.md)':
    '',

    '- [set debug mode interface](set_debug_mode.md)':
    '',

    '- [unset debug mode interface](unset_debug_mode.md)':
    '',

    '---':
    '',

    '**Testing**':
    '',

    '- [JavaScript assertion interface basic behavior](assertion_basic_behavior.md)':  # noqa
    '- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)',  # noqa

    '- [assert equal and assert not equal interfaces](assert_equal_and_not_equal.md)':  # noqa
    '',

    '- [assert true and assert false interfaces](assert_true_and_false.md)':
    '',

    '- [assert arrays equal and assert arrays not equal interfaces](assert_arrays_equal_and_arrays_not_equal.md)':  # noqa
    '',

    '- [assert dicts equal and assert dicts not equal interfaces](assert_dicts_equal_and_dicts_not_equal.md)':  # noqa
    '',

    '- [assert defined and assert undefined interfaces](assert_defined_and_undefined.md)':  # noqa
    '',

    '---':
    '',

}
