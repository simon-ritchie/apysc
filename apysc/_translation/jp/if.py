"""This module is for the translation mapping data of the
following document:

Document file: if.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# If class": "# If クラス",
    ##################################################
    "This page explains the `If` class.": "このページでは`If`クラスについて説明します。",
    ##################################################
    "Before reading on, maybe it is helpful to read the following page (the apysc uses the `If` class for the same reason of each apysc data type):": "このページを読み進める前に以下のページを確認しておくと役に立つかもしれません（apyscでは基本的なデータクラスと同様の理由で`If`クラスを使用しています）:",  # noqa
    ##################################################
    "- [Why the apysc library doesn't use the Python built-in data type](why_apysc_doesnt_use_python_builtin_data_type.md)": "- [なぜapyscではPythonのビルトインのデータの型を使用していないのか](jp_why_apysc_doesnt_use_python_builtin_data_type.md)",  # noqa
    ##################################################
    "## What is the If class?": "## If クラスの概要",
    ##################################################
    "The `If` class is the apysc branch instruction class. It behaves like the Python built-in `if` keyword.": "`If`クラスはapyscの分岐制御のためのクラスです。このクラスはPythonビルトインの`if`キーワードと似たような形で動作します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The `If` class requires the `with` statement as follows:": "`If`クラスは以下のコード例のように`with`ステートメントと共に使用する必要があります:",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ncondition: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition):\n    ...\n```": "```py\n# runnable\nimport apysc as ap\n\nap.Stage()\ncondition: ap.Boolean = ap.Boolean(True)\nwith ap.If(condition):\n    ...\n```",  # noqa
    ##################################################
    "The `If` class requires passing the `Boolean` value as the condition.": "`If`クラスのコンストラクタの引数には条件としての`Boolean`の値の指定が必要になります。",  # noqa
    ##################################################
    "## See also": "## 関連資料",
    ##################################################
    "- [Elif class](elif.md)": "- [Elif クラス](jp_elif.md)",
    ##################################################
    "- [Else class](else.md)": "- [Else クラス](jp_else.md)",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](branch_instruction_variables_reverting_setting.md)": "- [分岐条件の各クラスのスコープ内変数の復元設定](jp_branch_instruction_variables_reverting_setting.md)",  # noqa
    ##################################################
    "## If constructor API": "## If クラスのコンストラクタのAPI",
    ##################################################
    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>': '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa
    ##################################################
    "**[Interface summary]**": "**[インターフェイス概要]**",
    ##################################################
    "A class to append if branch instruction expression.<hr>": "if文の分岐制御の表現を追加するためのクラス。<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `condition`: Boolean or None": "- `condition`: Boolean or None",
    ##################################################
    "  - Boolean value to be used for judgment.": "  - 判定に使われるBooleanの真偽値。",
    ##################################################
    "- `locals_`: dict or None, default None": "- `locals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's local variables. Set locals() value to this argument. If specified, this interface reverts all local scope VariableNameMixIn variables (like Int, Sprite) at the end of an `If` scope. This setting is useful when you don't want to update each variable by implementing the `If` scope.": "  - 現在のスコープの各ローカル変数。指定する場合にはlocals()関数の値をごの引数に指定してください。もし指定された場合、このインターフェイスは`If`のスコープの終了時に対象のVariableNameMixInクラスの各ローカル変数のインスタンスの値をスコープの開始前の時点に復元します。この設定は`If`のスコープ内の処理でPython上の各ローカル変数の値を更新したくない場合などに便利なことがあります。",  # noqa
    ##################################################
    "- `globals_`: dict or None, default None": "- `globals_`: dict or None, default None",  # noqa
    ##################################################
    "  - Current scope's global variables. Set globals() value to this argument. This setting works the same way as the locals_ argument.": "  - 現在のスコープの各グローバル変数。設定する場合にはglobal()関数の値をこの引数に指定してください。この設定はlocals_引数と同じように動作します。",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> condition: ap.Boolean = int_val >= 10\n>>> with ap.If(condition):\n...     ap.trace("Int value is greater than equal 10!")\n...\n```': '```py\n>>> import apysc as ap\n>>> int_val: ap.Int = ap.Int(10)\n>>> condition: ap.Boolean = int_val >= 10\n>>> with ap.If(condition):\n...     ap.trace("Int value is greater than equal 10!")\n...\n```',  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Each branch instruction class's scope variables reverting setting](https://simon-ritchie.github.io/apysc/en/branch_instruction_variables_reverting_setting.html)": "- [分岐条件の各クラスのスコープ内変数の復元設定](https://simon-ritchie.github.io/apysc/jp/jp_branch_instruction_variables_reverting_setting.html)",  # noqa
}
