<span class="inconspicuous-txt">※この翻訳ドキュメントはスクリプトによって出力・同期されています。内容が怪しそうな場合は<a href="https://github.com/simon-ritchie/apysc/issues" target="_blank">GitHubにissue</a>を追加したり[英語の原文](https://simon-ritchie.github.io/apysc/en/index.html)の確認をお願いします。</span>

# apysc ドキュメント

apyscのドキュメントページへようこそ。apyscはPythonのフロントエンド用のライブラリです（現在開発中であり部分的にのみ動作します）。

## プロジェクトの関連リンク

- [GitHub](https://github.com/simon-ritchie/apysc)
  - もしもapyscライブラリを気にいったり、もしくはライブラリの将来に期待が出来そうと感じられたらリポジトリにスターを付けていただけますと幸いです。

- [PyPI](https://pypi.org/project/apysc/)

他の言語のドキュメント: | [英語 (English)](https://simon-ritchie.github.io/apysc/en/index.html) | 日本語 |

## クイックスタートガイド

### Table of contents

- [apyscが現在の実装で出来ることの概要](jp_what_apysc_can_do.md)
- [クイックスタートガイド](jp_quick_start.md)

- [import の慣習](jp_import_conventions.md)
- [推奨される型アノテーションのチェック設定](jp_recommended_type_checker_settings.md)

---

## コンテナーの各クラス

`Stage`はapyscの描画領域全体のコンテナーとなり、`Sprite`は通常の各インスタンスのコンテナーのクラスとなります。

### Table of contents

- [Stage クラス](jp_stage.md)
- [Sprite クラス](jp_sprite.md)

---

## 出力処理

以下はHTMLとJavaScriptの出力処理関係の各インターフェイスです。

### Table of contents

- [save_overall_html インターフェイス](jp_save_overall_html.md)
- [display_on_jupyter インターフェイス](jp_display_on_jupyter.md)

- [display_on_colaboratory インターフェイス](jp_display_on_colaboratory.md)
- [append_js_expression インターフェイス](jp_append_js_expression.md)

---

## 子要素関係の各インターフェイス

`Sprite`や`Stage`などの親となれる各クラスは以下のインターフェイスを持っています:

### Table of contents

- [add_child （子の追加）と remove_child （子の削除）のインターフェイス](jp_add_child_and_remove_child.md)
- [contains インターフェイス](jp_contains.md)

- [num_children （子の件数属性）のインターフェイス](jp_num_children.md)
- [get_child_at （特定位置の子の取得処理）のインターフェイス](jp_get_child_at.md)

---

## apyscの基本的な各データクラス

### Table of contents

- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)
- [基本的なデータクラスの共通の value インターフェイス](jp_fundamental_data_classes_value_interface.md)

- [Int と Number の各クラス](jp_int_and_number.md)
- [Int と Number クラスの共通の計算制御](jp_int_and_number_arithmetic_operations.md)

- [Int と Number クラスの共通の比較制御](jp_int_and_number_comparison_operations.md)
- [String クラス](jp_string.md)

- [String クラスの比較制御](jp_string_comparison_operations.md)
- [String クラスの加算と乗算の制御](jp_string_addition_and_multiplication.md)

- [Boolean クラス](jp_boolean.md)
- [Array クラス](jp_array.md)

- [Array クラスの append と push のインターフェイス](jp_array_append_and_push.md)
- [Array クラスの extend と concat のインターフェイス](jp_array_extend_and_concat.md)

- [Array クラスの insert と insert_at のインターフェイス](jp_array_insert_and_insert_at.md)
- [Array クラスの pop インターフェイス](jp_array_pop.md)

- [Array クラスの remove と remove_at のインターフェイス](jp_array_remove_and_remove_at.md)
- [Array クラスの sort インターフェイス](jp_array_sort.md)

- [Array クラスの reverse インターフェイス](jp_array_reverse.md)
- [Array クラスの slice インターフェイス](jp_array_slice.md)

- [Array クラスの length (配列の長さ取得) のインターフェイス](jp_array_length.md)
- [Array クラスの join (値の連結文字列生成) のインターフェイス](jp_array_join.md)

- [Array クラスの index_of (値のインデックス取得) のインターフェイス](jp_array_index_of.md)
- [Array クラスの clear インターフェイス](jp_array_clear.md)

- [Array クラスの比較の各インターフェイス](jp_array_comparison.md)
- [Dictionary クラス](jp_dictionary.md)

- [Dictionary クラスのジェネリックの型設定](jp_dictionary_generic.md)
- [Dictionary クラスの get インターフェイス](jp_dictionary_get.md)

- [Dictionary クラスの length インターフェイス](jp_dictionary_length.md)
- [Point2D クラス](jp_point2d.md)

---

## DisplayObject と GraphicsBase の各クラス

`DisplayObject`クラスは各表示用のオブジェクトの基底クラスです。`GraphicsBase`クラスは`DisplayObject`のサブクラスであり、且つ`Rectangle`などの各グラフィックスの基底クラスとなります。

### Table of contents

- [DisplayObject クラス](jp_display_object.md)
- [DisplayObject と GraphicsBase の各クラスの基本的な各属性の概要](jp_display_object_and_graphics_base_prop_abstract.md)

- [DisplayObject クラスの x と y インターフェイス](jp_display_object_x_and_y.md)
- [DisplayObjectクラス parent （親要素属性）のインターフェイス](jp_display_object_parent.md)

- [DisplayObject クラスの visible (表示・非表示) のインターフェイス](jp_display_object_visible.md)
- [DisplayObject クラスの get_css と set_css の各インターフェイス](jp_display_object_get_and_set_css.md)

- [DisplayObject クラスのマウスイベント設定の各インターフェイス](jp_display_object_mouse_event.md)
- [GraphicsBase クラスの rotation_around_center (中央座標基準の回転) インターフェイス](jp_graphics_base_rotation_around_center.md)

- [GraphicsBase クラスの rotation_around_point (指定座標基準の回転) の各インターフェイス](jp_graphics_base_rotation_around_point.md)
- [GraphicsBase クラスの scale_from_center (中央座標基準の拡縮) の各インターフェイス](jp_graphics_base_scale_from_center.md)

- [GraphicsBase クラスの scale_from_point (指定座標基準の拡縮) の各インターフェイス](jp_graphics_base_scale_from_point.md)
- [GraphicsBase クラスの flip_x (横軸の反転) と flip_y (縦軸の反転) のインターフェイス](jp_graphics_base_flip_interfaces.md)

- [GraphicsBase クラスの skew_x (X軸の歪み) と skew_y (Y軸の歪み) のインターフェイス](jp_graphics_base_skew.md)

---

## Graphics クラス

<br><iframe src="static/what_apysc_can_do_draw_vector_graphics/index.html" width="650" height="210"></iframe>

### Table of contents

`Graphics`クラスは各ベクターグラフィックスの描画処理を扱います。

- [描画の各インターフェイスの概要](jp_draw_interfaces_abstract.md)
- [Graphics クラス](jp_graphics.md)

- [Graphics クラスの begin_fill (塗りの設定)のインターフェイス](jp_graphics_begin_fill.md)
- [Graphics クラスの line_style (線のスタイル設定)のインターフェイス](jp_graphics_line_style.md)

- [Graphics クラスの draw_rect (四角の描画)のインターフェイス](jp_graphics_draw_rect.md)
- [Graphics クラスの draw_round_rect (角丸の四角の描画)のインターフェイス](jp_graphics_draw_round_rect.md)

- [Graphics クラスの draw_circle (円の描画)のインターフェイス](jp_graphics_draw_circle.md)
- [Graphics クラスの draw_ellipse (楕円描画) のインターフェイス](jp_graphics_draw_ellipse.md)

- [Graphics クラスの move_to (線の描画位置の変更)と line_to (指定座標への線の描画)のインターフェイス](jp_graphics_move_to_and_line_to.md)
- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)

- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)
- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)

- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)
- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)

- [Graphics クラスの draw_polygon (多角形描画)のインターフェイス](jp_graphics_draw_polygon.md)
- [Graphics クラスの fill_color (塗り設定)のインターフェイス](jp_graphics_fill_color.md)

- [Graphics クラスの fill_alpha (塗りの透明度設定)のインターフェイス](jp_graphics_fill_alpha.md)
- [Graphics クラスの line_color (線の色設定)のインターフェイス](jp_graphics_line_color.md)

- [Graphics クラスの line_color (線の透明度設定)のインターフェイス](jp_graphics_line_alpha.md)
- [Graphics クラスの line_color (線幅設定)のインターフェイス](jp_graphics_line_thickness.md)

- [Graphics クラスの line_dot_setting (点線設定)のインターフェイス](jp_graphics_line_dot_setting.md)
- [Graphics クラスの line_dash_setting (破線設定)のインターフェイス](jp_graphics_line_dash_setting.md)

- [Graphics クラスの line_round_dot_setting (点線(丸)設定)のインターフェイス](jp_graphics_line_round_dot_setting.md)
- [Graphics クラスの line_dash_dot_setting (一点鎖線設定)のインターフェイス](jp_graphics_line_dash_dot_setting.md)

---

## イベントの共通の各インターフェイス

