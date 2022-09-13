"""This module is for the translation mapping data of the
following document:

Document file: string_addition_and_multiplication.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class addition and multiplication operations": "# String クラスの加算と乗算の各オペレーション",  # noqa
    ##################################################
    "This page explains the `String` class addition and multiplication operations.": "このページでは`String`クラスの加算と乗算のオペレーションについて説明します。",  # noqa
    ##################################################
    "## Addition": "## 加算",
    ##################################################
    "The `String` class addition operation (`+`) returns the concatenated `String` value:": "`String`クラスの加算のオペレーション（`+`）は連結された`String`型の値を返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = string_1 + " World!"\nassert string_2 == "Hello World!"\nassert isinstance(string_2, ap.String)\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = string_1 + " World!"\nassert string_2 == "Hello World!"\nassert isinstance(string_2, ap.String)\n```',  # noqa
    ##################################################
    "Also, the `+=` operator is supported:": "また、`+=`のオペレーターもサポートしています:",
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_1 += " World!"\nassert string_1 == "Hello World!"\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_1 += " World!"\nassert string_1 == "Hello World!"\n```',  # noqa
    ##################################################
    "A `String` value + Python built-in `str` operation is supported. Similarly, a `String` value + `String` value operation is also supported:": "`String`の値とPythonのビルトインの`str`の値によるオペレーションもサポートしています。`String`の値同士のオペレーションも同様です。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = ap.String(" World!")\nstring_3: ap.String = string_1 + string_2\nassert string_3 == "Hello World!"\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = ap.String(" World!")\nstring_3: ap.String = string_1 + string_2\nassert string_3 == "Hello World!"\n```',  # noqa
    ##################################################
    "But a Python built-in `str` + `String` value is not supported; for instance, the following code raises an error:": "一方で`str`の値と`String`の値の場合（左側を`str`の値にする場合）はサポートしていません。例えば以下のコード例ではエラーとなります:",  # noqa
    ##################################################
    '```py\nimport apysc as ap\n\nstring_1: ap.String = ap.String(" World!")\nstring_2: ap.String = "Hello" + string_1\n```': '```py\nimport apysc as ap\n\nstring_1: ap.String = ap.String(" World!")\nstring_2: ap.String = "Hello" + string_1\n```',  # noqa
    ##################################################
    "```\nTypeError: must be str, not String\n```": "```\nTypeError: must be str, not String\n```",  # noqa
    ##################################################
    "## Multiplication": "## 乗算",
    ##################################################
    "The `String` class multiplication operation (`*`) returns the repeated `String` value, same behaviors as the Python built-in `str` value:": "`String`クラスの乗算のオペレーション（`*`）はPythonビルトインの文字列のように値を繰り返した文字列を返却します。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = string_1 * 3\nassert string_2 == "HelloHelloHello"\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = string_1 * 3\nassert string_2 == "HelloHelloHello"\n```',  # noqa
    ##################################################
    "The `int` or `Int` values are acceptable at the operation's right-side value:": "`int`もしくは`Int`型の値を右側の値として受け付けることができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nint_1: ap.Int = ap.Int(3)\nstring_2: ap.String = string_1 * int_1\nassert string_2 == "HelloHelloHello"\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nint_1: ap.Int = ap.Int(3)\nstring_2: ap.String = string_1 * int_1\nassert string_2 == "HelloHelloHello"\n```',  # noqa
}
