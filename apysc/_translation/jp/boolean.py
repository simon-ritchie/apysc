"""This module is for the translation mapping data of the
following document:

Document file: boolean.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Boolean class": "# Boolean クラス",
    ##################################################
    "This page explains the `Boolean` class.": "このページでは`Boolean`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page:": "事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Boolean class?": "## Boolean クラスの概要",
    ##################################################
    "The `Boolean` class is the apysc boolean class. It can accept `bool` or `Boolean` values at the constructor, as follows:": "`Boolean`クラスはapyscの真偽値のクラスです。コンストラクタの引数には以下のコード例のように`bool`や`Boolean`の値を受け付けます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n\nbool_3: ap.Boolean = ap.Boolean(bool_1)\nassert bool_3\n```": "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n\nbool_3: ap.Boolean = ap.Boolean(bool_1)\nassert bool_3\n```",  # noqa
    ##################################################
    "## Note for the Bool class alias": "## Boolクラスのエイリアスの特記事項",
    ##################################################
    "The `Bool` class is the alias of the `Boolean` class. And it behaves the same as the `Boolean` class.": "`Bool`クラスは`Boolean`クラスのエイリアスとなります。`Boolean`クラスと同じ挙動をします。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nassert ap.Boolean == ap.Bool\nassert ap.Boolean(True) == ap.Bool(True)\n```": "```py\n# runnable\nimport apysc as ap\n\nassert ap.Boolean == ap.Bool\nassert ap.Boolean(True) == ap.Bool(True)\n```",  # noqa
    ##################################################
    "## Boolean comparison": "## Boolean クラスの比較制御",
    ##################################################
    "The `Boolean` comparison interface behaves like the Python built-in `bool` value.": "`Boolean`クラスの比較のインターフェイスはPythonビルトインの`bool`クラスの値のように動作します。",  # noqa
    ##################################################
    "You can compare it with the equal comparison operator (`==`), and the `Boolean`\\, `bool`\\, `int`\\, `Int` types are acceptable, as follows:": "等値の比較のオペレーター（`==`）を使って`Boolean`の値と比較することができ、以下のコード例のように`Boolean`や`bool`、`int`、`Int`などの型との比較を行うことができます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 == True  # noqa\nassert bool_1 == ap.Boolean(True)\nassert bool_1 == 1\nassert bool_1 == ap.Int(1)\n```": "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 == True  # noqa\nassert bool_1 == ap.Boolean(True)\nassert bool_1 == 1\nassert bool_1 == ap.Int(1)\n```",  # noqa
    ##################################################
    "Also, the not equal comparison operator (`!=`) is supported, as follows:": "同様に以下のコード例のように非等値のオペレーター（`!=`）もサポートされています。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 != False  # noqa\nassert bool_1 != ap.Boolean(False)\nassert bool_1 != 0\nassert bool_1 != ap.Int(0)\n```": "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1 != False  # noqa\nassert bool_1 != ap.Boolean(False)\nassert bool_1 != 0\nassert bool_1 != ap.Int(0)\n```",  # noqa
    ##################################################
    "You can skip the comparison operator, as follows:": "以下のコードのように比較のオペレーターを省略して使うこともできます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n```": "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nassert bool_1\n\nbool_2: ap.Boolean = ap.Boolean(False)\nassert not bool_2\n```",  # noqa
    ##################################################
    "## Reverse a Boolean value": "## Boolean の値を反転させる",
    ##################################################
    "The `not_` property returns the reversed `Boolean` value:": "`not_`属性は値が反転した`Boolean`の値を返却します:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nbool_2: ap.Boolean = bool_1.not_\nassert not bool_2\n\nbool_3: ap.Boolean = bool_2.not_\nassert bool_3\n```": "```py\n# runnable\nimport apysc as ap\n\nbool_1: ap.Boolean = ap.Boolean(True)\nbool_2: ap.Boolean = bool_1.not_\nassert not bool_2\n\nbool_3: ap.Boolean = bool_2.not_\nassert bool_3\n```",  # noqa
    ##################################################
    "## Boolean class constructor API": "## Boolean クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Boolean class for apysc library.<hr>": "apyscライブラリのための真偽値のクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: Boolean or Int or bool or int": "- `value`: Boolean or Int or bool or int",  # noqa
    ##################################################
    "  - Initial boolean value. 0 or 1 are acceptable for an integer value.": "  - 真偽値の初期値。整数の場合は0か1が受け付けられます。",  # noqa
    ##################################################
    "- `variable_name_suffix`: str, default ''": "- `variable_name_suffix`: str, default ''",  # noqa
    ##################################################
    "  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript's debugging.": "  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。",  # noqa
    ##################################################
    "- `skip_init_substitution_expression_appending`: bool, default False": "- `skip_init_substitution_expression_appending`: bool, default False",  # noqa
    ##################################################
    "  - A boolean indicates whether to skip an initial substitution expression or not. This class uses this option internally.": "  - 初期値の代入のコード表現をスキップするかどうかの真偽値です。このオプションはクラス内部の実装で使用されます。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The Bool class is the alias of the Boolean, and it behaves the same as the Boolean class.<hr>": "BoolクラスはBooleanクラスのエイリアスであり、Booleanクラスと同じように動作します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> bool_val_1: ap.Boolean = ap.Boolean(True)\n>>> bool_val_1\nBoolean(True)\n\n>>> bool_val_2: ap.Bool = ap.Bool(True)\n>>> bool_val_2\nBoolean(True)\n```": "```py\n>>> import apysc as ap\n>>> bool_val_1: ap.Boolean = ap.Boolean(True)\n>>> bool_val_1\nBoolean(True)\n\n>>> bool_val_2: ap.Bool = ap.Bool(True)\n>>> bool_val_2\nBoolean(True)\n```",  # noqa
    ##################################################
    "## value property API": "## value 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current boolean value.<hr>": "現在の真偽値の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `value`: bool": "- `value`: bool",
    ##################################################
    "  - Current boolean value.": "  - 現在の真偽値の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.value = False\n>>> bool_val.value\nFalse\n\n>>> bool_val.value = ap.Boolean(True)\n>>> bool_val.value\nTrue\n```": "```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.value = False\n>>> bool_val.value\nFalse\n\n>>> bool_val.value = ap.Boolean(True)\n>>> bool_val.value\nTrue\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)": "- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)",  # noqa
    ##################################################
    "## not_ property API": "## not_ 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a not condition Boolean value.<hr>": "否定条件を加えた真偽値の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `result`: Boolean": "- `result`: Boolean",
    ##################################################
    "  - Not condition Boolean value.": "  - 反転（否定）させたBoolean型の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.not_\nBoolean(False)\n\n>>> bool_val.value = False\n>>> bool_val.not_\nBoolean(True)\n```": "```py\n>>> import apysc as ap\n>>> bool_val: ap.Boolean = ap.Boolean(True)\n>>> bool_val.not_\nBoolean(False)\n\n>>> bool_val.value = False\n>>> bool_val.not_\nBoolean(True)\n```",  # noqa
}
