"""This module is for the translation mapping data of the
following document:

Document file: branch_instruction_variables_reverting_setting.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Each branch instruction class's scope variable reverting setting": "# 各分岐制御のクラスのスコープ内の変数値の復元設定",  # noqa
    ##################################################
    "This page explains each branch instruction class (like the `If`\\, `Elif`\\, and `Else`) scope variables reverting setting.": "このページでは`If`や`Elif`、`Else`などの分岐制御の各クラスのスコープ内の変数の復元設定について説明します。",  # noqa
    ##################################################
    "## These interfaces execute with statement code": "## 各インターフェイスのwithステートメント内のコードの実行について",  # noqa
    ##################################################
    "These interfaces execute the code in each branch instruction regardless of the condition, and variables are updated.": "これらのインターフェイスでは条件に罹らわず各分岐箇所の（JavaScriptのコード出力のために）コードが実行され、Python上での変数の値が更新されます。",  # noqa
    ##################################################
    "For example, the following code of the condition is `False`\\, but the value of int is 20 on the Python:": "例えば以下のコード例では条件は`False`となっていますがPython上の値は20に更新されます:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\nassert int_1 == 20\n```": "```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\nassert int_1 == 20\n```",  # noqa
    ##################################################
    "This condition is skipped in JavaScript (converted code) since the condition is not satisfied.": "この部分はJavaScriptへ変換されたコード上では条件を満たさないため実行されません。",  # noqa
    ##################################################
    "## Scope variables reverting setting": "## スコープ内の変数の復元設定",
    ##################################################
    "The `If`, `Elif`, and `Else` classes have the arguments of the `locals_` and `globals_` (basically set the `locals()` and `globals()` built-in functions return value). If these arguments are specified, the scope variables are reverted when ended each scope (e.g., `If` scope).": "`If`や`Elif`、`Else`などのクラスは`locals_`と`globals_`の引数の省略可能なオプションを持っています（基本的に設定する場合にはビルトインの`locals()`関数と`globals()`関数の値を設定します）。これらの引数へ値が設定された場合にはスコープ内の各変数が`If`クラスなどのそれぞれのスコープが終了した時点でスコープ前の段階に復元されます。",  # noqa
    ##################################################
    "This interface is occasionally helpful when you don't want to update the variables in each branch instruction scope.": "このインターフェイスのオプションは各分岐の箇所でPythonの変数を更新したく無い場合などに役に立つケースがあります。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition, locals_=locals(), globals_=globals()):\n    int_1 += 10\nassert int_1 == 10\n```": "```py\n# runnable\nimport apysc as ap\n\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition, locals_=locals(), globals_=globals()):\n    int_1 += 10\nassert int_1 == 10\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [If class](if.md)": "- [If クラス](jp_if.md)",
    ##################################################
    "- [Elif class](elif.md)": "- [Elif クラス](jp_elif.md)",
    ##################################################
    "- [Else class](else.md)": "- [Else クラス](jp_else.md)",
}
