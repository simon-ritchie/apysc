"""This module is for the translation mapping data of the
following document:

Document file: string_comparison_operations.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# String class comparison operations": "# String クラスの比較の各オペレーション",
    ##################################################
    "This page explains the `String` class comparison operations, like the `=`\\, `>=`\\.": "このページでは`String`クラスの`=`や`>=`などの比較のオペレーションについて説明します。",  # noqa
    ##################################################
    "## Comparison return value type": "## 比較のオペレーションの返却値の型",
    ##################################################
    "Each `String` class comparison operation returns a `Boolean` value, not a Python built-in `bool` value.": "`String`クラスの比較の各オペレーションはPyhtonビルトインの`bool`の値ではなく`Boolean`型の値となります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == "Hello"\nassert result\nassert isinstance(result, ap.Boolean)\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == "Hello"\nassert result\nassert isinstance(result, ap.Boolean)\n```',  # noqa
    ##################################################
    "## Acceptable comparison right-side value types": "## 受け付けられる右側の値の型",
    ##################################################
    "The `str` or `String` types of comparison other value (comparison right-side value) types are acceptable, for instance:": "以下のコード例のように`str`もしくは`String`型の比較対象の値（比較の右側の値）を受け付けることができます:",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == "Hello"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == "Hello"\nassert result\n```',  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == string_2\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nstring_2: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == string_2\nassert result\n```',  # noqa
    ##################################################
    "## Equal comparison": "## 等値条件の比較",
    ##################################################
    "You can use the `==` operator for the equal comparison:": "`==`のオペレーターを使って等値条件の比較を行うことができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == "Hello"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 == "Hello"\nassert result\n```',  # noqa
    ##################################################
    "## Not equal comparison": "## 非等値条件の比較",
    ##################################################
    "You can use the `!=` operator for the not equal comparison:": "`!=`のオペレーターを使って非等値条件の比較を行うことができます。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 != "World"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("Hello")\nresult: ap.Boolean = string_1 != "World"\nassert result\n```',  # noqa
    ##################################################
    "## Less than or greater than comparison": "## 未満もしくは超過条件の比較",
    ##################################################
    "You can use each less than, less than or equal, greater than, greater than equal comparison, with the `<`\\, `<=`\\, `>`\\, `>=` operators, like the Python built-in `str` value. Sometimes these operations are helpful to compare with the date (or date-time) string.": "未満、以下、超過、以上の比較の処理をPythonビルトインの`str`の値のように`<`、`<=`、`>`、`>=`のオペレーターを使っておこなをことができます。ごの処理は日付や日時などの文字列比較などで役に立つことがあります。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 < "1970-01-06"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 < "1970-01-06"\nassert result\n```',  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 <= "1970-01-05"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 <= "1970-01-05"\nassert result\n```',  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 > "1970-01-04"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 > "1970-01-04"\nassert result\n```',  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 >= "1970-01-05"\nassert result\n```': '```py\n# runnable\nimport apysc as ap\n\nstring_1: ap.String = ap.String("1970-01-05")\nresult: ap.Boolean = string_1 >= "1970-01-05"\nassert result\n```',  # noqa
}
