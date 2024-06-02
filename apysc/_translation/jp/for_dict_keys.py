"""This module is for the translation mapping data of the
following document:

Document file: for_dict_keys.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# ForDictKeys class": "# ForDictKeys クラス",
    ##################################################
    "This page explains the `ForDictKeys` class.": "このページでは`ForDictKeys`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses this class for the same reason for each data type):": "事前に以下のページを読んでおくと役立つかもしれません（apyscライブラリではこのクラスを各データ型と同じように扱っています）。",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What class is this?": "## クラス概要",
    ##################################################
    "The `ForDictKeys` class is the for-loop class.": "`ForDictKeys`クラスはfor文でのループのためのクラスです。",  # noqa
    ##################################################
    "This interface returns `Dictionary`'s key in a loop.": "このインターフェイスはループ内で`Dictionary`のキーを返却します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "This class requires using the `with`-statement.": "このクラスは`with`ステートメントと共に使う必要があります。",  # noqa
    ##################################################
    "The `as`-keyword value becomes a `Dictionary`'s key.": "`as`キーワードの値は`Dictionary`のキーとなります。",  # noqa
    ##################################################
    "Also, this class requires the `dict_key_type` to specify a type of `Dictionary`'s key type.": "また、このクラスは`Dictionary`のキーの型を指定するための`dict_key_type`引数の指定が必要になります。",  # noqa
    ##################################################
    "This type only accepts an apysc type, such as the `String`, `Int`, `Number`, or `Boolean`.": "この型の指定は`String`や`Int`、`Number`、`Boolean`といったapyscの型のみ受け付けます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ndict_: ap.Dictionary[ap.String, int] = ap.Dictionary(\n    {\n        ap.String("apple"): 120,\n        ap.String("orange"): 200,\n    }\n)\nkeys: ap.Array[ap.String] = ap.Array([])\nwith ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:\n    keys.append(key)\nap.assert_arrays_equal(\n    keys,\n    ["apple", "orange"],\n)\n\nap.save_overall_html(dest_dir_path="for_dict_keys_basic_usage_1/")\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    stage_width=0,\n    stage_height=0,\n    background_color=ap.Color("#333"),\n    stage_elem_id="stage",\n)\n\ndict_: ap.Dictionary[ap.String, int] = ap.Dictionary(\n    {\n        ap.String("apple"): 120,\n        ap.String("orange"): 200,\n    }\n)\nkeys: ap.Array[ap.String] = ap.Array([])\nwith ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:\n    keys.append(key)\nap.assert_arrays_equal(\n    keys,\n    ["apple", "orange"],\n)\n\nap.save_overall_html(dest_dir_path="for_dict_keys_basic_usage_1/")\n```',  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "  - Notes: This class also has the same arguments and behaves in the same way.": "  - 特記事項 : このクラスは同じ引数を持ち同様の振る舞いをします。",  # noqa
    ##################################################
    "## ForDictKeys API": "## ForDictKeys API",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "The loop implementation class for the `ap.Dictionary` keys.<hr>": "`ap.Dictionary`の各キーのためのループ用のクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `dict_`: Dictionary[_DictKey, Any]": "- `dict_`: Dictionary[_DictKey, Any]",
    ##################################################
    "  - A dictionary to iterate.": "  - イテレーションで扱うための辞書。",
    ##################################################
    "- `dict_key_type`: Type[_DictKey]": "- `dict_key_type`: Type[_DictKey]",
    ##################################################
    "  - A dictionary key type. This interface accepts hashable types, such as the `String`, `Int`, `Number`, or `Boolean`.": "  - 辞書のキーの型。このインターフェイスは`String`、`Int`、`Number`、`Boolean`といったハッシュ化可能な型を受け付けます。",  # noqa
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
    '```py\n>>> import apysc as ap\n>>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(\n...     {\n...         ap.String("apple"): ap.Boolean(True),\n...         ap.String("orange"): ap.Boolean(False),\n...     }\n... )\n>>> keys: ap.Array[ap.String] = ap.Array([])\n>>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:\n...     keys.append(key)\n...\n>>> ap.assert_arrays_equal(\n...     keys,\n...     ["apple", "orange"],\n... )\n```': '```py\n>>> import apysc as ap\n>>> dict_: ap.Dictionary[ap.String, ap.Boolean] = ap.Dictionary(\n...     {\n...         ap.String("apple"): ap.Boolean(True),\n...         ap.String("orange"): ap.Boolean(False),\n...     }\n... )\n>>> keys: ap.Array[ap.String] = ap.Array([])\n>>> with ap.ForDictKeys(dict_=dict_, dict_key_type=ap.String) as key:\n...     keys.append(key)\n...\n>>> ap.assert_arrays_equal(\n...     keys,\n...     ["apple", "orange"],\n... )\n```',  # noqa
}
