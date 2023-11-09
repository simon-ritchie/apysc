"""This module is for the translation mapping data of the
following document:

Document file: else.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Else class": "# Else クラス",
    ##################################################
    "This page explains the `Else` class.": "このページでは`Else`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses the `Else` class for the same reason as each apysc data type):": "このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscでは`Else`クラスを以下のデータ型のケースと同じ理由で使用しています）:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Else class?": "## Else クラスの概要",
    ##################################################
    "The `Else` class is the apysc branch instruction class. It behaves like the Python built-in `else` keyword.": "`Else`クラスはapyscの条件分岐の指定用のクラスです。このクラスはPythonビルトインの`else`キーワードと同じように動作します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Else` requires using the `with` statement. The `Else` class statement is only acceptable to implement right after the `If` or `Elif` classes statement.": "`Else`クラスは`with`ステートメントとセットで使用する必要があります。`Else`クラスのステートメントは`If`もしくは`Elif`クラスのステートメントの直後でのみ使用することができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\nwith ap.Else():\n    int_1 += 20\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\nwith ap.Else():\n    int_1 += 20\n```",  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "If you insert the code between the `If` (or `Elif`) and `Else` statements, it raises an exception:": "もしも`If`もしくは`Elif`クラスと`Else`クラスのステートメントの間にコードを挿入するとエラーとなります:",  # noqa
    ##################################################
    "```py\nimport apysc as ap\n\nap.Stage()\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\n# If there is a code implementation between the `If` and `Else`, then\n# exceptions will be raised.\nint_2: ap.Int = ap.Int(20)\nwith ap.Else():\n    int_1 += 20\n```": "```py\nimport apysc as ap\n\nap.Stage()\ncondition: ap.Boolean = ap.Boolean(False)\nint_1: ap.Int = ap.Int(10)\n\nwith ap.If(condition):\n    int_1 += 10\n# If there is a code implementation between the `If` and `Else`, then\n# exceptions will be raised.\nint_2: ap.Int = ap.Int(20)\nwith ap.Else():\n    int_1 += 20\n```",  # noqa
    ##################################################
    "```\nValueError: Else interface can only use right after If or Elif interfaces.\n```": "```\nValueError: Else interface can only use right after If or Elif interfaces.\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [If class](if.md)": "- [If クラス](jp_if.md)",
    ##################################################
    "- [Elif class](elif.md)": "- [Elif クラス](jp_elif.md)",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "## Else constructor API": "## Else クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "A class to append else branch instruction expression.<hr>": "elseの分岐条件の表現を追加するためのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `locals_`: dict or None, default None": "- `locals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of an `Else` scope. This setting is useful when you don't want to update each variable by implementing the `Else` scope.": "  - 現在のスコープの各ローカル変数の値。利用する場合にはlocals()関数をこの引数へ指定してください。もし設定された場合には`Else`のスコープの最後にVariableNameMixInクラスを継承したクラスの各変数（例 : Spriteなど）の設定は復元されます。この設定は`Else`クラスのスコープ内で変数を更新したくない場合などに便利なことがあります。",  # noqa
    ##################################################
    "- `globals_`: dict or None, default None": "- `globals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.": "  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・You can only use this class immediately after the `If` or `Elif` statement.<hr>": " ・このクラスは`If`もしくは`Elif`クラスのステートメントの直後にのみ使用することができます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> with ap.If(int_val >= 11):\n...     ap.trace("Value is greater than equal 11.")\n...\n>>> with ap.Else():\n...     ap.trace("Value is less than 11.")\n...\n```': '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> with ap.If(int_val >= 11):\n...     ap.trace("Value is greater than equal 11.")\n...\n>>> with ap.Else():\n...     ap.trace("Value is less than 11.")\n...\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)": "- [分岐条件の各クラスのスコープ内変数の復元設定](https://simon-ritchie.github.io/apysc/jp/jp_branch_instruction_variables_reverting_setting.html)",  # noqa
}
