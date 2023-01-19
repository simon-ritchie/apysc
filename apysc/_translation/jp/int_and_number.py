"""This module is for the translation mapping data of the
following document:

Document file: int_and_number.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Int and Number classes": "# Int と Number クラス",
    ##################################################
    "This page explains the `Int` and `Number` classes.": "このページでは`Int`と`Number`の各クラスについて説明します。",  # noqa
    ##################################################
    "Before reading on, maybe it is helpful to read the following page:": "事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## Int class": "## Int クラス",
    ##################################################
    "The `Int` class is the apysc integer type. It can accept numeric values at the constructor, as follows:": "`Int`クラスはapyscの整数の型となります。このクラスは以下のコード例のようにコンストラクタに数値の値を受け付けます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nassert int_1 == 10\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nassert int_1 == 10\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(int_1)\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(int_1)\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(int_1)\nint_2 += 15\nassert int_2 == 25\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(int_1)\nint_2 += 15\nassert int_2 == 25\n```",  # noqa
    ##################################################
    "If you specify a float value to the constructor argument, then the `Int` class floor a value:": "もしコンストラクタの引数に浮動小数点数を指定した場合には`Int`クラスはその値の浮動小数点数を切り捨てます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10.5)\nassert int_1 == 10\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10.5)\nassert int_1 == 10\n```",  # noqa
    ##################################################
    "## Number class": "## Number クラス",
    ##################################################
    "The ``Number`` class is the apysc float type. It can accept numeric values at the constructor, same as `Int`:": "`Number`クラスはapyscの浮動小数点数の型です。このクラスは`Int`クラスと同様にコンストラクタの引数に数値を受け付けます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nassert number_1 == 10.5\n\nnumber_2: ap.Number = ap.Number(number_1)\nnumber_2 += 10.5\nassert number_2 == 21\n```": "```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nassert number_1 == 10.5\n\nnumber_2: ap.Number = ap.Number(number_1)\nnumber_2 += 10.5\nassert number_2 == 21\n```",  # noqa
    ##################################################
    "## Note for the Float class alias": "## Floatクラスのエイリアスの特記事項",
    ##################################################
    "The `Float` class is the alias of the `Number` class. It behaves the same as the `Number` class. Maybe a Python developer is familiar with its name rather than the `Number`\\. On the other hand, the `Number` is more common in JavaScript than the `Float`\\.": "`Float`クラスは`Number`クラスのエイリアス。です。このエイリアスは`Number`クラスと同様に動作します。Python開発者の方はもしかしたら`Number`クラスよりもこちらのエイリアスの方が慣れ親しんでいて自然に感じられるかもしれません。一方でJavaScriptなどの開発者の方は`Float`よりも`Number`の方が自然に思えるかもしれません。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nassert ap.Number == ap.Float\nassert ap.Number(10.5) == ap.Float(10.5)\n```": "```py\n# runnable\nimport apysc as ap\n\nassert ap.Number == ap.Float\nassert ap.Number(10.5) == ap.Float(10.5)\n```",  # noqa
    ##################################################
    "## Int and Number classes basic interfaces": "## Int と Number クラスの基本的なインターフェイス",
    ##################################################
    "The `Int` and `Number` classes have the same interfaces. For more details, please see:": "`Int`と`Number`の各クラスは同じ各インターフェイスを持っています。詳細に関しては以下をご確認ください:",  # noqa
    ##################################################
    "- [Int and Number classes basic arithmetic operations](int_and_number_arithmetic_operations.md)": "- [Int と Number クラスの基本的な各計算の制御](jp_int_and_number_arithmetic_operations.md)",  # noqa
    ##################################################
    "- [Int and Number classes basic comparison operations](int_and_number_comparison_operations.md)": "- [Int と Number クラスの基本的な各比較の制御](jp_int_and_number_comparison_operations.md)",  # noqa
    ##################################################
    "- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)": "- [基本的なデータクラスの共通の value インターフェイス](jp_fundamental_data_classes_value_interface.md)",  # noqa
    ##################################################
    "## Int class constructor API": "## Int クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Integer class for apysc library.<hr>": "apyscライブラリ上の整数のためのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: int or float or Int or Number": "- `value`: int or float or Int or Number",  # noqa
    ##################################################
    "  - Initial integer value. If the `float` or `Number` value is specified, this class casts it to an integer.": "  - 整数の初期値。もしも`float`や`Number`の値が指定された場合このクラスは値を整数へと変換します。",  # noqa
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
    "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> int_val\nInt(10)\n\n>>> int_val == 10\nBoolean(True)\n\n>>> int_val == ap.Int(10)\nBoolean(True)\n\n>>> int_val >= 10\nBoolean(True)\n\n>>> int_val += 10\n>>> int_val\nInt(20)\n\n>>> int_val = ap.Int(10.5)\n>>> int_val\nInt(10)\n```": "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> int_val\nInt(10)\n\n>>> int_val == 10\nBoolean(True)\n\n>>> int_val == ap.Int(10)\nBoolean(True)\n\n>>> int_val >= 10\nBoolean(True)\n\n>>> int_val += 10\n>>> int_val\nInt(20)\n\n>>> int_val = ap.Int(10.5)\n>>> int_val\nInt(10)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Int and Number common arithmetic operations](https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html)": "- [Int と Number クラスの共通の各計算制御](https://simon-ritchie.github.io/apysc/jp/jp_int_and_number_arithmetic_operations.html)",  # noqa
    ##################################################
    "- [Int and Number common comparison operations](https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html)": "- [Int と Number クラスの共通の各比較制御](https://simon-ritchie.github.io/apysc/jp/jp_int_and_number_comparison_operations.html)",  # noqa
    ##################################################
    "## Number class constructor API": "## Number クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Floating point number class for apysc library.<hr>": "apyscライブラリ用の浮動小数点数のクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: int or float or Int or Number": "- `value`: int or float or Int or Number",  # noqa
    ##################################################
    "  - Initial floating point number value. This class casts it to float if you specify int or Int value.": "  - 浮動小数点数の初期値。もしもintやIntなどの型の値が指定された場合このクラスは値を浮動小数点数へ変換します。",  # noqa
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
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "The `Float` class is the alias of the Number, and it behaves the same as the Number class.<hr>": "`Float`クラスはNumberクラスのエイリアスであり、このエイリアスはNumberクラスと同様に動作します。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> number: ap.Number = ap.Number(10.5)\n>>> number\nNumber(10.5)\n\n>>> number == 10.5\nBoolean(True)\n\n>>> number == ap.Number(10.5)\nBoolean(True)\n\n>>> number >= 10.5\nBoolean(True)\n\n>>> number += 10.3\n>>> number\nNumber(20.8)\n```": "```py\n>>> import apysc as ap\n>>> number: ap.Number = ap.Number(10.5)\n>>> number\nNumber(10.5)\n\n>>> number == 10.5\nBoolean(True)\n\n>>> number == ap.Number(10.5)\nBoolean(True)\n\n>>> number >= 10.5\nBoolean(True)\n\n>>> number += 10.3\n>>> number\nNumber(20.8)\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Int and Number common arithmetic operations](https://simon-ritchie.github.io/apysc/en/int_and_number_arithmetic_operations.html)": "- [Int と Number クラスの共通の各計算制御](https://simon-ritchie.github.io/apysc/jp/jp_int_and_number_arithmetic_operations.html)",  # noqa
    ##################################################
    "- [Int and Number common comparison operations](https://simon-ritchie.github.io/apysc/en/int_and_number_comparison_operations.html)": "- [Int と Number クラスの共通の各比較制御](https://simon-ritchie.github.io/apysc/jp/jp_int_and_number_comparison_operations.html)",  # noqa
    ##################################################
    "## value property API": "## value 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current number value.<hr>": "現在の数値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `value`: int or float": "- `value`: int or float",
    ##################################################
    "  - Current number value.": "  - 現在の数値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> int_val.value\n10\n\n>>> int_val.value = 20\n>>> int_val.value\n20\n\n>>> int_val.value = ap.Int(30)\n>>> int_val.value\n30\n```": "```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> int_val.value\n10\n\n>>> int_val.value = 20\n>>> int_val.value\n20\n\n>>> int_val.value = ap.Int(30)\n>>> int_val.value\n30\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)": "- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)",  # noqa
}
