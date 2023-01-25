"""This module is for the translation mapping data of the
following document:

Document file: dictionary.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Dictionary class": "# Dictionary クラス",
    ##################################################
    "This page explains the `Dictionary` class.": "このページでは`Dictionary`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page:": "事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Dictionary?": "## Dictionaryクラスの概要",
    ##################################################
    "The `Dictionary` class is the apysc dictionary class. It behaves like the Python built-in `dict` value.": "`Dictionary`クラスはapyscの辞書用のクラスです。ごのクラスはPythonビルトインの`dict`の値のように動作します。",  # noqa
    ##################################################
    "## Constructor method": "## コンストラクタメソッド",
    ##################################################
    "The `Dictionary` class constructor method requires a Python built-in `dict` or `Dictionary` value:": "`Dictionary`のコンストラクタではPythonビルトインの`dict`もしくはapyscの`Dictionary`の値を必要とします:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10})\nassert dict_1 == {"a": 10}\n\ndict_2: ap.Dictionary = ap.Dictionary(dict_1)\nassert dict_1 == dict_2\n```': '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10})\nassert dict_1 == {"a": 10}\n\ndict_2: ap.Dictionary = ap.Dictionary(dict_1)\nassert dict_1 == dict_2\n```',  # noqa
    ##################################################
    "## Value setter interface": "## 値のsetterのインターフェイス",
    ##################################################
    "A `Dictionary` value can be updated by indexing, like the Python built-in `dict` value:": "`Dictionary`の値はPythonのビルトインの`dict`の値と同じようにインデックスを使って更新することができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10})\ndict_1["a"] = 20\nassert dict_1 == {"a": 20}\n```': '```py\n# runnable\nimport apysc as ap\n\ndict_1: ap.Dictionary = ap.Dictionary({"a": 10})\ndict_1["a"] = 20\nassert dict_1 == {"a": 20}\n```',  # noqa
    ##################################################
    "## Value getter interface": "## 値のgetterのインターフェイス",
    ##################################################
    "A `Dictionary` value also can be retrieved by indexing:": "`Dictionary`の値の取得も同様にインデックスを使って行うことができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({"a": int_1})\nint_2: ap.Int = dict_1["a"]\nassert isinstance(int_2, ap.Int)\nassert int_2 == 10\n```': '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({"a": int_1})\nint_2: ap.Int = dict_1["a"]\nassert isinstance(int_2, ap.Int)\nassert int_2 == 10\n```',  # noqa
    ##################################################
    "## Notes of the getter interface": "## getterのインターフェイスの特記事項",
    ##################################################
    "If a `Dictionary` value doesn't have the specified key, a retrieved value type becomes the `AnyValue` type. This behavior occasionally is helpful when a `Dictionary` value is updated dynamically (e.g., updating by the JavaScript event handler).": "もしも`Dictionary`の値が指定されたキーを持たない場合、取り出される値は`AnyValue`型の値となります。この挙動はJavaScript上でのハンドラでの動的な更新処理などを使う際に便利な時があります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({"a": int_1})\nretrieved_val: ap.AnyValue = dict_1["b"]\nassert isinstance(retrieved_val, ap.AnyValue)\n```': '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({"a": int_1})\nretrieved_val: ap.AnyValue = dict_1["b"]\nassert isinstance(retrieved_val, ap.AnyValue)\n```',  # noqa
    ##################################################
    "## Value deletion interface": "## 値の削除のインターフェイス",
    ##################################################
    "A `Dictionary` value can be deleted by the `del` statement, as follows:": "`Dictionary`の値は以下のコード例のように`del`ステートメントで削除することができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({"a": int_1})\ndel dict_1["a"]\nassert dict_1 == {}\n```': '```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\ndict_1: ap.Dictionary = ap.Dictionary({"a": int_1})\ndel dict_1["a"]\nassert dict_1 == {}\n```',  # noqa
    ##################################################
    "## Dictionary class constructor API": "## Dictionary クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Dictionary class for the apysc library.<hr>": "apyscライブラリのための辞書のクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: dict or Dictionary": "- `value`: dict or Dictionary",
    ##################################################
    "  - Initial dictionary value.": "  - 辞書の初期値。",
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "- `skip_init_substitution_expression_appending`: bool, default False": "- `skip_init_substitution_expression_appending`: bool, default False",  # noqa
    ##################################################
    "  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.": "  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})\n>>> dictionary\nDictionary({\'a\': 10})\n\n>>> dictionary["a"]\n10\n\n>>> dictionary["b"] = 20\n>>> dictionary["b"]\n20\n```': '```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({"a": 10})\n>>> dictionary\nDictionary({\'a\': 10})\n\n>>> dictionary["a"]\n10\n\n>>> dictionary["b"] = 20\n>>> dictionary["b"]\n20\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Dictionary class generic type settings](https://simon-ritchie.github.io/apysc/en/dictionary_generic.html)": "- [Dictionary クラスのジェネリックの型設定](https://simon-ritchie.github.io/apysc/jp/jp_dictionary_generic.html)",  # noqa
    ##################################################
    "## value attribute API": "## value 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current dict value.<hr>": "現在の辞書の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `value`: dict": "- `value`: dict",
    ##################################################
    "  - Current dict value.": "  - 現在の辞書の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({})\n>>> dictionary.value = {\"a\": 10}\n>>> dictionary.value\n{'a': 10}\n```": "```py\n>>> import apysc as ap\n>>> dictionary: ap.Dictionary = ap.Dictionary({})\n>>> dictionary.value = {\"a\": 10}\n>>> dictionary.value\n{'a': 10}\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)": "- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)",  # noqa
}
