"""This module is for the translation mapping data of the
following document:

Document file: string.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class": "# String クラス",
    ##################################################
    "This page explains the `String` class.": "このページでは`String`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page:": "事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the String class?": "## String クラスの概要",
    ##################################################
    "The `String` class is the apysc string class. It can accept `str` or `String` values at the constructor, as follows:": "`String`クラスはapyscの文字列用のクラスです。このクラスは以下のコード例のようにコンストラクタの引数に`str`もしくは`String`型の値を受け付けます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nstring_1: ap.String = ap.String("Hello")\nassert string_1 == "Hello"\n\nstring_2: ap.String = ap.String(string_1)\nassert string_2 == "Hello"\n```': '```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nstring_1: ap.String = ap.String("Hello")\nassert string_1 == "Hello"\n\nstring_2: ap.String = ap.String(string_1)\nassert string_2 == "Hello"\n```',  # noqa
    ##################################################
    "## String class interfaces": "## String クラスの各インターフェイス",
    ##################################################
    "For more details about the `String` class each interface, please see the following:": "`String`クラスの各インターフェイスの詳細については以下の資料などをご確認ください:",  # noqa
    ##################################################
    "- [String class comparison operations](string_comparison_operations.md)": "- [String クラスの比較制御](jp_string_comparison_operations.md)",  # noqa
    ##################################################
    "- [String class addition and multiplication operations](string_addition_and_multiplication.md)": "- [String クラスの加算と乗算の制御](jp_string_addition_and_multiplication.md)",  # noqa
    ##################################################
    "## String class constructor API": "## String クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "String class for apysc library.<hr>": "apyscライブラリにおける文字列用のクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: String or str": "- `value`: String or str",
    ##################################################
    "  - Initial string value.": "  - 文字列の値の初期値。",
    ##################################################
    '- `variable_name_suffix`: str, default ""': '- `variable_name_suffix`: str, default ""',  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "- `skip_init_substitution_expression_appending`: bool, default False": "- `skip_init_substitution_expression_appending`: bool, default False",  # noqa
    ##################################################
    "  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.": "  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The `Str` class is the alias of `String`.<hr>": "`Str`クラスは`String`クラスのエイリアスとなります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("Hello")\n>>> string\nString("Hello")\n\n>>> string += " World!"\n>>> string\nString("Hello World!")\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("Hello")\n>>> string\nString("Hello")\n\n>>> string += " World!"\n>>> string\nString("Hello World!")\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [String class comparison operations](https://simon-ritchie.github.io/apysc/en/string_comparison_operations.html)": "- [String クラスの比較制御](https://simon-ritchie.github.io/apysc/jp/jp_string_comparison_operations.html)",  # noqa
    ##################################################
    "- [String class addition and multiplication operations](https://simon-ritchie.github.io/apysc/en/string_addition_and_multiplication.html)": "- [String クラスの加算と乗算の制御](https://simon-ritchie.github.io/apysc/jp/jp_string_addition_and_multiplication.html)",  # noqa
    ##################################################
    "## value property API": "## value 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current string value.<hr>": "現在の文字列の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `value`: str": "- `value`: str",
    ##################################################
    "  - Current string value.": "  - 現在の文字列の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("Hello")\n>>> string.value = "World!"\n>>> string.value\n\'World!\'\n```': '```py\n>>> import apysc as ap\n>>> _ = ap.Stage()\n>>> string: ap.String = ap.String("Hello")\n>>> string.value = "World!"\n>>> string.value\n\'World!\'\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)": "- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)",  # noqa
}
