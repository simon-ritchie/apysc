"""This module is for the translation mapping data of the
following document:

Document file: set_debug_mode.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# set_debug_mode interface": "# set_debug_mode インターフェイス",
    ##################################################
    "This page explains the `set_debug_mode` function interface.": "このページでは`set_debug_mode`関数のインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `set_debug_mode` function interface sets the debug mode setting. This setting appends the debug information (Python function or method calls and arguments information) to the exported HTML.": "`set_debug_mode`関数のインターフェイスはデバッグモードの設定を有効化します。この設定はデバッグ用の情報（Python上の関数やメソッドの呼び出しと引数情報など）を出力されるHTML上に追加します。",  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "The debug mode setting appends lots of information to the HTML. As a result, the exporting time becomes long, and the HTML file size becomes large.": "デバッグモードの設定は多くの情報をHTML上に追加します。結果として出力時間は長くなり、ファイルサイズも大きくなります。",  # noqa
    ##################################################
    "Also, this setting ignores the `minify` setting.": "また、この設定は`minify`（HTML最小化）の設定も無視します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "After the stage instantiation, you can set the debug mode by the `set_debug_mode` function.": "ステージのインスタンス後であれば`set_debug_mode`関数を使ってデバッグモードを設定ずることができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nap.set_debug_mode()\nsprite: ap.Sprite = ap.Sprite()\nint_1: ap.Int = ap.Int(10)\n\nap.save_overall_html(dest_dir_path="set_debug_mode_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nap.set_debug_mode()\nsprite: ap.Sprite = ap.Sprite()\nint_1: ap.Int = ap.Int(10)\n\nap.save_overall_html(dest_dir_path="set_debug_mode_basic_usage/")\n```',  # noqa
    ##################################################
    "This setting appends the information (Python's function and method callings, its module and class names, and argument information) as the JavaScript comment to the exported HTML, like the following:": "この設定は以下の例の用に出力されたHTML内にPythonの関数やメソッドの呼び出しやそのモジュールやクラス名、引数情報などのJavaScriptのコメントを追加します:",  # noqa
    ##################################################
    "```js\n...\n  //////////////////////////////////////////////////////////////////////\n  // [__init__ 1] started.\n  // module name: apysc._display.sprite\n  // class: Sprite\n  // arguments and variables:\n  //    variable_name = None\n  //    self = Sprite('')()\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 2] started.\n    // module name: apysc._type.array\n    // class: Array\n    // arguments and variables:\n    //    value = []\n    //    self = []()\n      //////////////////////////////////////////////////////////////////////\n      // [_append_constructor_expression 2] started.\n      // module name: apysc._type.array\n      // class: Array\n      // arguments and variables:\n      //    self = [](arr_2)\n        var arr_2 = [];\n      // [_append_constructor_expression 2] ended.\n      // module name: apysc._type.array\n      // class: Array\n      //////////////////////////////////////////////////////////////////////\n    // [__init__ 2] ended.\n    // module name: apysc._type.array\n    // class: Array\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 1] started.\n    // module name: apysc._display.display_object\n    // class: DisplayObject\n    // arguments and variables:\n    //    variable_name = 'sp_1'\n    //    self = Sprite('')()\n    // [__init__ 1] ended.\n    // module name: apysc._display.display_object\n    // class: DisplayObject\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [_append_constructor_expression 1] started.\n    // module name: apysc._display.sprite\n    // class: Sprite\n    // arguments and variables:\n    //    self = Sprite('sp_1')(sp_1)\n      var sp_1 = stage.nested();\n    // [_append_constructor_expression 1] ended.\n    // module name: apysc._display.sprite\n    // class: Sprite\n    //////////////////////////////////////////////////////////////////////\n...\n```": "```js\n...\n  //////////////////////////////////////////////////////////////////////\n  // [__init__ 1] started.\n  // module name: apysc._display.sprite\n  // class: Sprite\n  // arguments and variables:\n  //    variable_name = None\n  //    self = Sprite('')()\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 2] started.\n    // module name: apysc._type.array\n    // class: Array\n    // arguments and variables:\n    //    value = []\n    //    self = []()\n      //////////////////////////////////////////////////////////////////////\n      // [_append_constructor_expression 2] started.\n      // module name: apysc._type.array\n      // class: Array\n      // arguments and variables:\n      //    self = [](arr_2)\n        var arr_2 = [];\n      // [_append_constructor_expression 2] ended.\n      // module name: apysc._type.array\n      // class: Array\n      //////////////////////////////////////////////////////////////////////\n    // [__init__ 2] ended.\n    // module name: apysc._type.array\n    // class: Array\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [__init__ 1] started.\n    // module name: apysc._display.display_object\n    // class: DisplayObject\n    // arguments and variables:\n    //    variable_name = 'sp_1'\n    //    self = Sprite('')()\n    // [__init__ 1] ended.\n    // module name: apysc._display.display_object\n    // class: DisplayObject\n    //////////////////////////////////////////////////////////////////////\n    //////////////////////////////////////////////////////////////////////\n    // [_append_constructor_expression 1] started.\n    // module name: apysc._display.sprite\n    // class: Sprite\n    // arguments and variables:\n    //    self = Sprite('sp_1')(sp_1)\n      var sp_1 = stage.nested();\n    // [_append_constructor_expression 1] ended.\n    // module name: apysc._display.sprite\n    // class: Sprite\n    //////////////////////////////////////////////////////////////////////\n...\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [unset_debug_mode interface](unset_debug_mode.md)": "- [unset_debug_mode インターフェイス](jp_unset_debug_mode.md)",  # noqa
    ##################################################
    "## set_debug_mode API": "## set_debug_mode API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Set the debug mode for the HTML and JavaScript debugging. If calling this function, this interface applies the following setting: ": "HTMLとJavaScriptのデバッグ用にデバッグモードの設定を行います。もしこの関数を呼び出した場合、のインターフェイスは以下の設定を追加します: ",  # noqa
    ##################################################
    "<br> ・Disabling HTML minify setting. ": "<br> ・HTMLの最小化（minify）設定を無効化します。 ",
    ##################################################
    "<br> ・Changing to append per each interface JavaScript divider string.<hr>": "<br> ・各インターフェイスごとのJavaScript上での区切りのための文字列を追加します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ap.set_debug_mode()\n>>> int_val: ap.Int = ap.Int(10)\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> ap.set_debug_mode()\n>>> int_val: ap.Int = ap.Int(10)\n```",  # noqa
}
