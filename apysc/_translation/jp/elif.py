"""This module is for the translation mapping data of the
following document:

Document file: elif.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Elif class": "# Elif クラス",
    ##################################################
    "This page explains the `Elif` class.": "このページでは`Elif`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses the `Elif` class for the same reason as each other data type):": "このページを読み進める前に以下のページをご確認いただくと役に立つかもしれません（`Elif`クラスも他のデータのクラスと同じ理由で使われています）:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the Elif class?": "## Elif クラスの概要",
    ##################################################
    "The `Elif` class is the apysc branch instruction class. It behaves like the Python built-in `elif` keyword.": "`Elif`クラスはapyscの分岐条件用のクラスです。このクラスはPythonのビルトインの`elif`のキーワードと同じように動作します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `Elif` class requires using the `with` statement. Also, The `Elif` class statement is only acceptable to implement right after the `If` or `Elif` classes statement.": "`Elif`クラスは`with`ステートメントと共に使う必要があります。また、`Elif`クラスは`If`や`Elif`クラスのステートメントの直後にのみ使用することができます。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\ncondition_1: ap.Boolean = ap.Boolean(False)\ncondition_2: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition_1):\n    int_1 += 20\nwith ap.Elif(condition_2):\n    int_1 += 30\n```": "```py\n# runnable\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\ncondition_1: ap.Boolean = ap.Boolean(False)\ncondition_2: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition_1):\n    int_1 += 20\nwith ap.Elif(condition_2):\n    int_1 += 30\n```",  # noqa
    ##################################################
    "## Notes": "## 特記事項",
    ##################################################
    "If you insert the code between the `If` (or `Elif`) and `Elif` statements, then it raises exceptions:": "もし`If`（もしくは`Elif`）クラスと`Elif`クラスのステートメント間にコードを挟んだ場合エラーとなります:",  # noqa
    ##################################################
    "```py\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\ncondition_1: ap.Boolean = ap.Boolean(False)\ncondition_2: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition_1):\n    int_1 += 20\n# Code inserting between the `If` and `Elif` will raise an exception.\nint_2: ap.Int = ap.Int(30)\nwith ap.Elif(condition_2):\n    int_1 += 30\n```": "```py\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\ncondition_1: ap.Boolean = ap.Boolean(False)\ncondition_2: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition_1):\n    int_1 += 20\n# Code inserting between the `If` and `Elif` will raise an exception.\nint_2: ap.Int = ap.Int(30)\nwith ap.Elif(condition_2):\n    int_1 += 30\n```",  # noqa
    ##################################################
    "```\nValueError: Elif interface can only use right after If or Elif interfaces.\n```": "```\nValueError: Elif interface can only use right after If or Elif interfaces.\n```",  # noqa
    ##################################################
    "Also, you can't create the condition (`Boolean` value) at the `Elif` constructor position (the same goes for the comparison operators), for instance:": "また、`Elif`のコンストラクタにて直接`Boolean`の値の条件値を作成したり比較表現を行うことはできません。例えば以下のコードでもエラーとなります:",  # noqa
    ##################################################
    "```py\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\ncondition_1: ap.Boolean = ap.Boolean(False)\ncondition_2: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition_1):\n    int_1 += 20\nwith ap.Elif(int_1 == 10):\n    int_1 += 30\n```": "```py\nimport apysc as ap\n\nint_1: ap.Int = ap.Int(10)\n\ncondition_1: ap.Boolean = ap.Boolean(False)\ncondition_2: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition_1):\n    int_1 += 20\nwith ap.Elif(int_1 == 10):\n    int_1 += 30\n```",  # noqa
    ##################################################
    "```\nValueError: Elif interface can only use right after If or Elif interfaces.\n\nMaybe you are using Int or String, or anything-else comparison expression at Elif constructor (e.g., `with Elif(any_value == 10, ...):`).\nCurrently, that specifying expression directly is not supported, so please define conditions separately as follows:\ncondition: Boolean = any_value == 10\n...\nwith Elif(condition, ...):\n```": "```\nValueError: Elif interface can only use right after If or Elif interfaces.\n\nMaybe you are using Int or String, or anything-else comparison expression at Elif constructor (e.g., `with Elif(any_value == 10, ...):`).\nCurrently, that specifying expression directly is not supported, so please define conditions separately as follows:\ncondition: Boolean = any_value == 10\n...\nwith Elif(condition, ...):\n```",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [If class](if.md)": "- [If クラス](jp_if.md)",
    ##################################################
    "- [Else class](else.md)": "- [Else クラス](jp_else.md)",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "## Elif constructor API": "## Elif クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "A class to append the `else if` branch instruction expression.<hr>": "`else if`の分岐条件の表現を追加するためのクラスです。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `condition`: Boolean or None": "- `condition`: Boolean or None",
    ##################################################
    "  - Boolean value to be used for judgment.": "  - 判定に使われるBooleanの真偽値。",
    ##################################################
    "- `locals_`: dict or None, default None": "- `locals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of an `Elif` scope. This setting is useful when you don't want to update each variable by implementing the `Elif` scope.": "  - 現在のスコープの各ローカル変数。locals()関数の値を引数に指定してください。もしも指定された場合には`Elif`のスコープの終了時にこのインターフェイスはVariableNameMixInクラスを継承した各変数（例 : `Sprite`クラスなど）の値をスコープ前の状態に復元します。この設定は`Elif`スコープ内のコードで各変数を更新したくない場合に役立ちます。",  # noqa
    ##################################################
    "- `globals_`: dict or None, default None": "- `globals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.": "  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    " ・Currently the apysc can not initialize condition value in the constructor. ": " ・現在apyscでは条件値をコンストラクタ内で直接作成することはできません。",  # noqa
    ##################################################
    "<br> ・You can only use this class immediately after the `If` or `Elif` statement.<hr>": "<br> ・このクラスは`If`や`Elif`クラスによるステートメントの直後でのみ使用することができます。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> # You can avoid notes exception by predefining condition\n>>> # value, as follows:\n>>> import apysc as ap\n>>> any_value: ap.Int = ap.Int(10)\n>>> condition_1: ap.Boolean = any_value >= 10\n>>> condition_2: ap.Boolean = any_value >= 5\n>>> with ap.If(condition_1):\n...     # Do something here\n...     pass\n...\n>>> with ap.Elif(condition_2):\n...     # Do something else here\n...     pass\n...\n```": "```py\n>>> # You can avoid notes exception by predefining condition\n>>> # value, as follows:\n>>> import apysc as ap\n>>> any_value: ap.Int = ap.Int(10)\n>>> condition_1: ap.Boolean = any_value >= 10\n>>> condition_2: ap.Boolean = any_value >= 5\n>>> with ap.If(condition_1):\n...     # Do something here\n...     pass\n...\n>>> with ap.Elif(condition_2):\n...     # Do something else here\n...     pass\n...\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)": "- [分岐条件の各クラスのスコープ内変数の復元設定](https://simon-ritchie.github.io/apysc/jp/jp_branch_instruction_variables_reverting_setting.html)",  # noqa
}
