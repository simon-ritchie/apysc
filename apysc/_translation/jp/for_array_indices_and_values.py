"""This module is for the translation mapping data of the
following document:

Document file: for_array_indices_and_values.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# ForArrayIndicesAndValues class": "# ForArrayIndicesAndValues クラス",
    ##################################################
    "This page explains the `ForArrayIndicesAndValues` class.": "このページでは`ForArrayIndicesAndValues`クラスについて説明します。",  # noqa
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):": "事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `ForArrayIndicesAndValues` class is the for-loop class.": "`ForArrayIndicesAndValues`クラスはループ制御のためのクラスです。",  # noqa
    ##################################################
    "This interface returns `Array`'s index and value in a loop.": "このインターフェイスはループ内で`Array`クラスのインデックスと値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "This class requires using the `with`-statement.": "このクラスは`with`ステートメントと共に使う必要があります。",  # noqa
    ##################################################
    "The `as`-keyword value becomes an `Array`'s index and value.": "`as`キーワードの値は`Array`クラスのインデックスと値になります。",  # noqa
    ##################################################
    "Also, this class requires the `arr_value_type` to specify a type of an `Array`'s value type.": "また、このクラスは`Array`の配列内の値の型の指定用に`arr_value_type`引数の指定が必要になります。",  # noqa
    ##################################################
    "This type only accepts an apysc type, such as the `Int`, `Number`, `String`, or `Rectangle`.": "この型の指定は`Int`や`Number`、`String`や`Rectangle`などのapyscの型（クラス）のみ受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=225,\n    background_color=ap.Color("#333"),\n)\n\nx_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])\nwith ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (i, x):\n    circle: ap.Circle = ap.Circle(\n        x=x,\n        y=(i + 1) * 50,\n        radius=25,\n        fill_color=ap.Color("#0af"),\n    )\n\nap.save_overall_html(dest_dir_path="for_array_indices_and_values_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=350,\n    stage_height=225,\n    background_color=ap.Color("#333"),\n)\n\nx_arr: ap.Array[ap.Number] = ap.Array([ap.Number(75), ap.Number(175), ap.Number(275)])\nwith ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (i, x):\n    circle: ap.Circle = ap.Circle(\n        x=x,\n        y=(i + 1) * 50,\n        radius=25,\n        fill_color=ap.Color("#0af"),\n    )\n\nap.save_overall_html(dest_dir_path="for_array_indices_and_values_basic_usage_1/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "  - Notes: This class also has the same arguments and behaves in the same way.": "  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。",  # noqa
    ##################################################
    "## ForArrayIndicesAndValues API": "## ForArrayIndicesAndValues API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The loop implementation class for the `ap.Array` indices and values.<hr>": "`ap.Array`の各インデックスと値に対するループ制御の実装となるクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `arr`: Array[_ArrayValue]": "- `arr`: Array[_ArrayValue]",
    ##################################################
    "  - An array to iterate.": "  - イテレーションのための配列。",
    ##################################################
    "- `arr_value_type`: Type[_ArrayValue]": "- `arr_value_type`: Type[_ArrayValue]",
    ##################################################
    "  - An array value type. This interface accepts apysc types, such as the `Int`, `String`, `Rectangle`.": "  - 配列の値の型。このインターフェイスは`Int`、`String`、`Rectangle`などのapyscの型を受け付けます。",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     stage_width=350, stage_height=225, background_color=ap.Color("#333")\n... )\n>>> x_arr: ap.Array[ap.Number] = ap.Array(\n...     [ap.Number(75), ap.Number(175), ap.Number(275)]\n... )\n>>> with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (\n...     i,\n...     x,\n... ):\n...     circle: ap.Circle = ap.Circle(\n...         x=x,\n...         y=(i + 1) * 50,\n...         radius=25,\n...         fill_color=ap.Color("#0af"),\n...     )\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(\n...     stage_width=350, stage_height=225, background_color=ap.Color("#333")\n... )\n>>> x_arr: ap.Array[ap.Number] = ap.Array(\n...     [ap.Number(75), ap.Number(175), ap.Number(275)]\n... )\n>>> with ap.ForArrayIndicesAndValues(arr=x_arr, arr_value_type=ap.Number) as (\n...     i,\n...     x,\n... ):\n...     circle: ap.Circle = ap.Circle(\n...         x=x,\n...         y=(i + 1) * 50,\n...         radius=25,\n...         fill_color=ap.Color("#0af"),\n...     )\n```',  # noqa
}
