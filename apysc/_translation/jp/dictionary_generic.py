"""This module is for the translation mapping data of the
following document:

Document file: dictionary_generic.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Dictionary class generic type settings": "# Dictionary クラスのジェネリックの型アノテーション設定",
    ##################################################
    "This page explains the `Dictionary` class key and value's generic type settings.": "このページでは`Dictionary`クラスのキーと値のジェネリックの型アノテーション設定について説明します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "You can specify the key and value's type at the `Dictionary` type-annotation, as follows:": "以下のコードのように、`Dictionary`クラスではキーと値に対してジェネリックの型アノテーションを行うことができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({"a": 10})\na_value: int = dict_value["a"]\n```': '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({"a": 10})\na_value: int = dict_value["a"]\n```',  # noqa
    ##################################################
    "These generic type-annotations are sometimes helpful for checking with the mypy, Pylance, or other libraries and enhancing safety.": "これらのジェネリックの型アノテーションはmypyやPylanceなどのライブラリによるチェックや安全面で役に立つことがあります。",  # noqa
    ##################################################
    "For example, the following code raises an error of value's type when checking with the Pylance:": "例えば、以下のコード例では辞書の値の型に対するPylanceがエラーが発生します:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({"a": 10})\na_value: str = dict_value["a"]\n```': '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({"a": 10})\na_value: str = dict_value["a"]\n```',  # noqa
    ##################################################
    '```\nExpression of type "int" cannot be assigned to declared type "str"\n  "int" is incompatible with "str"\n```': '```\nExpression of type "int" cannot be assigned to declared type "str"\n  "int" is incompatible with "str"\n```',  # noqa
    ##################################################
    "Also, the following code raises an error of key's type (`str` is required but `int` is specified):": "同じように、以下のコード例では辞書のキーの型でエラーが発生します（`str`が必要になっている一方で`int`が指定されています）。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({"a": 10})\na_value: int = dict_value[10]\n```': '```py\n# runnable\nimport apysc as ap\n\ndict_value: ap.Dictionary[str, int] = ap.Dictionary({"a": 10})\na_value: int = dict_value[10]\n```',  # noqa
    ##################################################
    "If you need to use multiple types and type checking, then use the `Union`\\, as follows:": "もし複数の型の指定が必要な場合、以下のコード例のように`Union`を使うこともできます。",  # noqa
    ##################################################
    "Notes: Alternatively, use the `|` symbol, if you are using Python 3.10 or later) or `Any` type.": "特記事項: もしPython3.10以降をお使いの場合には`|`の記号などを代わりに使用することができます（もしくは`Any`の型を指定するなど）。",  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing import Union\n\nimport apysc as ap\n\n# Accepting the str and int key types.\ndict_value: ap.Dictionary[Union[int, str], int] = ap.Dictionary({"a": 10, 2: 20})\na_value: int = dict_value["a"]\nb_value: int = dict_value[2]\n```': '```py\n# runnable\nfrom typing import Union\n\nimport apysc as ap\n\n# Accepting the str and int key types.\ndict_value: ap.Dictionary[Union[int, str], int] = ap.Dictionary({"a": 10, 2: 20})\na_value: int = dict_value["a"]\nb_value: int = dict_value[2]\n```',  # noqa
    ##################################################
    '```py\n# runnable\nfrom typing import Any\n\nimport apysc as ap\n\n# Accepting all types by specifying the Any type.\ndict_value: ap.Dictionary[Any, Any] = ap.Dictionary({"a": 10, 2: "b"})\na_value: int = dict_value["a"]\nb_value: str = dict_value[2]\n```': '```py\n# runnable\nfrom typing import Any\n\nimport apysc as ap\n\n# Accepting all types by specifying the Any type.\ndict_value: ap.Dictionary[Any, Any] = ap.Dictionary({"a": 10, 2: "b"})\na_value: int = dict_value["a"]\nb_value: str = dict_value[2]\n```',  # noqa
}
