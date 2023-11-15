"""This module is for the translation mapping data of the
following document:

Document file: int_and_number_arithmetic_operations.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Int and Number basic arithmetic operations": "# Int と Number クラスの基本的な計算制御",
    ##################################################
    "This page explains basic arithmetic operations of the `Int` and `Number` classes, like addition, multiplication, or incremental addition.": "このページでは`Int`や`Number`の各クラスの加算や乗算などの基本的な計算制御について説明します。",  # noqa
    ##################################################
    "## Common behaviors": "## 共通の挙動",
    ##################################################
    "You can calculate the `Int` and `Number` values with the Python built-in values, such as `int` or `float`\\, as follows:": "`Int`や`Number`の各値は以下のコード例のように`int`や`float`などのPythonビルトインの値と計算することができます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 + 20\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 + 20\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "Also, arithmetic operations with the same types (e.g., `Int` and `Int`) are supported:": "また、同じ型同士（例 : `Int`と`Int`同士など）での計算も同様にサポートしています:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 + int_2\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 + int_2\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "Arithmetic operations are not supported if the left value is the Python built-in value. For instance, the following code raises an exception:": "計算で左側の値がPythonビルトインの値の場合はサポートしていません。例えば以下のコードではエラーとなります:",  # noqa
    ##################################################
    "```py\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\n\n# This will raise the error!\nint_1 = 20 + int_1\n```": "```py\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\n\n# This will raise the error!\nint_1 = 20 + int_1\n```",  # noqa
    ##################################################
    "```\nTypeError: unsupported operand type(s) for +: 'int' and 'Int'\n```": "```\nTypeError: unsupported operand type(s) for +: 'int' and 'Int'\n```",  # noqa
    ##################################################
    "## Addition": "## 加算",
    ##################################################
    "You can add values with the `+` operator.": "`+`のオペレーターを使って各値の加算処理を行うことができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 + 20\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 + 20\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 + int_2\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 + int_2\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10) + ap.Int(20)\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10) + ap.Int(20)\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "Also, you can use the `+=` operator.": "`+=`のオペレーターも同じように使用することができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 += 20\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 += 20\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 += int_2\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(20)\nint_1 += int_2\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "## Subtraction": "## 減算",
    ##################################################
    "You can subtract values with the `-` operator.": "`-`のオペレーターを使って各値の減算を行うことができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(30)\nint_1 = int_1 - 10\nassert int_1 == 20\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(30)\nint_1 = int_1 - 10\nassert int_1 == 20\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(30)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 - int_2\nassert int_1 == 10\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(30)\nint_2: ap.Int = ap.Int(20)\nint_1 = int_1 - int_2\nassert int_1 == 10\n```",  # noqa
    ##################################################
    "Also, you can use the `-=` operator.": "`-=`のオペレーターも同様に使用することができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(50)\nint_1 -= 30\nassert int_1 == 20\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(50)\nint_1 -= 30\nassert int_1 == 20\n```",  # noqa
    ##################################################
    "## Multiplication": "## 乗算",
    ##################################################
    "You can multiply values with the `*` operator.": "`*`のオペレーターを使って各値を乗算することができます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 * 3\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 * 3\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(5)\nint_1 = int_1 * int_2\nassert int_1 == 50\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(5)\nint_1 = int_1 * int_2\nassert int_1 == 50\n```",  # noqa
    ##################################################
    "Also, you can use the `*=` operator.": "`*=`のオペレーターを使うこともできます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 *= 3\nassert int_1 == 30\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 *= 3\nassert int_1 == 30\n```",  # noqa
    ##################################################
    "## Division": "## 除算",
    ##################################################
    "You can divide values with the `/` operator. A return value becomes a `Number` value, not an `Int`\\.": "`/`のオペレーターを使って各値の除算を行うことができます。返却値は`Int`の整数ではなく`Number`の浮動小数点数になります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = int_1 / 4\nassert number_1 == 2.5\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = int_1 / 4\nassert number_1 == 2.5\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(4)\nnumber_1: ap.Number = int_1 / int_2\nassert number_1 == 2.5\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(4)\nnumber_1: ap.Number = int_1 / int_2\nassert number_1 == 2.5\n```",  # noqa
    ##################################################
    "Also, you can use the `/=` operator.": "`/=`のオペレーターを使うこともできます。",
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nnumber_1: ap.Number = ap.Number(10)\nnumber_1 /= 4\nassert number_1 == 2.5\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nnumber_1: ap.Number = ap.Number(10)\nnumber_1 /= 4\nassert number_1 == 2.5\n```",  # noqa
    ##################################################
    "## Floor division": "## 切り捨て除算",
    ##################################################
    "You can divide and floor values with the `//` operator. A return value becomes an `Int` value, not a `Number`\\.": "`//`のオペレーターで除算と浮動小数点数の切り捨てを行うことができます。返却値は`Number`型の浮動小数点数ではなく`Int`の整数となります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 // 4\nassert int_1 == 2\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_1 = int_1 // 4\nassert int_1 == 2\n```",  # noqa
    ##################################################
    "## Modulo": "## 剰余",
    ##################################################
    "You can use the modulo operation with the `%` operator.": "`%`のオペレーターを使って剰余の計算を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: int = int_1 % 3\nassert int_2 == 1\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nint_1: ap.Int = ap.Int(10)\nint_2: int = int_1 % 3\nassert int_2 == 1\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nnumber_1: ap.Number = ap.Number(10.5)\nnumber_2: ap.Number = number_1 % 3\nassert number_2 == 1.5\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\nnumber_1: ap.Number = ap.Number(10.5)\nnumber_2: ap.Number = number_1 % 3\nassert number_2 == 1.5\n```",  # noqa
}
