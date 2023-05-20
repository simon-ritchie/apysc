<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/index.html)の確認をお願いします。</span>

# apysc ドキュメント

apyscのドキュメントページへようこそ。apyscはPythonのフロントエンド用のライブラリです（現在開発中であり部分的にのみ動作します）。

## プロジェクトの関連リンク

- [GitHub](https://github.com/simon-ritchie/apysc)
  - もしもapyscライブラリを気にいったり、もしくはライブラリの将来に期待が出来そうと感じられたらリポジトリにスターを付けていただけますと幸いです。

- [PyPI](https://pypi.org/project/apysc/)

他の言語のドキュメント: | [英語 (English)](https://simon-ritchie.github.io/apysc/en/index.html) | 日本語 |

## クイックスタートガイド

```{toctree}
:maxdepth: 1
jp_what_apysc_can_do
jp_quick_start
jp_import_conventions
jp_recommended_type_checker_settings
```

## コンテナーの各クラス

`Stage`はapyscの描画領域全体のコンテナーとなり、`Sprite`は通常の各インスタンスのコンテナーのクラスとなります。

```{toctree}
:maxdepth: 1
jp_stage
jp_sprite
```

## 出力処理

以下はHTMLとJavaScriptの出力処理関係の各インターフェイスです。

```{toctree}
:maxdepth: 1
jp_save_overall_html
jp_display_on_jupyter
jp_display_on_colaboratory
jp_append_js_expression
```

## 子要素関係の各インターフェイス

`Sprite`や`Stage`などの親となれる各クラスは以下のインターフェイスを持っています:

```{toctree}
:maxdepth: 1
jp_add_child_and_remove_child
jp_remove_children
jp_contains
jp_num_children
jp_get_child_at
```

## apyscの基本的な各データクラス

```{toctree}
:maxdepth: 1
jp_why_apysc_doesnt_use_python_builtin_data_type
jp_fundamental_data_classes_value_interface
jp_to_string
```

### Int と Number クラス

```{toctree}
:maxdepth: 1
jp_int_and_number
jp_int_and_number_arithmetic_operations
jp_int_and_number_comparison_operations
```

### String クラス

```{toctree}
:maxdepth: 1
jp_string
jp_string_comparison_operations
jp_string_addition_and_multiplication
jp_string_split
```

### Boolean クラス

```{toctree}
:maxdepth: 1
jp_boolean
```

### Array クラス

```{toctree}
:maxdepth: 1
jp_array
jp_array_append_and_push
jp_array_extend_and_concat
jp_array_insert_and_insert_at
jp_array_pop
jp_array_remove_and_remove_at
jp_array_sort
jp_array_reverse
jp_array_slice
jp_array_length
jp_array_join
jp_array_index_of
jp_array_clear
jp_array_comparison
```

### Dictionary クラス

```{toctree}
:maxdepth: 1
jp_dictionary
jp_dictionary_generic
jp_dictionary_get
jp_dictionary_length
```

## DisplayObject と GraphicsBase の各クラス

`DisplayObject`クラスは各表示用のオブジェクトの基底クラスです。`GraphicsBase`クラスは`DisplayObject`のサブクラスであり、且つ`Rectangle`などの各グラフィックスの基底クラスとなります。

```{toctree}
:maxdepth: 1
jp_display_object
jp_display_object_and_graphics_base_prop_abstract
jp_display_object_x_and_y
jp_display_object_parent
jp_display_object_visible
jp_display_object_get_and_set_css
jp_display_object_mouse_event
jp_graphics_base_fill_color
jp_graphics_base_fill_alpha
jp_graphics_base_line_color
jp_graphics_base_line_alpha
jp_graphics_base_line_thickness
jp_graphics_base_line_dot_setting
jp_graphics_base_line_dash_setting
jp_graphics_base_line_round_dot_setting
jp_graphics_base_line_dash_dot_setting
jp_graphics_base_rotation_around_center
jp_graphics_base_rotation_around_point
jp_graphics_base_scale_from_center
jp_graphics_base_scale_from_point
jp_graphics_base_flip_interfaces
jp_graphics_base_skew
```

## 各グラフィックのクラス

```{toctree}
:maxdepth: 1
jp_triangle
jp_rectangle
jp_circle
jp_ellipse
jp_line
jp_polyline
jp_polygon
jp_path
```

## Graphics クラス

<br><iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>

`Graphics`クラスは各ベクターグラフィックスの描画処理を扱います。

```{toctree}
:maxdepth: 1
jp_draw_interfaces_abstract
jp_graphics
jp_graphics_begin_fill
jp_graphics_line_style
jp_graphics_draw_triangle
jp_graphics_draw_rect
jp_graphics_draw_round_rect
jp_graphics_draw_circle
jp_graphics_draw_ellipse
jp_graphics_move_to_and_line_to
jp_graphics_draw_line
jp_graphics_draw_dotted_line
jp_graphics_draw_dashed_line
jp_graphics_draw_round_dotted_line
jp_graphics_draw_dash_dotted_line
jp_graphics_draw_polygon
jp_graphics_draw_path
jp_graphics_clear
```

## SVG テキスト

```{toctree}
:maxdepth: 1
jp_svg_text
jp_svg_text_span
```

## 座標・サイズ等のデータの各クラス

```{toctree}
:maxdepth: 1
jp_point2d
jp_path_move_to
jp_path_line_to
jp_path_horizontal
jp_path_vertical
jp_path_close
jp_path_bezier_2d
jp_path_bezier_2d_continual
jp_path_bezier_3d
jp_path_bezier_3d_continual
jp_rectangle_geom
jp_get_bounds
```

## イベントの共通の各インターフェイス

```{toctree}
:maxdepth: 1
jp_about_handler_options_type
jp_event_prevent_default_and_stop_propagation
jp_bind_and_trigger_custom_event
```

## MouseEvent クラスとマウスイベントの設定

<br><iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

```{toctree}
:maxdepth: 1
jp_mouse_event_abstract
jp_mouse_event_basic
jp_click
jp_dblclick
jp_mousedown_and_mouseup
jp_mouseover_and_mouseout
jp_mousemove
```

## 条件分岐の制御

```{toctree}
:maxdepth: 1
jp_if
jp_elif
jp_else
jp_branch_instruction_variables_reverting_setting
jp_return
```

## ループ

```{toctree}
:maxdepth: 1
jp_for
jp_continue
jp_range
```

## タイマーとenter frame

<br><iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>

```{toctree}
:maxdepth: 1
jp_timer
jp_timer_event
jp_timer_delay
jp_fps
jp_timer_repeat_count
jp_timer_start_and_stop
jp_timer_complete
jp_timer_reset
jp_enter_frame
jp_unbind_enter_frame_and_unbind_enter_frame_all
```

## DateTime クラス

```{toctree}
:maxdepth: 1
jp_datetime
jp_datetime_year
jp_datetime_month
jp_datetime_day
jp_datetime_hour
jp_datetime_minute
jp_datetime_second
jp_datetime_millisecond
jp_datetime_weekday_js_and_weekday_py
jp_datetime_now
jp_datetime_set_month_end
```

## TimeDelta クラス

```{toctree}
:maxdepth: 1
jp_timedelta
jp_timedelta_days
jp_timedelta_total_seconds
```

## アニメーション

<br><iframe src="static/animation_interfaces_abstract_rotation_around_center/index.html" width="150" height="150"></iframe>

```{toctree}
:maxdepth: 1
jp_animation_interfaces_abstract
jp_animation_event
jp_animation_duration
jp_animation_delay
jp_animation_return_value
jp_animation_base_start
jp_animation_complete
jp_animation_method_chaining
jp_animation_base_target
jp_animation_pause_and_play
jp_animation_reset
jp_animation_finish
jp_animation_reverse
jp_animation_time
jp_easing_enum
jp_sequential_animation
jp_animation_parallel
jp_animation_move
jp_animation_x
jp_animation_y
jp_animation_width_and_height
jp_animation_fill_color
jp_animation_fill_alpha
jp_animation_line_color
jp_animation_line_alpha
jp_animation_line_thickness
jp_animation_radius
jp_animation_rotation_around_center
jp_animation_rotation_around_point
jp_animation_scale_x_and_y_from_center
jp_animation_scale_x_and_y_from_point
```

## 数学

```{toctree}
:maxdepth: 1
jp_math_min
jp_math_max
jp_math_trunc
```

## その他の操作関係の各インターフェイス

```{toctree}
:maxdepth: 1
jp_delete
```

## デバッグ

```{toctree}
:maxdepth: 1
jp_trace
jp_set_debug_mode
jp_unset_debug_mode
jp_add_debug_info_setting
jp_variable_name_suffix
```

## テスト

```{toctree}
:maxdepth: 1
jp_assertion_basic_behavior
jp_assert_equal_and_not_equal
jp_assert_true_and_false
jp_assert_greater_and_greater_equal
jp_assert_less_and_less_equal
jp_assert_arrays_equal_and_arrays_not_equal
jp_assert_dicts_equal_and_dicts_not_equal
jp_assert_defined_and_undefined
```