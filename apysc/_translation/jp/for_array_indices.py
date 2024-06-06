"""This module is for the translation mapping data of the
following document:

Document file: for_array_indices.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# ForArrayIndices class": "# ForArrayIndices クラス",
    ##################################################
    "This page explains the `ForArrayIndices` class.": "このページでは`ForArrayIndices`クラスについて説明します。",  # noqa
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):": "事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `ForArrayIndices` class is the for-loop class.": "`ForArrayIndices`クラスはループ制御のためのクラスです。",  # noqa
    ##################################################
    "This interface returns `Array`'s index (starts with 0) in a loop.": "このインターフェイスではループ中の`Array`クラスのインデックス（0からスタートします）を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "This class requires using the `with`-statement.": "このクラスは`with`ステートメントと共に使う必要があります。",  # noqa
    ##################################################
    "The `as`-keyword value becomes the `Int` type index.": "`as`キーワードの値は`Int`型のインデックスとなります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\narr: ap.Array[ap.Number] = ap.Array([ap.Number(50), ap.Number(150), ap.Number(250)])\nindices: ap.Array[ap.Int] = ap.Array([])\nwith ap.ForArrayIndices(arr=arr) as i:\n    indices.append(i)\n\nap.assert_arrays_equal(indices, [0, 1, 2])\n\nap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\narr: ap.Array[ap.Number] = ap.Array([ap.Number(50), ap.Number(150), ap.Number(250)])\nindices: ap.Array[ap.Int] = ap.Array([])\nwith ap.ForArrayIndices(arr=arr) as i:\n    indices.append(i)\n\nap.assert_arrays_equal(indices, [0, 1, 2])\n\nap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_1/")\n```',  # noqa
    ##################################################
    "The following example uses an index and sets a circle center-x coordinate.": "以下の例ではインデックスを使って円の中心のX座標を設定しています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nx_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])\nwith ap.ForArrayIndices(arr=x_arr) as i:\n    x: ap.Number = x_arr[i]\n    circle: ap.Circle = ap.Circle(\n        x=x,\n        y=75,\n        radius=25,\n        fill_color=ap.Color("#0af"),\n    )\n\nap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_2/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=150,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\nx_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])\nwith ap.ForArrayIndices(arr=x_arr) as i:\n    x: ap.Number = x_arr[i]\n    circle: ap.Circle = ap.Circle(\n        x=x,\n        y=75,\n        radius=25,\n        fill_color=ap.Color("#0af"),\n    )\n\nap.save_overall_html(dest_dir_path="for_array_indices_basic_usage_2/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "  - Notes: This class also has the same arguments and behaves in the same way.": "  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。",  # noqa
    ##################################################
    "## ForArrayIndices API": "## ForArrayIndices API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The loop implementation class for the `ap.Array` indices.<hr>": "`ap.Array`のインデックス制御のためのループ制御用のクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `arr`: Array": "- `arr`: Array",
    ##################################################
    "  - An array to iterate.": "  - イテレーションのための配列。",
    ##################################################
    "- `locals_`: Optional[Dict[str, Any]], optional": "- `locals_`: Optional[Dict[str, Any]], optional",  # noqa
    ##################################################
    "  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of a with-statement scope. This setting is useful when you don't want to update each variable.": "  - 現在のスコープの各ローカル変数。この引数にはlocals()関数の返却値を設定してください。もしこの引数が指定された場合、このインターフェイスはローカルスコープのVariableNameMixInの各変数（例 : IntやSpriteなど）の値をwithステートメントの最後で復元します。この設定は各変数を更新したくない場合等に役立ちます。",  # noqa
    ##################################################
    "- `globals_`: Optional[Dict[str, Any]], optional": "- `globals_`: Optional[Dict[str, Any]], optional",  # noqa
    ##################################################
    "  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.": "  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, optional": "- `variable_name_suffix`: str, optional",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array[ap.Number] = ap.Array(\n...     [ap.Number(50), ap.Number(150), ap.Number(250)]\n... )\n>>> indices: ap.Array[ap.Int] = ap.Array([])\n>>> with ap.ForArrayIndices(arr=arr) as i:\n...     indices.append(i)\n...\n>>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array[ap.Number] = ap.Array(\n...     [ap.Number(50), ap.Number(150), ap.Number(250)]\n... )\n>>> indices: ap.Array[ap.Int] = ap.Array([])\n>>> with ap.ForArrayIndices(arr=arr) as i:\n...     indices.append(i)\n...\n>>> _ = ap.assert_arrays_equal(indices, [0, 1, 2])\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Why the apysc library doesn’t use the Python built-in data type](https://simon-ritchie.github.io/apysc/en/why_apysc_doesnt_use_python_builtin_data_type.html)": "- [なぜapyscライブラリではPythonビルトインのデータ型を使っていないのか](https://simon-ritchie.github.io/apysc/jp/jp_why_apysc_doesnt_use_python_builtin_data_type.html)",  # noqa
    ##################################################
    "- [Each branch instruction class’s scope variable reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)": "- [各分岐制御のクラスのスコープ内の変数値の復元設定](https://simon-ritchie.github.io/apysc/jp/jp_branch_instruction_variables_reverting_setting.html)",  # noqa
}
