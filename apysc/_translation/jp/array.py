"""This module is for the translation mapping data of the
following document:

Document file: array.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Array class": "# Array クラス",
    ##################################################
    "This page explains the `Array` class.": "このページでは`Array`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page:": "事前に以下のページを確認しておくと読み進める上で役に立つかもしれません:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Array?": "## Array クラスとは",
    ##################################################
    "The `Array` class is the apysc array class. It behaves like the Python built-in `list` value.": "`Array`クラスはapyscの配列のクラスです。このクラスはPythonビルトインの`list`のように動作します。",  # noqa
    ##################################################
    "## Constructor method": "## コンストラクタメソッド",
    ##################################################
    "The `Array` class constructor method requires iterable objects, like the `list`\\, `tuple`\\, `range`\\, or `Array` value.": "`Array`クラスのコンストラクタでは`list`や`tuple`、`range`、`Array`などのイテラブルなオブジェクトが引数に必要となります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\narr_from_list: ap.Array = ap.Array([1, 2, 3])\nassert arr_from_list == [1, 2, 3]\n\narr_from_tuple: ap.Array = ap.Array((4, 5, 6))\nassert arr_from_tuple == [4, 5, 6]\n\nother_arr: ap.Array = ap.Array([7, 8, 9])\narr_from_arr: ap.Array = ap.Array(other_arr)\nassert arr_from_arr == [7, 8, 9]\n```": "```py\n# runnable\nimport apysc as ap\n\narr_from_list: ap.Array = ap.Array([1, 2, 3])\nassert arr_from_list == [1, 2, 3]\n\narr_from_tuple: ap.Array = ap.Array((4, 5, 6))\nassert arr_from_tuple == [4, 5, 6]\n\nother_arr: ap.Array = ap.Array([7, 8, 9])\narr_from_arr: ap.Array = ap.Array(other_arr)\nassert arr_from_arr == [7, 8, 9]\n```",  # noqa
    ##################################################
    "## Generic type annotation": "## ジェネリックの型アノテーション",
    ##################################################
    "If the `Array` values types are unique, you can set the generic type to an `Array` value. This annotation may be helpful when you use it on the IDE (for type checkers).": "もし`Array`クラスの値の型が一意な場合は配列に対してジェネリックの型の指定を行うことができます。この型アノテーションはIDE上などで便利なケースがあります（型チェックのライブラリなどを使う場合に）。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2])\nint_val: int = arr.pop()\nassert isinstance(int_val, int)\n```": "```py\n# runnable\nimport apysc as ap\n\narr: ap.Array[int] = ap.Array([1, 2])\nint_val: int = arr.pop()\nassert isinstance(int_val, int)\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Funcdamental data classes common value interface](fundamental_data_classes_value_interface.md)": "- [基本的なデータクラスの共通の value インターフェイス](jp_fundamental_data_classes_value_interface.md)",  # noqa
    ##################################################
    "- [Array class append and push interfaces](array_append_and_push.md)": "- [Array クラスの append と push のインターフェイス](jp_array_append_and_push.md)",  # noqa
    ##################################################
    "- [Array class extend and concat interfaces](array_extend_and_concat.md)": "- [Array クラスの extend と concat のインターフェイス](jp_array_extend_and_concat.md)",  # noqa
    ##################################################
    "- [Array class insert and insert_at interfaces](array_insert_and_insert_at.md)": "- [Array クラスの insert と insert_at のインターフェイス](jp_array_insert_and_insert_at.md)",  # noqa
    ##################################################
    "- [Array class pop interface](array_pop.md)": "- [Array クラスの pop インターフェイス](jp_array_pop.md)",  # noqa
    ##################################################
    "- [Array class remove and remove_at interfaces](array_remove_and_remove_at.md)": "- [Array クラスの remove と remove_at のインターフェイス](jp_array_remove_and_remove_at.md)",  # noqa
    ##################################################
    "- [Array class sort interface](array_sort.md)": "- [Array クラスの sort インターフェイス](jp_array_sort.md)",  # noqa
    ##################################################
    "- [Array class reverse interface](array_reverse.md)": "- [Array クラスの reverse インターフェイス](jp_array_reverse.md)",  # noqa
    ##################################################
    "- [Array class slice interface](array_slice.md)": "- [Array クラスの slice インターフェイス](jp_array_slice.md)",  # noqa
    ##################################################
    "- [Array class length interface](array_length.md)": "- [Array クラスの length (配列の長さ取得) のインターフェイス](jp_array_length.md)",  # noqa
    ##################################################
    "- [Array class join interface](array_join.md)": "- [Array クラスの join (値の連結文字列生成) のインターフェイス](jp_array_join.md)",  # noqa
    ##################################################
    "- [Array class index_of interface](array_index_of.md)": "- [Array クラスの index_of (値のインデックス取得) のインターフェイス](jp_array_index_of.md)",  # noqa
    ##################################################
    "- [Array class comparison interfaces](array_comparison.md)": "- [Array クラスの比較の各インターフェイス](jp_array_comparison.md)",  # noqa
    ##################################################
    "## Array class constructor API": "## Array クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Array class for the apysc library.<hr>": "apyscライブラリの配列を扱うためのクラスです。<hr>",
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `value`: Array or list or tuple or range": "- `value`: Array or list or tuple or range",  # noqa
    ##################################################
    "  - Initial array value.": "  - 配列の初期値。",
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
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr\nArray([1, 2, 3])\n\n>>> arr[0]\n1\n\n>>> arr[1]\n2\n\n>>> arr = ap.Array((4, 5, 6))\n>>> arr\nArray([4, 5, 6])\n\n>>> arr = ap.Array(range(3))\n>>> arr\nArray([0, 1, 2])\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr\nArray([1, 2, 3])\n\n>>> arr[0]\n1\n\n>>> arr[1]\n2\n\n>>> arr = ap.Array((4, 5, 6))\n>>> arr\nArray([4, 5, 6])\n\n>>> arr = ap.Array(range(3))\n>>> arr\nArray([0, 1, 2])\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Array class comparison interfaces](https://simon-ritchie.github.io/apysc/en/array_comparison.html)": "- [Array クラスの比較の各インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_array_comparison.html)",  # noqa
    ##################################################
    "## value property API": "## value 属性のAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "Get a current array value.<hr>": "現在の配列の値を取得します。<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `value`: list": "- `value`: list",
    ##################################################
    "  - Current array value.": "  - 現在の配列の値。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.value = [4, 5, 6]\n>>> arr.value\n[4, 5, 6]\n```": "```py\n>>> import apysc as ap\n>>> arr: ap.Array = ap.Array([1, 2, 3])\n>>> arr.value = [4, 5, 6]\n>>> arr.value\n[4, 5, 6]\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [apysc fundamental data classes value interface](https://simon-ritchie.github.io/apysc/en/fundamental_data_classes_value_interface.html)": "- [apyscの基本的なデータクラスの value インターフェイス](https://simon-ritchie.github.io/apysc/jp/jp_fundamental_data_classes_value_interface.html)",  # noqa
}
