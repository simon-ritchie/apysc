"""This module is for the translation mapping data of the
following document:

Document file: unset_debug_mode.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# unset_debug_mode interface": "# unset_debug_mode インターフェイス",
    ##################################################
    "This page explains the `unset_debug_mode` function interface.": "このページでは`unset_debug_mode`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `unset_debug_mode` function interface unsets the debug mode setting. It stops the debug information appending.": "`unset_debug_mode`関数のインターフェイスはデバッグモードの設定を解除します。この関数はデバッグ情報の追加を停止します。",  # noqa
    ##################################################
    "The debug mode exports lots of information. Sometimes it becomes cumbersome. In that case, stopping the debug mode is helpful when it is no longer needed.": "デバッグモードの設定は大量の情報を出力します。時折これは煩雑な（情報が多すぎる）状態になることがあります。そのような場合にデバッグモードが不要になったタイミングで設定を解除すると役に立つことがあります。",  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "If the exporting interface (e.g., `ap.save_overall_html`) `minify` option is enabled, it removes debug mode information. So it is required to set the `minify=False` when you use the `unset_debug_mode` interface.": "もしも出力のインターフェイス（例 : `ap.save_overall_html`など）の`minify`のオプションが有効になっていると、デバッグモードの情報なども削除されてしまいます。そのため`unset_debug_mode`インターフェイスでデバッグモードを解除した場合には`minify=False`の引数設定が必要になります。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `unset_debug_mode` interface requires no arguments.": "`unset_debug_mode`インターフェイスは引数の指定を必要としません。",  # noqa
    ##################################################
    "The following example appends the debug information only at the `int_1` instantiation and incremental addition of 10.": "以下のコード例では`int_1`の変数のインスタンス化と10の加算処理の箇所のみデバッグ情報の追加を有効化しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nap.set_debug_mode()\nint_1: ap.Int = ap.Int(10)\nint_1 += 10\nap.unset_debug_mode()\nint_2: ap.Int = ap.Int(20)\nint_2 += 20\n\nap.save_overall_html(minify=False, dest_dir_path="unset_debug_mode_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nap.set_debug_mode()\nint_1: ap.Int = ap.Int(10)\nint_1 += 10\nap.unset_debug_mode()\nint_2: ap.Int = ap.Int(20)\nint_2 += 20\n\nap.save_overall_html(minify=False, dest_dir_path="unset_debug_mode_basic_usage/")\n```',  # noqa
    ##################################################
    "The exported HTML includes the debug information at the first integer position. It doesn't include the sprite and second integer positions, as follows:": "出力されたHTMLでは最初の整数部分のデバッグ情報を以下のように含んでいます。その後のスプライトや2つ目の整数関係の位置のものは含まれないようになっています:",  # noqa
    ##################################################
    "```js\n...\n  var sp_1 = stage.nested();\n  var g_1 = stage.nested();\n  arr_2.push(g_1);\n  var i_12 = -1;\n  i_12 = arr_2.indexOf(g_1);\n  var b_3 = false;\n  var i_13 = -1;\n...\n  //////////////////////////////////////////////////////////////////////\n  // [__init__ 12] started.\n  // module name: apysc._type.int\n  // class: Int\n  // arguments and variables:\n  //    value = 10\n  //    self = 0()\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 14] started.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    // arguments and variables:\n    //    type_name = 'i'\n    //    value = 10\n    //    self = 0(i_16)\n    // [__init__ 14] ended.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [to_int_from_float 14] started.\n    // module name: apysc._converter.cast\n    // arguments and variables:\n    //    int_or_float = 10\n    // [to_int_from_float 14] ended.\n    // module name: apysc._converter.cast\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [append_constructor_expression 14] started.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    // arguments and variables:\n    //    self = 10(i_16)\n      var i_16 = 10;\n    // [append_constructor_expression 14] ended.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    //////////////////////////////////////////////////////////////////////\n...\n  var i_18 = 20;\n  var i_19 = cpy(i_18);\n  var i_19 = i_18 + 20;\n  i_18 = i_19;\n...\n```": "```js\n...\n  var sp_1 = stage.nested();\n  var g_1 = stage.nested();\n  arr_2.push(g_1);\n  var i_12 = -1;\n  i_12 = arr_2.indexOf(g_1);\n  var b_3 = false;\n  var i_13 = -1;\n...\n  //////////////////////////////////////////////////////////////////////\n  // [__init__ 12] started.\n  // module name: apysc._type.int\n  // class: Int\n  // arguments and variables:\n  //    value = 10\n  //    self = 0()\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 14] started.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    // arguments and variables:\n    //    type_name = 'i'\n    //    value = 10\n    //    self = 0(i_16)\n    // [__init__ 14] ended.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [to_int_from_float 14] started.\n    // module name: apysc._converter.cast\n    // arguments and variables:\n    //    int_or_float = 10\n    // [to_int_from_float 14] ended.\n    // module name: apysc._converter.cast\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [append_constructor_expression 14] started.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    // arguments and variables:\n    //    self = 10(i_16)\n      var i_16 = 10;\n    // [append_constructor_expression 14] ended.\n    // module name: apysc._type.number_value_mixin\n    // class: NumberValueMixIn\n    //////////////////////////////////////////////////////////////////////\n...\n  var i_18 = 20;\n  var i_19 = cpy(i_18);\n  var i_19 = i_18 + 20;\n  i_18 = i_19;\n...\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [set_debug_mode interface](set_debug_mode.md)": "- [set_debug_mode インターフェイス](jp_set_debug_mode.md)",  # noqa
    ##################################################
    "## unset_debug_mode API": "## unset_debug_mode API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Unset the debug mode for the HTML and JavaScript debugging.<hr>": "HTMLとJavaScriptのデバッグ用のデバッグモードの設定を解除します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ap.set_debug_mode()\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.unset_debug_mode()\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ap.set_debug_mode()\n>>> int_val: ap.Int = ap.Int(10)\n>>> ap.unset_debug_mode()\n```",  # noqa
}
