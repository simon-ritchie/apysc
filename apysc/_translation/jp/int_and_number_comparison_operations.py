"""This module is for the translation mapping data of the
following document:

Document file: int_and_number_comparison_operations.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Int and Number basic comparison operations": "# Int と Number クラスの基本的な比較制御",
    ##################################################
    "This page explains basic comparison operations of the `Int` and `Number` classes, like the `>=`\\, `<`\\.": "このページでは`Int`や`Number`クラスの`>=`や`<`などの基本的な比較制御について説明します。",  # noqa
    ##################################################
    "## Common behaviors": "## 共通の挙動",
    ##################################################
    "Each comparison operation returns a `Boolean` value, not a Python built-in `bool` value:": "各比較制御はPythonのビルトインの`bool`の値ではなく`Boolean`の値を返却します。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == 10\nassert isinstance(result, ap.Boolean)\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == 10\nassert isinstance(result, ap.Boolean)\n```",  # noqa
    ##################################################
    "You can compare the `Int` or `Number` values with the Python built-in values, like the `int` or `float`:": "`Int`や`Number`の値をPythonビルトインの`int`や`float`などの値と比較することもできます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(20)\nresult: ap.Boolean = int_1 == 20\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(20)\nresult: ap.Boolean = int_1 == 20\nassert result\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nresult: ap.Boolean = number_1 == 10.5\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nresult: ap.Boolean = number_1 == 10.5\nassert result\n```",  # noqa
    ##################################################
    "Also, the comparison between the `Int` and `Int`\\, `Number` and `Number`\\, `Int` and `Number` are supported:": "同様に`Int`と`Int`間、`Number`と`Number`間、`Int`と`Number`間の比較などもサポートしています:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == int_2\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nint_2: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == int_2\nassert result\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nnumber_2: ap.Number = ap.Number(10.5)\nresult: ap.Boolean = number_1 == number_2\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nnumber_1: ap.Number = ap.Number(10.5)\nnumber_2: ap.Number = ap.Number(10.5)\nresult: ap.Boolean = number_1 == number_2\nassert result\n```",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = ap.Number(10)\nresult: ap.Boolean = int_1 == number_1\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nnumber_1: ap.Number = ap.Number(10)\nresult: ap.Boolean = int_1 == number_1\nassert result\n```",  # noqa
    ##################################################
    "## Equal comparison operator": "## 等値条件の比較のオペレーター",
    ##################################################
    "You can use the `==` operator for the equal comparison:": "`==`のオペレーターを使って等値条件の比較を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == 10\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 == 10\nassert result\n```",  # noqa
    ##################################################
    "## Not equal comparison operator": "## 非等値条件の比較のオペレーター",
    ##################################################
    "You can use the `!=` operator for the not equal comparison:": "`!=`のオペレーターを使って非等値条件の比較を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 != 15\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 != 15\nassert result\n```",  # noqa
    ##################################################
    "## Less than comparison operator": "## 未満条件の比較のオペレーター",
    ##################################################
    "You can use the `<` operator for the less than comparison:": "`<`のオペレーターを使って未満条件の比較を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 < 11\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 < 11\nassert result\n```",  # noqa
    ##################################################
    "## Less than or equal comparison operator": "## 以下条件の比較のオペレーター",
    ##################################################
    "You can use the `<=` operator for the less than or equal comparison:": "`<=`のオペレーターを使って以下条件の比較を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 <= 10\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 <= 10\nassert result\n```",  # noqa
    ##################################################
    "## Greater than comparison operator": "## 超過条件の比較のオペレーター",
    ##################################################
    "You can use the `>` operator for the greater than comparison:": "`>`のオペレーターを使って超過条件の比較を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 > 9\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 > 9\nassert result\n```",  # noqa
    ##################################################
    "## Greater than or equal comparison operator": "## 以上条件の比較のオペレーター",
    ##################################################
    "You can use the `>=` operator for the greater than or equal comparison:": "`>=`のオペレーターを使って以上条件の比較を行うことができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 >= 10\nassert result\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\nresult: ap.Boolean = int_1 >= 10\nassert result\n```",  # noqa
}
