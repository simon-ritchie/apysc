"""This module is for the translation mapping data of the
following document:

Document file: for_dict_keys_and_values.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# ForDictKeysAndValues class": "# ForDictKeysAndValues クラス",
    ##################################################
    "This page explains the `ForDictKeysAndValues` class.": "このページでは`ForDictKeysAndValues`クラスについて説明します。",  # noqa
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):": "事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `ForDictKeysAndValues` class is the for-loop class.": "`ForDictKeysAndValues`クラスはfor文のループのためのクラスです。",  # noqa
    ##################################################
    "This interface returns `Dictionary`'s key and value in a loop.": "このインターフェイスはループの中で`Dictionary`のキーと値を返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "This class requires using the `with`-statement.": "このクラスは`with`ステートメントと共に使う必要があります。",  # noqa
    ##################################################
    "The `as`-keyword value becomes a `Dictionary`'s key and value.": "`as`キーワード部分の値は`Dictionary`のキーと値になります。",  # noqa
    ##################################################
    "Also, this class requires the `dict_key_type` and `dict_value_type` arguments to specify types of `Dictionary`'s key and value types.": "また、このクラスは`Dictionary`のキーと値の型を指定するための`dict_key_type`と`dict_value_type`引数の指定を必要とします。",  # noqa
    ##################################################
    "The `dict_key_type` only accepts a hashable apysc type, such as the `String`, `Int`, `Number`, and `Boolean`.": "`dict_key_type`は`String`、`Int`、`Number`、`Boolean`などのハッシュ化可能なapyscの型のみを受け付けます。",  # noqa
    ##################################################
    "Similarly, the `dict_value_type` only accepts an apysc type, such as the `String`, `Int`, or `Rectangle`.": "同様に`dict_value_type`引数は`String`や`Int`、`Rectangle`などのapyscの型を受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(background_color="#333", stage_width=250, stage_height=300)\n\ndict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(\n    {\n        ap.Number(50): ap.Number(50),\n        ap.Number(100): ap.Number(125),\n        ap.Number(150): ap.Number(200),\n    }\n)\nwith ap.ForDictKeysAndValues(\n    dict_=dict_,\n    dict_key_type=ap.Number,\n    dict_value_type=ap.Number,\n) as (key, value):\n    ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")\n\nap.save_overall_html(dest_dir_path="for_dict_keys_and_values_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(background_color="#333", stage_width=250, stage_height=300)\n\ndict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(\n    {\n        ap.Number(50): ap.Number(50),\n        ap.Number(100): ap.Number(125),\n        ap.Number(150): ap.Number(200),\n    }\n)\nwith ap.ForDictKeysAndValues(\n    dict_=dict_,\n    dict_key_type=ap.Number,\n    dict_value_type=ap.Number,\n) as (key, value):\n    ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")\n\nap.save_overall_html(dest_dir_path="for_dict_keys_and_values_basic_usage_1/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "  - Notes: This class also has the same arguments and behaves in the same way.": "  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。",  # noqa
    ##################################################
    "## ForDictKeysAndValues API": "## ForDictKeysAndValues API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The loop implementation class for the `ap.Dictionary` keys and values.<hr>": "`ap.Dictionary`のキーと値のためのループのクラスの実装です。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `dict_`: Dictionary[_DictKey, _DictValue]": "- `dict_`: Dictionary[_DictKey, _DictValue]",  # noqa
    ##################################################
    "  - A dictionary to iterate.": "  - イテレーションで扱うための辞書。",
    ##################################################
    "- `dict_key_type`: Type[_DictKey]": "- `dict_key_type`: Type[_DictKey]",
    ##################################################
    "  - A dictionary key type. This interface accepts hashable types, such as the `String`, `Int`, `Number`, or `Boolean`.": "  - 辞書のキーの型。このインターフェイスは`String`、`Int`、`Number`、`Boolean`といったハッシュ化可能な型を受け付けます。",  # noqa
    ##################################################
    "- `dict_value_type`: Type[_DictValue]": "- `dict_value_type`: Type[_DictValue]",
    ##################################################
    "  - A dictionary value type. This interface accepts `InitializeWithBaseValueInterface` subclasses, such as the `Int`, `String`, or `Rectangle`.": "  - 辞書の値の型。ごのインターフェイスは`Int`、`String`、`Rectangle`などの`InitializeWithBaseValueInterface`のサブクラスの型のみ受け付けます。",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(background_color="#333", stage_width=250, stage_height=300)\n>>> dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(\n...     {\n...         ap.Number(50): ap.Number(50),\n...         ap.Number(100): ap.Number(125),\n...         ap.Number(150): ap.Number(200),\n...     }\n... )\n>>> with ap.ForDictKeysAndValues(\n...     dict_=dict_,\n...     dict_key_type=ap.Number,\n...     dict_value_type=ap.Number,\n... ) as (key, value):\n...     _ = ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage(background_color="#333", stage_width=250, stage_height=300)\n>>> dict_: ap.Dictionary[ap.Number, ap.Number] = ap.Dictionary(\n...     {\n...         ap.Number(50): ap.Number(50),\n...         ap.Number(100): ap.Number(125),\n...         ap.Number(150): ap.Number(200),\n...     }\n... )\n>>> with ap.ForDictKeysAndValues(\n...     dict_=dict_,\n...     dict_key_type=ap.Number,\n...     dict_value_type=ap.Number,\n... ) as (key, value):\n...     _ = ap.Rectangle(x=key, y=value, width=50, height=50, fill_color="#0af")\n```',  # noqa
}