### Table of contents

- [ハンドラの options パラメーターの型について](jp_about_handler_options_type.md)
- [Event クラスの prevent_default と stop_propagation の各インターフェイス](jp_event_prevent_default_and_stop_propagation.md)

- [bind_custom_event と trigger_custom_event の各インターフェイス](jp_bind_and_trigger_custom_event.md)

---

## MouseEvent クラスとマウスイベントの設定

<br><iframe src="static/mousemove_basic_usage/index.html" width="200" height="200"></iframe>

### Table of contents

- [MouseEvent クラスの各インターフェイスの概要](jp_mouse_event_abstract.md)
- [基本的なマウスイベントの各インターフェイス](jp_mouse_event_basic.md)

- [click インターフェイス](jp_click.md)
- [dblclick インターフェイス](jp_dblclick.md)

- [mousedown と mouseup のインターフェイス](jp_mousedown_and_mouseup.md)
- [mouseover と mouseout のインターフェイス](jp_mouseover_and_mouseout.md)

- [mousemove インターフェイス](jp_mousemove.md)

---

## 条件分岐の制御

### Table of contents

- [If クラス](jp_if.md)
- [Elif クラス](jp_elif.md)

- [Else クラス](jp_else.md)
- [各条件分岐のクラスのスコープ内の変数値の復元設定](jp_branch_instruction_variables_reverting_setting.md)

- [Return クラス](jp_return.md)

---

## ループ

### Table of contents

- [ループ用の For クラス](jp_for.md)
- [Continue クラス](jp_continue.md)

---

## タイマー

<br><iframe src="static/what_apysc_can_do_timer_animation/index.html" width="150" height="150"></iframe>

### Table of contents

- [Timer クラス](jp_timer.md)
- [TimerEvent クラス](jp_timer_event.md)

- [Timer クラスの delay 設定](jp_timer_delay.md)
- [FPS の enum](jp_fps.md)

- [Timer クラスの repeat_count 設定](jp_timer_repeat_count.md)
- [Timer クラスの start と stop の各インターフェイス](jp_timer_start_and_stop.md)

- [Timer クラスの timer_complete インターフェイス](jp_timer_complete.md)
- [Timer クラスの reset インターフェイス](jp_timer_reset.md)

---

## アニメーション

