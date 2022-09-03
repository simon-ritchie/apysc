"""This module is for the translation mapping data of the
following document:

Document file: index.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# apysc documentation": "# apysc ドキュメント",
    ##################################################
    "Welcome to apysc documentation! apysc is the Python front-end library (currently developing and only works partially).": "apyscのドキュメントページへようこそ。apyscはPythonのフロントエンド用のライブラリです（現在開発中であり部分的にのみ動作します）。",  # noqa
    ##################################################
    "## Project links": "## プロジェクトの関連リンク",
    ##################################################
    "- [GitHub](https://github.com/simon-ritchie/apysc)": "- [GitHub](https://github.com/simon-ritchie/apysc)",  # noqa
    ##################################################
    "  - Please leave a ⭐️star⭐️ if you favor the apysc library or have high hopes for the library's future!": "  - もしもapyscライブラリを気にいったり、もしくはライブラリの将来に期待が出来そうと感じられたらリポジトリにスターを付けていただけますと幸いです。",  # noqa
    ##################################################
    "- [PyPI](https://pypi.org/project/apysc/)": "- [PyPI](https://pypi.org/project/apysc/)",  # noqa
    ##################################################
    "Other languages documentations: | English | [Japanese (日本語)](https://simon-ritchie.github.io/apysc/jp/jp_index.html) |": "他の言語のドキュメント: | [英語 (English)](https://simon-ritchie.github.io/apysc/en/index.html) | 日本語 |",  # noqa
    ##################################################
    "## Quick start guide": "## クイックスタートガイド",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nwhat_apysc_can_do\nquick_start\nimport_conventions\nrecommended_type_checker_settings\n```": "```{toctree}\n:maxdepth: 1\njp_what_apysc_can_do\njp_quick_start\njp_import_conventions\njp_recommended_type_checker_settings\n```",  # noqa
    ##################################################
    "## Container classes": "## コンテナーの各クラス",
    ##################################################
    "The `Stage` is the apysc overall drawing area container, and the `Sprite` is the container class.": "`Stage`はapyscの描画領域全体のコンテナーとなり、`Sprite`は通常の各インスタンスのコンテナーのクラスとなります。",  # noqa
    ##################################################
    "```{toctree}\n:maxdepth: 1\nstage\nsprite\n```": "```{toctree}\n:maxdepth: 1\njp_stage\njp_sprite\n```",  # noqa
    ##################################################
    "## Exporting": "## 出力処理",
    ##################################################
    "The HTML and JavaScript exporting interfaces.": "以下はHTMLとJavaScriptの出力処理関係の各インターフェイスです。",  # noqa
    ##################################################
    "```{toctree}\n:maxdepth: 1\nsave_overall_html\ndisplay_on_jupyter\ndisplay_on_colaboratory\nappend_js_expression\n```": "```{toctree}\n:maxdepth: 1\njp_save_overall_html\njp_display_on_jupyter\njp_display_on_colaboratory\njp_append_js_expression\n```",  # noqa
    ##################################################
    "## Child-related interfaces": "## 子要素関係の各インターフェイス",
    ##################################################
    "The parent class, such as the `Sprite` or `Stage`, has the following interfaces:": "`Sprite`や`Stage`などの親となれる各クラスは以下のインターフェイスを持っています:",  # noqa
    ##################################################
    "```{toctree}\n:maxdepth: 1\nadd_child_and_remove_child\nremove_children\ncontains\nnum_children\nget_child_at\n```": "```{toctree}\n:maxdepth: 1\njp_add_child_and_remove_child\njp_remove_children\njp_contains\njp_num_children\njp_get_child_at\n```",  # noqa
    ##################################################
    "## apysc basic data classes": "## apyscの基本的な各データクラス",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nwhy_apysc_doesnt_use_python_builtin_data_type\nfundamental_data_classes_value_interface\nint_and_number\nint_and_number_arithmetic_operations\nint_and_number_comparison_operations\nstring\nstring_comparison_operations\nstring_addition_and_multiplication\nboolean\narray\narray_append_and_push\narray_extend_and_concat\narray_insert_and_insert_at\narray_pop\narray_remove_and_remove_at\narray_sort\narray_reverse\narray_slice\narray_length\narray_join\narray_index_of\narray_clear\narray_comparison\ndictionary\ndictionary_generic\ndictionary_get\ndictionary_length\n```": "```{toctree}\n:maxdepth: 1\njp_why_apysc_doesnt_use_python_builtin_data_type\njp_fundamental_data_classes_value_interface\njp_int_and_number\njp_int_and_number_arithmetic_operations\njp_int_and_number_comparison_operations\njp_string\njp_string_comparison_operations\njp_string_addition_and_multiplication\njp_boolean\njp_array\njp_array_append_and_push\njp_array_extend_and_concat\njp_array_insert_and_insert_at\njp_array_pop\njp_array_remove_and_remove_at\njp_array_sort\njp_array_reverse\njp_array_slice\njp_array_length\njp_array_join\njp_array_index_of\njp_array_clear\njp_array_comparison\njp_dictionary\njp_dictionary_generic\njp_dictionary_get\njp_dictionary_length\n```",  # noqa
    ##################################################
    "## DisplayObject and GraphicsBase classes": "## DisplayObject と GraphicsBase の各クラス",  # noqa
    ##################################################
    "The `DisplayObject` class is the base class for each display object. The `GraphicsBase` class is the `DisplayObject` subclass and the base class of each graphic class, such as the `Rectangle` class.": "`DisplayObject`クラスは各表示用のオブジェクトの基底クラスです。`GraphicsBase`クラスは`DisplayObject`のサブクラスであり、且つ`Rectangle`などの各グラフィックスの基底クラスとなります。",  # noqa
    ##################################################
    "```{toctree}\n:maxdepth: 1\ndisplay_object\ndisplay_object_and_graphics_base_prop_abstract\ndisplay_object_x_and_y\ndisplay_object_parent\ndisplay_object_visible\ndisplay_object_get_and_set_css\ndisplay_object_mouse_event\ngraphics_base_fill_color\ngraphics_base_fill_alpha\ngraphics_base_line_color\ngraphics_base_line_alpha\ngraphics_base_line_thickness\ngraphics_base_line_dot_setting\ngraphics_base_line_dash_setting\ngraphics_base_line_round_dot_setting\ngraphics_base_line_dash_dot_setting\ngraphics_base_rotation_around_center\ngraphics_base_rotation_around_point\ngraphics_base_scale_from_center\ngraphics_base_scale_from_point\ngraphics_base_flip_interfaces\ngraphics_base_skew\n```": "```{toctree}\n:maxdepth: 1\njp_display_object\njp_display_object_and_graphics_base_prop_abstract\njp_display_object_x_and_y\njp_display_object_parent\njp_display_object_visible\njp_display_object_get_and_set_css\njp_display_object_mouse_event\njp_graphics_base_fill_color\njp_graphics_base_fill_alpha\njp_graphics_base_line_color\njp_graphics_base_line_alpha\njp_graphics_base_line_thickness\njp_graphics_base_line_dot_setting\njp_graphics_base_line_dash_setting\njp_graphics_base_line_round_dot_setting\njp_graphics_base_line_dash_dot_setting\njp_graphics_base_rotation_around_center\njp_graphics_base_rotation_around_point\njp_graphics_base_scale_from_center\njp_graphics_base_scale_from_point\njp_graphics_base_flip_interfaces\njp_graphics_base_skew\n```",  # noqa
    ##################################################
    "## Each graphic class": "## 各グラフィックのクラス",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nrectangle\ncircle\nellipse\nline\npolyline\npolygon\npath\n```": "```{toctree}\n:maxdepth: 1\njp_rectangle\njp_circle\njp_ellipse\njp_line\njp_polyline\njp_polygon\njp_path\n```",  # noqa
    ##################################################
    "## Graphics class": "## Graphics クラス",
    ##################################################
    "The `Graphics` class handles each vector graphics drawing.": "`Graphics`クラスは各ベクターグラフィックスの描画処理を扱います。",  # noqa
    ##################################################
    "```{toctree}\n:maxdepth: 1\ndraw_interfaces_abstract\ngraphics\ngraphics_begin_fill\ngraphics_line_style\ngraphics_draw_rect\ngraphics_draw_round_rect\ngraphics_draw_circle\ngraphics_draw_ellipse\ngraphics_move_to_and_line_to\ngraphics_draw_line\ngraphics_draw_dotted_line\ngraphics_draw_dashed_line\ngraphics_draw_round_dotted_line\ngraphics_draw_dash_dotted_line\ngraphics_draw_polygon\ngraphics_draw_path\ngraphics_clear\n```": "```{toctree}\n:maxdepth: 1\njp_draw_interfaces_abstract\njp_graphics\njp_graphics_begin_fill\njp_graphics_line_style\njp_graphics_draw_rect\njp_graphics_draw_round_rect\njp_graphics_draw_circle\njp_graphics_draw_ellipse\njp_graphics_move_to_and_line_to\njp_graphics_draw_line\njp_graphics_draw_dotted_line\njp_graphics_draw_dashed_line\njp_graphics_draw_round_dotted_line\njp_graphics_draw_dash_dotted_line\njp_graphics_draw_polygon\njp_graphics_draw_path\njp_graphics_clear\n```",  # noqa
    ##################################################
    "## Geometry-related classes": "## 座標・サイズ等のデータの各クラス",
    ##################################################
    "```{toctree}\n:maxdepth: 1\npoint2d\npath_move_to\npath_line_to\npath_horizontal\npath_vertical\npath_close\npath_bezier_2d\npath_bezier_2d_continual\npath_bezier_3d\npath_bezier_3d_continual\n```": "```{toctree}\n:maxdepth: 1\njp_point2d\njp_path_move_to\njp_path_line_to\njp_path_horizontal\njp_path_vertical\njp_path_close\njp_path_bezier_2d\njp_path_bezier_2d_continual\njp_path_bezier_3d\njp_path_bezier_3d_continual\n```",  # noqa
    ##################################################
    "## Common event interfaces": "## イベントの共通の各インターフェイス",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nabout_handler_options_type\nevent_prevent_default_and_stop_propagation\nbind_and_trigger_custom_event\n```": "```{toctree}\n:maxdepth: 1\njp_about_handler_options_type\njp_event_prevent_default_and_stop_propagation\njp_bind_and_trigger_custom_event\n```",  # noqa
    ##################################################
    "## MouseEvent class and mouse event binding": "## MouseEvent クラスとマウスイベントの設定",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nmouse_event_abstract\nmouse_event_basic\nclick\ndblclick\nmousedown_and_mouseup\nmouseover_and_mouseout\nmousemove\n```": "```{toctree}\n:maxdepth: 1\njp_mouse_event_abstract\njp_mouse_event_basic\njp_click\njp_dblclick\njp_mousedown_and_mouseup\njp_mouseover_and_mouseout\njp_mousemove\n```",  # noqa
    ##################################################
    "## Branch instruction": "## 条件分岐の制御",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nif\nelif\nelse\nbranch_instruction_variables_reverting_setting\nreturn\n```": "```{toctree}\n:maxdepth: 1\njp_if\njp_elif\njp_else\njp_branch_instruction_variables_reverting_setting\njp_return\n```",  # noqa
    ##################################################
    "## Loop": "## ループ",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nfor\ncontinue\n```": "```{toctree}\n:maxdepth: 1\njp_for\njp_continue\n```",  # noqa
    ##################################################
    "## Timer": "## タイマー",
    ##################################################
    "```{toctree}\n:maxdepth: 1\ntimer\ntimer_event\ntimer_delay\nfps\ntimer_repeat_count\ntimer_start_and_stop\ntimer_complete\ntimer_reset\n```": "```{toctree}\n:maxdepth: 1\njp_timer\njp_timer_event\njp_timer_delay\njp_fps\njp_timer_repeat_count\njp_timer_start_and_stop\njp_timer_complete\njp_timer_reset\n```",  # noqa
    ##################################################
    "## Animation": "## アニメーション",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nanimation_interfaces_abstract\nanimation_event\nanimation_duration\nanimation_delay\nanimation_return_value\nanimation_base_start\nanimation_complete\nanimation_method_chaining\nanimation_base_target\nanimation_pause_and_play\nanimation_reset\nanimation_finish\nanimation_reverse\nanimation_time\neasing_enum\nsequential_animation\nanimation_parallel\nanimation_move\nanimation_x\nanimation_y\nanimation_width_and_height\nanimation_fill_color\nanimation_fill_alpha\nanimation_line_color\nanimation_line_alpha\nanimation_line_thickness\nanimation_radius\nanimation_rotation_around_center\nanimation_rotation_around_point\nanimation_scale_x_and_y_from_center\nanimation_scale_x_and_y_from_point\n```": "```{toctree}\n:maxdepth: 1\njp_animation_interfaces_abstract\njp_animation_event\njp_animation_duration\njp_animation_delay\njp_animation_return_value\njp_animation_base_start\njp_animation_complete\njp_animation_method_chaining\njp_animation_base_target\njp_animation_pause_and_play\njp_animation_reset\njp_animation_finish\njp_animation_reverse\njp_animation_time\njp_easing_enum\njp_sequential_animation\njp_animation_parallel\njp_animation_move\njp_animation_x\njp_animation_y\njp_animation_width_and_height\njp_animation_fill_color\njp_animation_fill_alpha\njp_animation_line_color\njp_animation_line_alpha\njp_animation_line_thickness\njp_animation_radius\njp_animation_rotation_around_center\njp_animation_rotation_around_point\njp_animation_scale_x_and_y_from_center\njp_animation_scale_x_and_y_from_point\n```",  # noqa
    ##################################################
    "## Other manipulation interfaces": "## その他の操作関係の各インターフェイス",
    ##################################################
    "```{toctree}\n:maxdepth: 1\ndelete\n```": "```{toctree}\n:maxdepth: 1\njp_delete\n```",  # noqa
    ##################################################
    "## Debugging": "## デバッグ",
    ##################################################
    "```{toctree}\n:maxdepth: 1\ntrace\nset_debug_mode\nunset_debug_mode\nadd_debug_info_setting\nvariable_name_suffix\n```": "```{toctree}\n:maxdepth: 1\njp_trace\njp_set_debug_mode\njp_unset_debug_mode\njp_add_debug_info_setting\njp_variable_name_suffix\n```",  # noqa
    ##################################################
    "## Testing": "## テスト",
    ##################################################
    "```{toctree}\n:maxdepth: 1\nassertion_basic_behavior\nassert_equal_and_not_equal\nassert_true_and_false\nassert_arrays_equal_and_arrays_not_equal\nassert_dicts_equal_and_dicts_not_equal\nassert_defined_and_undefined\n```": "```{toctree}\n:maxdepth: 1\njp_assertion_basic_behavior\njp_assert_equal_and_not_equal\njp_assert_true_and_false\njp_assert_arrays_equal_and_arrays_not_equal\njp_assert_dicts_equal_and_dicts_not_equal\njp_assert_defined_and_undefined\n```",  # noqa
}