<br><iframe src="static/animation_interfaces_abstract_rotation_around_center/index.html" width="150" height="150"></iframe>

### Table of contents

- [アニメーションの各インターフェイスの概要](jp_animation_interfaces_abstract.md)
- [AnimationEvent クラス](jp_animation_event.md)

- [Animation クラスの duration 設定](jp_animation_duration.md)
- [Animation クラスの delay 設定](jp_animation_delay.md)

- [アニメーションの各インターフェイスの返却値について](jp_animation_return_value.md)
- [AnimationBase クラスの start インターフェイス](jp_animation_base_start.md)

- [AnimationBase クラスの animation_complete インターフェイス](jp_animation_complete.md)
- [AnimationBase クラスの各インターフェイスのメソッドチェーンについて](jp_animation_method_chaining.md)

- [AnimationBase クラスの target 属性](jp_animation_base_target.md)
- [アニメーションの pause と play の各インターフェイス](jp_animation_pause_and_play.md)

- [アニメーションの reset インターフェイス](jp_animation_reset.md)
- [アニメーションの finish インターフェイス](jp_animation_finish.md)

- [アニメーションの reverse インターフェイス](jp_animation_reverse.md)
- [animation_time インターフェイス](jp_animation_time.md)

- [イージングの enum](jp_easing_enum.md)
- [連続したアニメーション設定](jp_sequential_animation.md)

- [animation_parallel インターフェイス](jp_animation_parallel.md)
- [animation_move インターフェイス](jp_animation_move.md)

- [animation_x インターフェイス](jp_animation_x.md)
- [animation_y インターフェイス](jp_animation_y.md)

- [animation_width と animation_height の各インターフェイス](jp_animation_width_and_height.md)
- [animation_fill_color インターフェイス](jp_animation_fill_color.md)

- [animation_fill_alpha インターフェイス](jp_animation_fill_alpha.md)
- [animation_line_color インターフェイス](jp_animation_line_color.md)

- [animation_line_alpha インターフェイス](jp_animation_line_alpha.md)
- [animation_line_thickness インターフェイス](jp_animation_line_thickness.md)

- [animation_radius インターフェイス](jp_animation_radius.md)
- [animation_rotation_around_center インターフェイス](jp_animation_rotation_around_center.md)

- [animation_rotation_around_point インターフェイス](jp_animation_rotation_around_point.md)
- [animation_scale_x_from_center と animation_scale_y_from_center の各インターフェイス](jp_animation_scale_x_and_y_from_center.md)

- [animation_scale_x_from_point と animation_scale_y_from_point の各インターフェイス](jp_animation_scale_x_and_y_from_point.md)
- [animation_skew_x インターフェイス](jp_animation_skew_x.md)

---

## その他の操作関係の各インターフェイス

### Table of contents

- [delete インターフェイス](jp_delete.md)

---

## デバッグ

### Table of contents

- [trace 関数のインターフェイス](jp_trace.md)
- [set_debug_mode インターフェイス](jp_set_debug_mode.md)

- [unset_debug_mode インターフェイス](jp_unset_debug_mode.md)
- [add_debug_info_setting のデコレーターのインターフェイス](jp_add_debug_info_setting.md)

---

## テスト

### Table of contents

- [JavaScriptの各アサーションのインターフェイスの基本的な挙動](jp_assertion_basic_behavior.md)
- [assert_equal と assert_not_equal の各インターフェイス](jp_assert_equal_and_not_equal.md)

- [assert_true と assert_false の各インターフェイス](jp_assert_true_and_false.md)
- [assert_arrays_equal と assert_arrays_not_equal の各インターフェイス](jp_assert_arrays_equal_and_arrays_not_equal.md)

- [assert_dicts_equal と assert_dicts_not_equal の各インターフェイス](jp_assert_dicts_equal_and_dicts_not_equal.md)
- [assert_defined と assert_undefined の各インターフェイス](jp_assert_defined_and_undefined.md)